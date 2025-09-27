empty_d = dict()
print(type(empty_d))

d = {
    'k': 'v',
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3'
    }

print(d['k1'])
print(d.get('k1'))
print(d)

d['k4'] = 'v4'
print(d)

del d['k4']
print(d.get('k4'))