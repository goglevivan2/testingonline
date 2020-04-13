import os
import subprocess
#print(os.system('node permutations.js ABCDE EDBCA XYZ ZYX ZXY'))
l = subprocess.check_output('node permutations.js ABCDEFGH 123 321 ')
l=l.decode('utf-8').split()
print('Result',l)