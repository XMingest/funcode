#Problems involving the computation of exact values of very large magnitude and precision are common
#For example, the computation of the national debt is a taxing experience for many computer systems
#This problem requires that you write a program to compute the exact value of Rn
#  where R is a real number ( 0.0 < R < 99.999 ) and n is an integer such that 0 < n ≤ 25
def func():
    while True:
        s = ''
        try:
            s = input().strip()
        except:
            s = ''
        if s:
            doti = s[0:6].index('.')
            r = int(s[0: doti] + s[doti + 1: 6])
            if r == 0:
                print(0)
                continue
            n = int(s[6:])
            doti = 5 - doti
            while r % 10 == 0:
                r //= 10
                doti -= 1
            doti *= n
            result = str(r ** n)
            if doti > len(result):
                print('.' + '0' * (doti - len(result)) + result)
            else:
                print(result[:-doti] + '.' + result[-doti:])
        else:
            break
    return

if __name__ == "__main__":
    func()
