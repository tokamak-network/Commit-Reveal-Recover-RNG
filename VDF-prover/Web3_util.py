from web3 import Web3
import configparser
import json


def pad_hex(x):
    n = (64 - (len(x) % 64)) % 64
    return ('0' * n) + x
# keccack hash function outputs int for strings 
def mod_hash_eth(n, *strings):
  # concatenate integer strings as even bytes
  # for example, [10, 17] -> 0x0a, 0x11 -> 0x0a11
  toHex = [format(int(x), '02x') for x in strings]
  padToEvenLen = [pad_hex(x) for x in toHex]
  input = ''.join(padToEvenLen)
  print("input", input)
  r = Web3.keccak(hexstr=input)
  print(r.hex())
  r = int(r.hex(), 16)
  r = r % n
  return r

def read_config():
    """Read and return configuration from a file."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Networks'], config['Contract']

def get_web3(rpc_url):
    """Initialize and return a Web3 instance with the given RPC URL."""
    return Web3(Web3.HTTPProvider(rpc_url))

def select_network(networks, contract_details):
    """Prompt the user to select a network and return the corresponding Web3 instance."""
    print(f"Select a network for the contract address {contract_details['address']}:")
    print("1. Ethereum Mainnet")
    print("2. Goerli Testnet")
    print("3. Titan (Layer 2) Mainnet")
    print("4. Titan (Layer 2) Goerli Testnet")
    choice = input("Choice: ")
    print("")

    if choice == "1":
        return get_web3(networks['ethereum_mainnet'])
    elif choice == "2":
        return get_web3(networks['goerli_testnet'])
    elif choice == "3":
        return get_web3(networks['titan_mainnet'])
    elif choice == "4":
        return get_web3(networks['titan_goerli'])
    else:
        print("Invalid selection. Please try again.")
        return select_network(networks)

def setup_contract(web3, contract_details):
    """Create and return a contract object using the provided Web3 instance."""
    with open(contract_details['abi'], 'r') as abi_file:
        contract_abi = json.load(abi_file)
    contract_address = Web3.to_checksum_address(contract_details['address'])
    return web3.eth.contract(address=contract_address, abi=contract_abi)

def get_commit_reveal_values(contract, round_number):
    """Retrieve all CommitRevealValues for a given round until an empty participant address is found."""
    commit_reveal_values = []
    index = 0
    while True:
        value = contract.functions.commitRevealValues(round_number, index).call()
        # participantAddress가 '0x000...'인 경우 더 이상의 유효한 값이 없다고 간주
        if value[2] == '0x0000000000000000000000000000000000000000':
            break
        commit_reveal_values.append(value)
        index += 1
    return commit_reveal_values
    
def get_stage(stage_value):
    """Convert stage value to stage name."""
    stages = ["Commit", "Reveal", "Finished"]
    return stages[stage_value] if stage_value < len(stages) else "Unknown"
    
def parse_commits(commit_reveal_values):
    """Parse commit reveal values and return as a list of dictionaries."""
    parsed_data = []
    """
    for value in commit_reveal_values:
        parsed_entry = {
            "c": value[0],
            "a": value[1],
            "participantAddress": value[2]
        }
        parsed_data.append(parsed_entry)
    """
    for value in commit_reveal_values:
        parsed_data.append(value[0])
    return parsed_data
    
def parse_value_at_round(value_at_round):
    """Parse a ValueAtRound struct and return as a dictionary."""
    return {
        "omega": value_at_round[0],
        "bStar": value_at_round[1],
        "numOfParticipants": value_at_round[2],
        "g": value_at_round[3],
        "h": value_at_round[4],
        "n": value_at_round[5],
        "T": value_at_round[6],
        "isCompleted": value_at_round[7],
        "isAllRevealed": value_at_round[8]
    }

def get_contract_values():
    networks, contract_details = read_config()
    web3 = select_network(networks, contract_details)
    contract = setup_contract(web3, contract_details)

    """Read and return specific values from the smart contract."""
    round_info = contract.functions.round().call()
    stage = get_stage(contract.functions.stage().call())

    # valuesAtRound 정보 가져오기 및 파싱
    raw_value_at_round = contract.functions.valuesAtRound(round_info).call()
    value_at_round = parse_value_at_round(raw_value_at_round)

    # commitRevealValues 정보 가져오기 및 파싱
    commit_reveal_values = get_commit_reveal_values(contract, round_info)
    commits = parse_commits(commit_reveal_values)

    # 결과 출력
    print(f"Round: {round_info}, Stage: {stage}")
    print(f"Divisor  n: {value_at_round['n']}")
    print(f"Generator g: {value_at_round['g']}")
    print(f"Value h: {value_at_round['h']}")
    print(f"Time delay T: {value_at_round['T']}")
    print(f"Commits: {commits}")
    #for value in parsed_commit_reveal_values:
    #    print(value)

    return round_info, stage, value_at_round, commits




if __name__ == "__main__":
    c = ['10', '11']
    # c = even_hex_concat(c)
    print(c)
    print(mod_hash_eth(100000, *c))
    # get_contract_values()