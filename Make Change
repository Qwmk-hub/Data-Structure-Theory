def calculate(charged,given):
    coins = [500,100,50,10]

    if given < charged:
        print(-1)
        return
    
    change = given- charged
    result=[]

    for coin in coins:
        count=change//coin
        result.append(count)
        change %=coin

    if change != 0:
        print(-1)
    else:
        print(1, *result)

charged, given=map(int, input().split())
calculate(charged, given)
