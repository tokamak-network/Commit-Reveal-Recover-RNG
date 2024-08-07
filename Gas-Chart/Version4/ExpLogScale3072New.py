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

#   Exponentiation by Squaring Square and Multiply Precompile ModExp
#   x^2^2 42984 8561 3844
#   x^2^4 49771 14063 5380
#   x^2^8 63339 25433 8452
#   x^2^16 90677 48004 14596
#   x^2^32 146191 93776 26884
#   x^2^64 260435 187843 51460
#   x^2^128 501998 386069 100612
#   x^2^256 1037650 822925 198925
#   x^2^512 2348889 1858131 395543
#   x^2^1024 5900805 4574606 788784
#   x^2^2048 16722555 12591803 1575266

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import FuncFormatter
#x = ["$x^{2^2}$", "$x^{2^4}$", "$x^{2^8}$", "$x^{2^{16}}$", "$x^{2^{32}}$", "$x^{2^{64}}$", "$x^{2^{128}}$", "$x^{2^{256}}$", "$x^{2^{512}}$", "$x^{2^{1024}}$", "$x^{2^{2048}}$"]
x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

expBySquareIterative = [42984, 49771, 63339, 90677, 146191, 260435, 501998, 1037650, 2348889, 5900805, 16722555]
expBySquareAndMultiply = [8561, 14063, 25433, 48004, 93776, 187843, 386069, 822925, 1858131, 4574606, 12591803]
precompileModExp = [3844, 5380, 8452, 14596, 26884, 51460, 100612, 198925, 395543, 788784, 1575266]


colors = ["tab:red", "tab:green", "tab:blue"]
markers = ['o', '^', 's']  # circle, triangle, square

plt.plot(x, expBySquareIterative, color=colors[0], marker=markers[0], label="Exponentiation by Squaring")
plt.plot(x, expBySquareAndMultiply, color=colors[1], marker=markers[1], label="Square and Multiply")
plt.plot(x, precompileModExp, color=colors[2], marker=markers[2], label="Precompile ModExp")

plt.legend(fontsize=13)
plt.xlabel('Exponentiation ($\\tau$ of $x^{2^{2^\\tau}}$)', fontsize=16)
plt.ylabel('Gas Used ($10^6$)', labelpad= 7, fontsize=15.5)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-6)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
x_numerical = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048])
plt.xticks(fontsize=13, rotation = 45)
plt.yticks(fontsize=13)
# margin
plt.grid(True, linestyle="--")
plt.tight_layout()
# Add text 'x^{2^t}' to the plot
# Adjust 'x_coord' and 'y_coord' to position the text appropriately
# x_coord = len(x) - 0.6  # Position at the end of the x-axis
# y_coord = min(min(expBySquareIterative), min(expBySquareAndMultiply), min(precompileModExp)) * -150  # Adjust this as needed
# plt.text(x_coord, y_coord, r'$x^{2^t}$', fontsize=15, ha='right', va='bottom')
plt.savefig('modexp-3072.png', dpi=500)
plt.show()