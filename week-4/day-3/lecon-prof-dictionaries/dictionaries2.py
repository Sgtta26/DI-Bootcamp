info = {
    'first_name': 'Yossi',
    'last_name': 'Eik',
    'phone': '052855823243',
}

print("Items:", info.items())

for key, value in info.items():
    if key == 'first_name':
        if value == 'Yossi':
            print("Whatever")
    print(f"{key} : {value}")