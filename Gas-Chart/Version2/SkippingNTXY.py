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
  [ 1948075, 'λ1024', 'T2^20' ],
  [ 2055287, 'λ1024', 'T2^21' ],
  [ 2159308, 'λ1024', 'T2^22' ],
  [ 2266357, 'λ1024', 'T2^23' ],
  [ 2363314, 'λ1024', 'T2^24' ],
  [ 2480958, 'λ1024', 'T2^25' ],
  [ 3921992, 'λ2048', 'T2^20' ],
  [ 4128691, 'λ2048', 'T2^21' ],
  [ 4338719, 'λ2048', 'T2^22' ],
  [ 4555330, 'λ2048', 'T2^23' ],
  [ 4749156, 'λ2048', 'T2^24' ],
  [ 4980923, 'λ2048', 'T2^25' ],
  [ 6882805, 'λ3072', 'T2^20' ],
  [ 7235788, 'λ3072', 'T2^21' ],
  [ 7603641, 'λ3072', 'T2^22' ],
  [ 7964096, 'λ3072', 'T2^23' ],
  [ 8334172, 'λ3072', 'T2^24' ],
  [ 8729305, 'λ3072', 'T2^25' ]
]
SkippingNTXY = [
  [ 1641074, 'λ1024', 'T2^20' ],
  [ 1732143, 'λ1024', 'T2^21' ],
  [ 1819849, 'λ1024', 'T2^22' ],
  [ 1910526, 'λ1024', 'T2^23' ],
  [ 1990607, 'λ1024', 'T2^24' ],
  [ 2091942, 'λ1024', 'T2^25' ],
  [ 3443416, 'λ2048', 'T2^20' ],
  [ 3623386, 'λ2048', 'T2^21' ],
  [ 3807821, 'λ2048', 'T2^22' ],
  [ 3998967, 'λ2048', 'T2^23' ],
  [ 4165695, 'λ2048', 'T2^24' ],
  [ 4371667, 'λ2048', 'T2^25' ],
  [ 6224820, 'λ3072', 'T2^20' ],
  [ 6541315, 'λ3072', 'T2^21' ],
  [ 6873002, 'λ3072', 'T2^22' ],
  [ 7197192, 'λ3072', 'T2^23' ],
  [ 7530564, 'λ3072', 'T2^24' ],
  [ 7889786, 'λ3072', 'T2^25' ]
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
        ySkippingTXY[i//6].append(SkippingNTXY[i+j][0])

for i in range(0,3):
    plt.plot(xNTXYVInProof[i], yNTXYVInProof[i], color=colors[i], marker=markers[i], label=str(BitSize[i])+" λ")
    plt.plot(xSkippingTXY[i], ySkippingTXY[i], color=colors[i], marker=markers[i], linestyle='--', label=str(BitSize[i])+" λ, Skipped deterministic elements")

plt.xlabel('T', labelpad= 15, fontsize = 13)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize = 13)

custom_lines = [Line2D([0], [0], color='red', lw=2),
                Line2D([0], [0], color='green', lw=2),
                Line2D([0], [0], color='blue', lw=2),
                Line2D([0], [0], color='black', linestyle='--', lw=2)]

plt.legend(custom_lines, ['λ = 1024', 'λ = 2048', 'λ = 3072', 'Shortening Proof Size'], fontsize=12)
#plt.legend(bbox_to_anchor=(1.05, 0), loc='lower left', borderaxespad=0., fontsize = 13)

# custom_lines = [Line2D([0], [0], color=colors[i], lw=2) for i in range(3)] + [Line2D([0], [0], color='black', linestyle=lineStyles[i], lw=2) for i in range(2)]
# plt.legend(custom_lines, [str(BitSize[i]) + ' Bits' for i in range(3)] + ['One N', 'N in Proof'])

plt.gca().yaxis.get_offset_text().set_visible(False)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.subplots_adjust(left=0.15, bottom=0.2) #, right=0.65)  # Adjust the right space as needed)

plt.show()