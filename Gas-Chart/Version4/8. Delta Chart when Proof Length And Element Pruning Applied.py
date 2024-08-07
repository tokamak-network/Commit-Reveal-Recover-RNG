# Copyright 2024 justin
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

data = [
    [ '0', '3071986', 'λ2048', 'T2^20' ],
    [ '0', '3238167', 'λ2048', 'T2^21' ],
    [ '0', '3401433', 'λ2048', 'T2^22' ],
    [ '0', '3568367', 'λ2048', 'T2^23' ],
    [ '0', '3735574', 'λ2048', 'T2^24' ],
    [ '0', '3904507', 'λ2048', 'T2^25' ],
    [ '1', '2909174', 'λ2048', 'T2^20' ],
    [ '1', '3074025', 'λ2048', 'T2^21' ],
    [ '1', '3235735', 'λ2048', 'T2^22' ],
    [ '1', '3401763', 'λ2048', 'T2^23' ],
    [ '1', '3568576', 'λ2048', 'T2^24' ],
    [ '1', '3736471', 'λ2048', 'T2^25' ],
    [ '2', '2747554', 'λ2048', 'T2^20' ],
    [ '2', '2911073', 'λ2048', 'T2^21' ],
    [ '2', '3072866', 'λ2048', 'T2^22' ],
    [ '2', '3237132', 'λ2048', 'T2^23' ],
    [ '2', '3403520', 'λ2048', 'T2^24' ],
    [ '2', '3569661', 'λ2048', 'T2^25' ],
    [ '3', '2588362', 'λ2048', 'T2^20' ],
    [ '3', '2751002', 'λ2048', 'T2^21' ],
    [ '3', '2911687', 'λ2048', 'T2^22' ],
    [ '3', '3074269', 'λ2048', 'T2^23' ],
    [ '3', '3239816', 'λ2048', 'T2^24' ],
    [ '3', '3404373', 'λ2048', 'T2^25' ],
    [ '4', '2430590', 'λ2048', 'T2^20' ],
    [ '4', '2592664', 'λ2048', 'T2^21' ],
    [ '4', '2752178', 'λ2048', 'T2^22' ],
    [ '4', '2913883', 'λ2048', 'T2^23' ],
    [ '4', '3079487', 'λ2048', 'T2^24' ],
    [ '4', '3242164', 'λ2048', 'T2^25' ],
    [ '5', '2277606', 'λ2048', 'T2^20' ],
    [ '5', '2437336', 'λ2048', 'T2^21' ],
    [ '5', '2597171', 'λ2048', 'T2^22' ],
    [ '5', '2757360', 'λ2048', 'T2^23' ],
    [ '5', '2922131', 'λ2048', 'T2^24' ],
    [ '5', '3083862', 'λ2048', 'T2^25' ],
    [ '6', '2129852', 'λ2048', 'T2^20' ],
    [ '6', '2289191', 'λ2048', 'T2^21' ],
    [ '6', '2447951', 'λ2048', 'T2^22' ],
    [ '6', '2606915', 'λ2048', 'T2^23' ],
    [ '6', '2770455', 'λ2048', 'T2^24' ],
    [ '6', '2931777', 'λ2048', 'T2^25' ],
    [ '7', '1995322', 'λ2048', 'T2^20' ],
    [ '7', '2153689', 'λ2048', 'T2^21' ],
    [ '7', '2311218', 'λ2048', 'T2^22' ],
    [ '7', '2469381', 'λ2048', 'T2^23' ],
    [ '7', '2632284', 'λ2048', 'T2^24' ],
    [ '7', '2792359', 'λ2048', 'T2^25' ],
    [ '8', '1884013', 'λ2048', 'T2^20' ],
    [ '8', '2040774', 'λ2048', 'T2^21' ],
    [ '8', '2197857', 'λ2048', 'T2^22' ],
    [ '8', '2355173', 'λ2048', 'T2^23' ],
    [ '8', '2516183', 'λ2048', 'T2^24' ],
    [ '8', '2675469', 'λ2048', 'T2^25' ],
    [ '9', '1817855', 'λ2048', 'T2^20' ],
    [ '9', '1973222', 'λ2048', 'T2^21' ],
    [ '9', '2129116', 'λ2048', 'T2^22' ],
    [ '9', '2286058', 'λ2048', 'T2^23' ],
    [ '9', '2445803', 'λ2048', 'T2^24' ],
    [ '9', '2603753', 'λ2048', 'T2^25' ],
    [ '10', '1842438', 'λ2048', 'T2^20' ],
    [ '10', '1996403', 'λ2048', 'T2^21' ],
    [ '10', '2151756', 'λ2048', 'T2^22' ],
    [ '10', '2307041', 'λ2048', 'T2^23' ],
    [ '10', '2466822', 'λ2048', 'T2^24' ],
    [ '10', '2622673', 'λ2048', 'T2^25' ],
    [ '11', '2052779', 'λ2048', 'T2^20' ],
    [ '11', '2206488', 'λ2048', 'T2^21' ],
    [ '11', '2360597', 'λ2048', 'T2^22' ],
    [ '11', '2513923', 'λ2048', 'T2^23' ],
    [ '11', '2674179', 'λ2048', 'T2^24' ],
    [ '11', '2828269', 'λ2048', 'T2^25' ],
    [ '12', '2654059', 'λ2048', 'T2^20' ],
    [ '12', '2807365', 'λ2048', 'T2^21' ],
    [ '12', '2960568', 'λ2048', 'T2^22' ],
    [ '12', '3111978', 'λ2048', 'T2^23' ],
    [ '12', '3272037', 'λ2048', 'T2^24' ],
    [ '12', '3424821', 'λ2048', 'T2^25' ],
    [ '13', '4127483', 'λ2048', 'T2^20' ],
    [ '13', '4280159', 'λ2048', 'T2^21' ],
    [ '13', '4432185', 'λ2048', 'T2^22' ],
    [ '13', '4582307', 'λ2048', 'T2^23' ],
    [ '13', '4741586', 'λ2048', 'T2^24' ],
    [ '13', '4894320', 'λ2048', 'T2^25' ],
    [ '14', '7729319', 'λ2048', 'T2^20' ],
    [ '14', '7881334', 'λ2048', 'T2^21' ],
    [ '14', '8032176', 'λ2048', 'T2^22' ],
    [ '14', '8181920', 'λ2048', 'T2^23' ],
    [ '14', '8340937', 'λ2048', 'T2^24' ],
    [ '14', '8492728', 'λ2048', 'T2^25' ]
]
ts = ["20", "21", "22", "23", "24", "25"]
colors = ["tab:red", "tab:green", "tab:blue", "tab:orange", "tab:purple", "tab:brown"]
 # circle, triangle, square
markers = ['o', '^', 's', 'D', 'P', 'X'] 
x = [[],[],[],[],[],[]]
y = [[],[],[],[],[],[]]
for i in range(len(data)):
    x[i%6].append(int(data[i][0]))
    y[i%6].append(int(data[i][1]))
for i in range(6):
    plt.plot(x[i], y[i], color=colors[i], label="$"+ts[i]+"$", marker=markers[i])
plt.axvline(x=9.00000001, color='black')
plt.text(10, 9180000, 'Minimum', ha='right', fontsize=13)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title=r'$\tau$', fontsize=13, title_fontsize=13)
plt.xlabel('Number of Skipped Proof', labelpad= 10.9,fontsize=15 ) 
plt.ylabel('Gas Used ($10^6$)', labelpad= 18, fontsize=15)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
# Adjust the bottom margin
#plt.subplots_adjust(top=0.55)
plt.subplots_adjust(bottom=0.1)
plt.grid(True, linestyle="--")
plt.tight_layout()
plt.savefig('delta-2048.png', dpi=500)
plt.show()