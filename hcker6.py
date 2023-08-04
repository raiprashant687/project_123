# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
s1 = input()
m = tuple()
count = 0

for i in range(len(s)):

    result = re.search(s1, s[i:i + len(s1)])
    if result is not None:
        m = (i, i + len(s1) - 1)
        count += 1
        print(m)
    else:
        pass
if count == 0:
    print('(-1,-1)')
print(count)

