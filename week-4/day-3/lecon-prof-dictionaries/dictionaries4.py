info1 = {
    'first_name': 'Yossi',
    'last_name': 'Eik',
    'phone': '052855823243',
}
info2 = {
    'first_name': 'Martha',
    'last_name': 'Smith',
    'phone': '05423423423',
    'address': 'Ramat Gan'
}
phone_book = [info1, info2]

for info in phone_book:
    if info['first_name'] == 'Yossi':
        print(info['phone'])