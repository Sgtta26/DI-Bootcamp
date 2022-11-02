info = {
    'first_name': 'Yossi',
    'last_name': 'Eik',
    'phone': '052855823243',
}

additional_info = {
    'address': 'Tel Aviv',
    'Country': 'Israel'
}

# Updating one dictionary with another
info.update(additional_info)

print(info)