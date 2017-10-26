def gcd(num1,num2):
    remainder = 1
    divisor = min(num1, num2)
    divident = max(num1, num2)
    while remainder != 0:
        remainder = divident % divisor
        if remainder == 0:
            break
        divident = divisor
        divisor = remainder
    return divisor

tc = input()
while tc > 0:
    arr_len = input()
    arr = map(int, raw_input().strip().split(' '))
    if arr_len >= 2:
        gcd_ = gcd(arr[0],arr[1])
    else:
        gcd_ = arr[0]
    if 1 in arr:
        print "YES"
    else:
        for x in range(2, arr_len):
            if gcd_ == 1:
                break
            gcd_ = gcd(gcd_,arr[x])
        if gcd_ != 1:
            print "NO"
        else:
            print "YES"
    tc -= 1