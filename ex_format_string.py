"""
3 Ways to format a string
"""
drink_menu = {
    'Coffee Latte': 850,
    'Green Tea': 650,
    'Ice cafe au lait': 1050,
    'Caramel Machhiato': 1250
}

for key, value in drink_menu.items():
    print(key, ': $', value)
print('='*30)

# (1) %operator
for key, value in drink_menu.items():
    print('%20s: $%5.0f' % (key, value))

# (2) str.format
for key, value in drink_menu.items():
    print('{0:<20s}: ${1:>5,.0f}'.format(key, value))
print('='*30)

# (3) f-string (Python 3.6+)
#for key, value in drink_menu.items():
#    print(f'{key:<20s}: ${value:>5,.0f}')
#print('='*30)

# what's this?
#for key, value in drink_menu.items():
#    print(f'{key:<20s}, {value:>05d})
