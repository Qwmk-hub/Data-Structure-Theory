import sys
def main():
    bag=[]
    data=sys.stdin
    for line in data:
        if len(line.split()) == 4:
            operator,cur,pid,expire=line.split()
            bag.append((int(cur)+int(expire),pid))
        elif line.split()[0]=="sell_product":
            cur=int(line.split()[1])
            while bag and bag[-1][0]<=cur:
                bag.pop()
            print(bag.pop()[1] if bag else -1)
        else:
            cur = int(line.split()[1])
            new_bag=[]
            for i in bag:
                if i[0]>cur:
                    new_bag.append(i)
            bag=new_bag
            print(([int(i[1]) for i in bag][::-1]))
main()
