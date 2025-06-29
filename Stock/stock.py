def main():
    from os import read, write, _exit
    from heapq import heappush, heappop

    stock_data = {}
    sell_order = {}
    buy_order = {}
    
    data = []
    output = []
    dtappend = data.append
    print = output.append
    while x:=read(0, 16777216): dtappend(x)
    tokens = iter(b''.join(data).split())

    for op in tokens:
        if op==b"register_stock":
            sid = int(next(tokens))
            stock_data[sid] = 0
            sell_order[sid] = []
            buy_order[sid] = []
        elif op==b"place_sell_order":
            sid, qt, mn = int(next(tokens)), int(next(tokens)), int(next(tokens))
            while buy_order[sid] and -buy_order[sid][0][0] >= mn:
                price, oq = buy_order[sid][0]
                stock_data[sid] = -price
                if qt<oq: buy_order[sid][0] = (price, oq-qt)
                else: heappop(buy_order[sid])
                qt -= oq
                if qt<=0: break
            else: heappush(sell_order[sid], (mn, qt))
        elif op==b"place_buy_order":
            sid, qt, mx = int(next(tokens)), int(next(tokens)), int(next(tokens))
            while sell_order[sid] and sell_order[sid][0][0] <= mx:
                price, oq = sell_order[sid][0]
                stock_data[sid] = price
                if qt<oq: sell_order[sid][0] = (price, oq-qt)
                else: heappop(sell_order[sid])
                qt -= oq
                if qt<=0: break
            else: heappush(buy_order[sid], (-mx, qt))
        elif op==b"print_all_stocks":
            print(str(sorted(stock_data.items(), key=lambda x:(-x[1],x[0]))).encode())
    
    write(1, b'\n'.join(output))
    _exit(0)
main()
