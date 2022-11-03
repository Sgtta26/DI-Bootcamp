def bank_account(holder, balance=0.0):
    # holder = 'Batya'
    # 4.5
    print(f"Holder: {holder}. BALANCE: {balance}")
    # Holder: Batya. BALANCE: 4.5

def multiple_accounts(holders: list, balance = 0.0):

    # holders = ['Bill','David','Batya']
    # balance = 4.5 (default 0.0)
    for holder in holders:
        # holder = 'Batya'
        bank_account(holder, balance)


names = ['Bill','David','Batya']

multiple_accounts(names, 4.5)