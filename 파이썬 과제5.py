#파이썬프로그래밍 6주차 과제
def read_single_digit(a):
  if a== '0':
    print('영', end=' ')
  if a== '1':
    print('일', end=' ')
  if a== '2':
    print('이', end=' ')
  if a== '3':
    print('삼', end=' ')
  if a== '4':
    print('사', end=' ')
  if a== '5':
    print('오', end=' ')
  if a== '6':
    print('육', end=' ')
  if a== '7':
    print('칠', end=' ')
  if a== '8':
    print('팔', end=' ')
  if a== '9':
    print('구', end=' ')

def read_number(a):
  if len(a) == 1:
    read_single_digit(a[0])
  elif len(a) == 2:
    read_single_digit(a[0])
    read_single_digit(a[1])
  else:
    read_single_digit(a[0])
    read_single_digit(a[1])
    read_single_digit(a[2])
a = str(input('세 자리 정수 입력: '))
read_number(a)
