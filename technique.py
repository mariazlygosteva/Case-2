# Part of case-study #2: Technique
# Developers: Saipulaev А., Zlygosteva M.
#

import ru_local as ru

def main():
    '''
    Main function.
    :return: None
    '''

purchase = input(ru.COUNT_SMARTPHONES_AND_HEADPHONES)
num_smartphones, num_headphones = map(int, purchase.split())
total_price = 0
discount = 0
smartphone_price = 25000
headphones_price = 4500
bonuses = 0.05

# 1
smartphones_cost = num_smartphones * smartphone_price
headphones_cost = num_headphones * headphones_price
total_price_without_discount = smartphones_cost + headphones_cost

# 2
discount_headphones = int(num_headphones * headphones_price * 0.2)

# 3
if smartphones_cost >= 25000:
    discount = int(headphones_price * 0.2) * num_headphones
    total_price = total_price_without_discount - discount
else:
    total_price = total_price_without_discount

# 4
bonus_points = int(total_price * bonuses)

# 5
bonuses_residual = smartphone_price * 3 * bonuses
price = int(total_price - bonuses_residual)

# 6
bonuses50 = int(total_price / 2)

print(f'{ru.HEADPHONE_DISCOUNT} - {discount_headphones}')
print(f'{ru.COST_OF_SMARTPHONES_AND_HEADPHONES_WITHOUT_DISCOUNT} - '
      f'{total_price_without_discount}')
print(f'{ru.DISCOUNTED_PRICE_OF_SMARTPHONES_AND_HEADPHONES} - {total_price}')
print(f'{ru.BONUSES} - {bonus_points}')
print(f'{ru.BONUSES_RESIDUAL} - {price}')
print(f'{ru.FIFTY_PERCENT_DISCOUNT} - {bonuses50}')

if name == 'main':
    main()
