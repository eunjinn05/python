#딕셔너리
cabinet = {3:'A', 6:'B'}
print(cabinet[3])
print(cabinet.get(3))
print(cabinet.get(7, 'no use'))

print(3 in cabinet)

cabinet[7] = 'C'
print(cabinet)

del cabinet[6]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())