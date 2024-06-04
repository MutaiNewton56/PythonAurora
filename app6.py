# Pass by Reference
# Pass by Value
## How variable are stored 
### In Memory

a=[23]
print(f"a=23={a}")
b=a
print(f"b=a={b}")
a.append(49)
z=a
z.append(990)
print(f"a=130={a}")
print(f"b={b}")
print(f"Memory of a={id(a)} ")
print(f"Memory of b={id(b)} ")