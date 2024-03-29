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

dataOneN = [
  [ 3788252, 'λ2048', 'T2^20' ],
  [ 3789054, 'λ2048', 'T2^20' ],
  [ 3787319, 'λ2048', 'T2^20' ],
  [ 3780632, 'λ2048', 'T2^20' ],
  [ 3784345, 'λ2048', 'T2^20' ],
  [ 3787801, 'λ2048', 'T2^20' ],
  [ 3782021, 'λ2048', 'T2^20' ],
  [ 3787490, 'λ2048', 'T2^20' ],
  [ 3788698, 'λ2048', 'T2^20' ],
  [ 3801350, 'λ2048', 'T2^20' ],
  [ 3986631, 'λ2048', 'T2^21' ],
  [ 3990170, 'λ2048', 'T2^21' ],
  [ 4006341, 'λ2048', 'T2^21' ],
  [ 3991224, 'λ2048', 'T2^21' ],
  [ 3998147, 'λ2048', 'T2^21' ],
  [ 3990975, 'λ2048', 'T2^21' ],
  [ 3998807, 'λ2048', 'T2^21' ],
  [ 3981315, 'λ2048', 'T2^21' ],
  [ 3993595, 'λ2048', 'T2^21' ],
  [ 3976968, 'λ2048', 'T2^21' ],
  [ 4189498, 'λ2048', 'T2^22' ],
  [ 4182714, 'λ2048', 'T2^22' ],
  [ 4199992, 'λ2048', 'T2^22' ],
  [ 4192202, 'λ2048', 'T2^22' ],
  [ 4189041, 'λ2048', 'T2^22' ],
  [ 4193200, 'λ2048', 'T2^22' ],
  [ 4191750, 'λ2048', 'T2^22' ],
  [ 4189759, 'λ2048', 'T2^22' ],
  [ 4191299, 'λ2048', 'T2^22' ],
  [ 4184532, 'λ2048', 'T2^22' ],
  [ 4398999, 'λ2048', 'T2^23' ],
  [ 4399595, 'λ2048', 'T2^23' ],
  [ 4384392, 'λ2048', 'T2^23' ],
  [ 4393079, 'λ2048', 'T2^23' ],
  [ 4391225, 'λ2048', 'T2^23' ],
  [ 4400912, 'λ2048', 'T2^23' ],
  [ 4391690, 'λ2048', 'T2^23' ],
  [ 4404701, 'λ2048', 'T2^23' ],
  [ 4393701, 'λ2048', 'T2^23' ],
  [ 4388301, 'λ2048', 'T2^23' ],
  [ 4584429, 'λ2048', 'T2^24' ],
  [ 4586027, 'λ2048', 'T2^24' ],
  [ 4598287, 'λ2048', 'T2^24' ],
  [ 4606285, 'λ2048', 'T2^24' ],
  [ 4610835, 'λ2048', 'T2^24' ],
  [ 4580867, 'λ2048', 'T2^24' ],
  [ 4593114, 'λ2048', 'T2^24' ],
  [ 4592281, 'λ2048', 'T2^24' ],
  [ 4598470, 'λ2048', 'T2^24' ],
  [ 4603166, 'λ2048', 'T2^24' ],
  [ 4809455, 'λ2048', 'T2^25' ],
  [ 4797312, 'λ2048', 'T2^25' ],
  [ 4800873, 'λ2048', 'T2^25' ],
  [ 4803371, 'λ2048', 'T2^25' ],
  [ 4802379, 'λ2048', 'T2^25' ],
  [ 4803652, 'λ2048', 'T2^25' ],
  [ 4794267, 'λ2048', 'T2^25' ],
  [ 4787658, 'λ2048', 'T2^25' ],
  [ 4795554, 'λ2048', 'T2^25' ],
  [ 4815858, 'λ2048', 'T2^25' ]
]
dataNInProof = [
  [ 3916498, 'λ2048', 'T2^20' ],
  [ 3918273, 'λ2048', 'T2^20' ],
  [ 3916057, 'λ2048', 'T2^20' ],
  [ 3909825, 'λ2048', 'T2^20' ],
  [ 3913096, 'λ2048', 'T2^20' ],
  [ 3917049, 'λ2048', 'T2^20' ],
  [ 3911229, 'λ2048', 'T2^20' ],
  [ 3916670, 'λ2048', 'T2^20' ],
  [ 3918127, 'λ2048', 'T2^20' ],
  [ 3930634, 'λ2048', 'T2^20' ],
  [ 4122869, 'λ2048', 'T2^21' ],
  [ 4126424, 'λ2048', 'T2^21' ],
  [ 4141652, 'λ2048', 'T2^21' ],
  [ 4127237, 'λ2048', 'T2^21' ],
  [ 4133901, 'λ2048', 'T2^21' ],
  [ 4126731, 'λ2048', 'T2^21' ],
  [ 4135069, 'λ2048', 'T2^21' ],
  [ 4117783, 'λ2048', 'T2^21' ],
  [ 4129601, 'λ2048', 'T2^21' ],
  [ 4112710, 'λ2048', 'T2^21' ],
  [ 4332564, 'λ2048', 'T2^22' ],
  [ 4326287, 'λ2048', 'T2^22' ],
  [ 4342861, 'λ2048', 'T2^22' ],
  [ 4335550, 'λ2048', 'T2^22' ],
  [ 4332093, 'λ2048', 'T2^22' ],
  [ 4336300, 'λ2048', 'T2^22' ],
  [ 4334280, 'λ2048', 'T2^22' ],
  [ 4332891, 'λ2048', 'T2^22' ],
  [ 4334395, 'λ2048', 'T2^22' ],
  [ 4328095, 'λ2048', 'T2^22' ],
  [ 4548546, 'λ2048', 'T2^23' ],
  [ 4549128, 'λ2048', 'T2^23' ],
  [ 4534681, 'λ2048', 'T2^23' ],
  [ 4543424, 'λ2048', 'T2^23' ],
  [ 4541544, 'λ2048', 'T2^23' ],
  [ 4551257, 'λ2048', 'T2^23' ],
  [ 4542027, 'λ2048', 'T2^23' ],
  [ 4555043, 'λ2048', 'T2^23' ],
  [ 4544018, 'λ2048', 'T2^23' ],
  [ 4538634, 'λ2048', 'T2^23' ],
  [ 4742327, 'λ2048', 'T2^24' ],
  [ 4743666, 'λ2048', 'T2^24' ],
  [ 4756232, 'λ2048', 'T2^24' ],
  [ 4763406, 'λ2048', 'T2^24' ],
  [ 4768267, 'λ2048', 'T2^24' ],
  [ 4738784, 'λ2048', 'T2^24' ],
  [ 4751040, 'λ2048', 'T2^24' ],
  [ 4749603, 'λ2048', 'T2^24' ],
  [ 4756139, 'λ2048', 'T2^24' ],
  [ 4760277, 'λ2048', 'T2^24' ],
  [ 4973745, 'λ2048', 'T2^25' ],
  [ 4961864, 'λ2048', 'T2^25' ],
  [ 4966084, 'λ2048', 'T2^25' ],
  [ 4968312, 'λ2048', 'T2^25' ],
  [ 4967562, 'λ2048', 'T2^25' ],
  [ 4968289, 'λ2048', 'T2^25' ],
  [ 4959471, 'λ2048', 'T2^25' ],
  [ 4952824, 'λ2048', 'T2^25' ],
  [ 4960176, 'λ2048', 'T2^25' ],
  [ 4980528, 'λ2048', 'T2^25' ]
]

BitSize = [2048]
colors = ['#ff0000', '#0000ff']
markers = ['o', 's']  # circle, triangle, square
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
lineStyles = ['-', '--']

x = []
y = []

for i in range(0, len(dataOneN), 10):
    y_sum = 0
    print(i)
    for j in range(0,10):
        y_sum += dataNInProof[i+j][0] - dataOneN[i+j][0]
    x.append(ts[i//10])
    y.append(y_sum/10)

plt.plot(x, y, color=colors[0], marker=markers[0], linestyle=lineStyles[0])

plt.xlabel('T', labelpad= 15, fontsize=13)
plt.ylabel('Gas Difference', labelpad= 15, fontsize=13)
plt.legend(fontsize=12)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
# Adjust the bottom margin
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(bottom=0.2)
plt.show()