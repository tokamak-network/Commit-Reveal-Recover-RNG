// Copyright 2023 justin
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
import { useWeb3Contract } from "react-moralis"
import { Switch } from "@headlessui/react"
import dynamic from "next/dynamic"
import { abi, contractAddresses } from "./../constants"
import { useMoralis } from "react-moralis"
import { useEffect, useState } from "react"
import { createTestCases2 } from "./../utils/testFunctions"
import { Input, useNotification, Button, Toggle } from "web3uikit"
import { getBitLenth2, getLength } from "../utils/testFunctions"
import { toBeHex, dataLength, ethers } from "ethers"
import React from "react"
const ReactJson = dynamic(() => import("react-json-view-with-toggle"), {
    ssr: false,
})
function classNames(...classes) {
    return classes.filter(Boolean).join(" ")
}
export default function Commit() {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex)
    const randomAirdropAddress =
        chainId in contractAddresses ? contractAddresses[chainId][0] : null
    const [commitCalldata, setCommitCalldata] = useState()
    const [commitData, setCommitData] = useState()
    const [commitDataState, setCommitDataState] = useState("initial")
    const { runContractFunction: enterEventByCommit, isLoading, isFetching } = useWeb3Contract()
    const [enabled, setEnabled] = useState(false)
    const dispatch = useNotification()

    function validation() {
        if (commitData == undefined || commitData == "") {
            setCommitDataState("error")
            return false
        } else if (commitData == "0x" || commitData == "0" || commitData == 0) {
            dispatch({
                type: "error",
                message: "Commit Value cannot be 0",
                title: "Error Message",
                position: "topR",
                icon: "bell",
            })
            return false
        }
        return true
    }
    async function enterEventByCommitFunction() {
        if (validation()) {
            const enterEventByCommitOptions = {
                abi: abi,
                contractAddress: randomAirdropAddress,
                functionName: "enterEventByCommit",
                params: {
                    _c: commitCalldata,
                },
            }
            await enterEventByCommit({
                params: enterEventByCommitOptions,
                onSuccess: handleSuccess,
                onError: (error) => {
                    dispatch({
                        type: "error",
                        message:
                            error?.error?.message && error.error.message != "execution reverted"
                                ? error.error.message
                                : error.error
                                ? new ethers.Interface(abi).parseError(
                                      error.error.data.originalError.data
                                  ).name
                                : error?.data?.message,
                        title: "Error Message",
                        position: "topR",
                        icon: "bell",
                    })
                },
            })
        }
    }
    const handleSuccess = async function (tx) {
        await tx.wait(1)
        handleNewNotification(tx)
        //updateUI()
    }
    //async function updateUI() {}
    const handleNewNotification = function () {
        dispatch({
            type: "info",
            message: "Transaction Completed",
            title: "Tx Notification",
            position: "topR",
            icon: "bell",
        })
    }
    useEffect(() => {
        if (isWeb3Enabled) {
            //updateUI()
        }
    }, [isWeb3Enabled])
    return (
        <div className="border-dashed border-amber-950 border-2 rounded-lg p-10 m-5">
            <h3 data-testid="test-form-title" className="sc-eXBvqI eGDBJr font-bold">
                Join Airdrop Event by Commit
            </h3>
            <div className="mb-2 mt-2 flex flex-row">
                <div className="mx-1.5">JSON</div>
                <Switch
                    checked={enabled}
                    onChange={setEnabled}
                    className="group relative inline-flex h-5 w-10 flex-shrink-0 cursor-pointer items-center justify-center rounded-full focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2"
                >
                    <span className="sr-only">Use setting</span>
                    <span
                        aria-hidden="true"
                        className="pointer-events-none absolute h-full w-full rounded-md bg-white"
                    />
                    <span
                        aria-hidden="true"
                        className={classNames(
                            enabled ? "bg-indigo-600" : "bg-emerald-600",
                            "pointer-events-none absolute mx-auto h-4 w-9 rounded-full transition-colors duration-200 ease-in-out"
                        )}
                    />
                    <span
                        aria-hidden="true"
                        className={classNames(
                            enabled ? "translate-x-5" : "translate-x-0",
                            "pointer-events-none absolute left-0 inline-block h-5 w-5 transform rounded-full border border-gray-200 bg-white shadow ring-0 transition-transform duration-200 ease-in-out"
                        )}
                    />
                </Switch>
                <div className="mx-1">Decimal</div>
            </div>
            <div className="mb-2 mt-5 flex flex-row">
                <Input
                    label={enabled ? "Commit Value in Decimal" : "Commit Value in JSON Object"}
                    type="text"
                    placeholder=""
                    id="CommitValue"
                    validation={{ required: true }}
                    value={commitData}
                    onChange={(e) => {
                        setCommitData(e.target.value)
                        if (enabled) {
                            let stringVal = e.target.value
                            if (e.target.value.length == 0) stringVal = "0"
                            setCommitCalldata({
                                val: toBeHex(stringVal, getLength(dataLength(toBeHex(stringVal)))),
                                bitlen: getBitLenth2(BigInt(stringVal)),
                            })
                        } else {
                            if (e.target.value.length != 0)
                                setCommitCalldata(JSON.parse(e.target.value))
                        }
                    }}
                    state={commitDataState}
                    errorMessage="Commit Value is required"
                    width="50%"
                />
                <Button
                    style={{ marginLeft: "10px", fontWeight: "bold" }}
                    onClick={() => {
                        let rand = window.crypto.getRandomValues(new Uint8Array(2048 / 8))
                        const bytesHex = rand.reduce(
                            (o, v) => o + ("00" + v.toString(16)).slice(-2),
                            ""
                        )
                        if (enabled) setCommitData(BigInt("0x" + bytesHex).toString(10))
                        else
                            setCommitData(
                                JSON.stringify({
                                    val: toBeHex(
                                        "0x" + bytesHex,
                                        getLength(dataLength("0x" + bytesHex))
                                    ),
                                    bitlen: getBitLenth2(BigInt("0x" + bytesHex)),
                                })
                            )
                        let stringVal = BigInt("0x" + bytesHex).toString(10)
                        if (stringVal.length == 0) stringVal = "0"
                        setCommitCalldata({
                            val: toBeHex(stringVal, getLength(dataLength(toBeHex(stringVal)))),
                            bitlen: getBitLenth2(BigInt(stringVal)),
                        })
                    }}
                    text="Auto Generate"
                    theme="primary"
                />
            </div>
            <button
                id="enterEventByCommit"
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto mt-3"
                disabled={isLoading || isFetching}
                type="button"
                onClick={enterEventByCommitFunction}
            >
                {isLoading || isFetching ? (
                    <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                ) : (
                    <div>Commit</div>
                )}
            </button>
            <div
                className="mt-4 ml-1 text-base h-40"
                style={{ textOverflow: "ellipsis", overflow: "hidden" }}
            >
                {/* calldata: {JSON.stringify(commitCalldata)} */}
                <ReactJson src={commitCalldata} />
            </div>
            <div className="mt-2">
                <div>
                    Commit your value using the Auto Generate button or Type your number manually.
                </div>
                <div>*Auto Generate button uses the window.crypto.getRandomValues function.</div>
            </div>
        </div>
    )
}
