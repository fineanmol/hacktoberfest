## This file will show different ways to print a set.
print("hello wordl")
s=set()
print(type(s))
l=[1,2,3,4,5]
s=set(l)
print(s)
s.add(6)
print(s)
s.union({1,2,3,4,5,6,7,8})
print(s)
s1=s.intersection({1,2,3})
print(s1)
print(s.isdisjoint(s1))
