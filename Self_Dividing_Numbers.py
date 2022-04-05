def SDN(n):
    x = n
    count = 0
    loop_count = 0 
    while x > 0:
        p = x % 10
        if p == 0 or n % p > 0:
            #print("no")
            return False
        else:
            #print ("yes")
            count = count + 1
        loop_count = loop_count + 1
        x = x // 10
    if loop_count == count :
        return True
def SDN_upto(lower_limit,upper_limit):
    for i in range(lower_limit,upper_limit+1):
        if SDN(i):
            print(i,end = " ")
n = int(input())
m = int(input())
SDN_upto(n,m)