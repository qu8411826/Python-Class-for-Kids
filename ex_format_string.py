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
