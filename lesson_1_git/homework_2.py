a = int(input())
print(a%10*10000+a%100//10*1000+a%1000//100*100+a%10000//1000*10+a//10000)