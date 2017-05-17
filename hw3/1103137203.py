
def main():
    print("使用方法: 回收期<pp>或折現後回收期<dpp> [<資金成本(折現率)>] <各期金額>")
    print("折現後回收期例: dpp 0.08 -30000000 6500000 6500000 6500000 6500000 6500000 6500000")
    print("回收期例: pp -30000000 6500000 6500000 6500000 6500000 6500000 6500000")
    arg = input().strip().split()
    if len(arg) < 2: # 1
        print("使用方法: 回收期<pp>或折現後回收期<dpp> [<資金成本(折現率)>] <各期金額>")
        print("折現後回收期例: dpp 0.08 -30000000 6500000 6500000 6500000 6500000 6500000 6500000")
        print("回收期例: pp -30000000 6500000 6500000 6500000 6500000 6500000 6500000")

    if "pp" == arg[0]:
        argLength = len(arg)
        n = 0
        first = float(arg[1])
        print("年度:",0,"累積現金流量:",first)
        for i in range(2,argLength):
            first = first + float(arg[i])
            print("年度:",i-1,"累積現金流量:",first)
            if(0 >= first):
                n = 1 + n
            else:
                profit = first - float(arg[i])
        devi = abs(profit) / float(arg[i])
        pp = n + devi
        print("回收期:",pp,"年")
    
    if "dpp" == arg[0]:
        argLength = len(arg)
        n = 0
        k = float(arg[1])
        first = float(arg[2])
        print("年度:",0,"折現因子(折現率=", k,"):", 1,"     現金流量折現值:",round(first)," 累積現金流量:",first)
        for i in range(3,argLength):
            rate = 1 / (k + 1)**(i-2)
            first = first + (float(arg[i]) * rate)
            print("年度:",i-2,"折現因子(折現率=", k,"):", round(rate,4),"現金流量折現值:",round(float(arg[i]) * rate,2),"累積現金流量:",round(first,2))
            if(0 >= first):
                n = 1 + n
            else:
                profit = first - (float(arg[i]) * rate)
        devi = abs(profit) / (float(arg[i]) * rate)
        dpp = n + devi
        print("回收期:",dpp,"年")
    
main()