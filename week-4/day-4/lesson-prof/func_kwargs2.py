# MULTIPLE / UNCPECIFIED AMOUNT OF KEY-VALUE ARGUMENTS

def create_dict(**kwargs):
    if 'data' in kwargs:
        return kwargs
    else:
        print("NO DATA INSIDE!")

data = create_dict(name='Yossi', last_name='Eik', city='TLV', data='213')
print(data)


d = {'data': '12321', 'date':'1/1/1991'}
# **d -> 'data' = '12321', 'date' = '1/1/1991'

def scan_data(**info):
    if 'data' in info:
        print("THERE's DATA")
    else:
        print('NO DATA')

scan_data(**d)