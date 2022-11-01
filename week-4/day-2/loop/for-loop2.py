letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

countries = ['Brazil','Germany','UK','US','Somalia','Brazil','Brazil','US','US','US','US','Brazil','Germany','Germany','Germany']

uniques = set()
duplicated = set()
duplicated_idx = []

for idx, value in enumerate(countries):
    if value in uniques:
        duplicated.add(value)
        duplicated_idx.append(idx)
    else:
        uniques.add(value)

print(uniques)
print(duplicated)

print(uniques.difference(duplicated))

