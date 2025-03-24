def exchange(coin):
    coin500 = coin // 500
    coin = coin % 500

    coin100 = coin // 100
    coin = coin % 100

    coin50 = coin // 50
    coin = coin % 50

    coin10 = coin // 10
    coin = coin % 10

    print('500원 동전의 개수:',coin500)
    print('100원 동전의 개수:',coin100)
    print('50원 동전의 개수:',coin50)
    print('10원 동전의 개수:',coin10)

def get_integer(prompt):
    res = int(input(prompt))
    return res

coin = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(coin)
