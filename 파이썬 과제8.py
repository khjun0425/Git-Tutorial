def buy(dic):
  while True:
    print('[구입]')
    item = input("상품명? ")
    if item == '':
      return False
    amount = int(input('수량은? '))
    dic[item] = amount
    print(f"장바구니에 {item} {amount}개가 담겼습니다.",end='\n\n')

def show(dic):
  print('')
  print(f'>>> 장바구니 보기: {dic}',end='\n\n')

def find(dic):
  print('[검색]')
  key = input('장바구니에서 확인하고자 하는 상품은? ')

  if key in dic:
    print(f'{key}은(는) {dic[key]}개 담겨 있습니다.')
  else:
    print(f'{key}은(는) 장바구니에 없습니다.')

#주 프로그램 부
shopping_bag = {}
while True:
  if buy(shopping_bag) == False:
    break
show(shopping_bag)
find(shopping_bag)
