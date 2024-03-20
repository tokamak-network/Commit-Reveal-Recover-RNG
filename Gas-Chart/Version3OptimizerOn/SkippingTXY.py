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
from matplotlib.lines import Line2D
NTXYVInProof = [
[ 1891828, 'λ1024', 'T2^20' ],
[ 1993090, 'λ1024', 'T2^21' ],
[ 2096346, 'λ1024', 'T2^22' ],
[ 2198301, 'λ1024', 'T2^23' ],
[ 2295138, 'λ1024', 'T2^24' ],
[ 2407067, 'λ1024', 'T2^25' ],
[ 3854404, 'λ2048', 'T2^20' ],
[ 4060607, 'λ2048', 'T2^21' ],
[ 4264504, 'λ2048', 'T2^22' ],
[ 4480256, 'λ2048', 'T2^23' ],
[ 4672532, 'λ2048', 'T2^24' ],
[ 4897782, 'λ2048', 'T2^25' ],
[ 6803677, 'λ3072', 'T2^20' ],
[ 7155541, 'λ3072', 'T2^21' ],
[ 7522241, 'λ3072', 'T2^22' ],
[ 7875852, 'λ3072', 'T2^23' ],
[ 8241395, 'λ3072', 'T2^24' ],
[ 8630845, 'λ3072', 'T2^25' ]
]
SkippingTXY= [
[ 1703075, 'λ1024', 'T2^20' ],
[ 1794407, 'λ1024', 'T2^21' ],
[ 1887612, 'λ1024', 'T2^22' ],
[ 1979175, 'λ1024', 'T2^23' ],
[ 2065978, 'λ1024', 'T2^24' ],
[ 2167695, 'λ1024', 'T2^25' ],
[ 3551294, 'λ2048', 'T2^20' ],
[ 3741107, 'λ2048', 'T2^21' ],
[ 3928636, 'λ2048', 'T2^22' ],
[ 4127613, 'λ2048', 'T2^23' ],
[ 4303679, 'λ2048', 'T2^24' ],
[ 4511895, 'λ2048', 'T2^25' ],
[ 6381721, 'λ3072', 'T2^20' ],
[ 6710482, 'λ3072', 'T2^21' ],
[ 7054129, 'λ3072', 'T2^22' ],
[ 7384081, 'λ3072', 'T2^23' ],
[ 7726266, 'λ3072', 'T2^24' ],
[ 8091868, 'λ3072', 'T2^25' ]
]

BitSize = [1024, 2048, 3072]
colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
lineStyles = ['-', '--']

xNTXYVInProof = [[],[],[]]
yNTXYVInProof = [[],[],[]]
xSkippingTXY = [[],[],[]]
ySkippingTXY = [[],[],[]]

for i in range(0,len(NTXYVInProof),6):
    for j in range(0,6):
        xNTXYVInProof[i//6].append(ts[j])
        yNTXYVInProof[i//6].append(NTXYVInProof[i+j][0])
        xSkippingTXY[i//6].append(ts[j])
        ySkippingTXY[i//6].append(SkippingTXY[i+j][0])

for i in range(0,3):
    plt.plot(xNTXYVInProof[i], yNTXYVInProof[i], color=colors[i], marker=markers[i], label=str(BitSize[i])+" λ")
    plt.plot(xSkippingTXY[i], ySkippingTXY[i], color=colors[i], marker=markers[i], linestyle='--', label=str(BitSize[i])+" λ, Skipped deterministic elements")

plt.xlabel('T', labelpad= 15, fontsize = 13)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize = 13)

custom_lines = [Line2D([0], [0], color='red', marker='o', lw=1.5),
                Line2D([0], [0], color='green', marker='^', lw=1.5),
                Line2D([0], [0], color='blue', marker='s', lw=1.5),
                Line2D([0], [0], color='black', linestyle='--', lw=1)]

plt.legend(custom_lines, ['λ = 1024', 'λ = 2048', 'λ = 3072', 'Skipped Deterministic Elements'], prop={'size': 9.5}, bbox_to_anchor=(0.43, 0.7596))
#plt.legend(bbox_to_anchor=(1.05, 0), loc='lower left', borderaxespad=0., fontsize = 13)

# custom_lines = [Line2D([0], [0], color=colors[i], lw=2) for i in range(3)] + [Line2D([0], [0], color='black', linestyle=lineStyles[i], lw=2) for i in range(2)]
# plt.legend(custom_lines, [str(BitSize[i]) + ' Bits' for i in range(3)] + ['One N', 'N in Proof'])

plt.gca().yaxis.get_offset_text().set_visible(False)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.subplots_adjust(left=0.15, bottom=0.2) #, right=0.65)  # Adjust the right space as needed)
plt.grid(True, linestyle="--")
plt.savefig('6.5 T deletion.png', dpi=500)
plt.show()
