def get_fixed_price(price):
    global discount_rate
    result = price * (100/(100 - discount_rate))
    return result

discount_rate = int(input('할인율은? '))
A_price = int(input('A 상품의 할인된 가격은? '))
B_price = int(input('B 상품의 할인된 가격은? '))

A_result = get_fixed_price(A_price)
B_result = get_fixed_price(B_price)
print('A 상품의 정가는',A_result,'원')
print('B 상품의 정가는',B_result,'원')
