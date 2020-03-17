import numpy as np
import sortedcontainers as st

ss = st.SortedSet([1,2,2,2,2,3,4,5])
check = ss.__contains__(6)	# 6 in ss
size = len(ss)

print(ss,type(ss))

print(type(ss[0:3]))

ss.add(8)
ss.add(9)
ss.discard(1)
ss.discard(10)

del ss[-1]

print(size)
print(check) 

print("pop:",ss.pop(-1))

ss.remove(2)
ss.add(2)
ss.add(2)
print(ss)
print("count",ss.count(2))

ss.clear()
print(ss)


a = st.SortedSet([1,2])
b = st.SortedSet([3,4])

c = a[0:]


print(c)

for elem in c:
	print(elem, type(elem))
