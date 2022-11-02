info2 = {
    'first_name': 'Martha',
    'last_name': 'Smith',
    'phone': '05423423423',
    'address': 'Ramat Gan'
}

# Removing key+value (without returning)
del info2['address']
print(info2)

# Removing from dictionary and storing the value
name = info2.pop('first_name')
print(name)


keys = list(info2.keys())
print(keys)
