#给定一个正整数，我们可以定义出下面的公式:
#N=a[1]+a[2]+a[3]+…+a[m];
#a[i]>0,1<=m<=N;
#对于一个正整数，求解满足上面公式的所有算式组合，如，对于整数 4 :
#4 = 4;
#4 = 3 + 1;
#4 = 2 + 2;
#4 = 2 + 1 + 1;
#4 = 1 + 1 + 1 + 1;
#所以上面的结果是 5 。
#注意：对于 “4 = 3 + 1” 和 “4 = 1 + 3” ，这两处算式实际上是同一个组合!
def splt_to(n, m, data):
    if m > n:
        return splt_to(n, n, data)
    if not m or not n:
        return 0
    if n == 1 or m == 1:
        return 1
    y = data['step'] * n + m
    if y in data:
        return data[y]
    result = splt_to(n, m - 1, data)
    if n == m:
        result += 1
        data[y] = result
        return result
    if n < m * 2:
        result += splt_to(n - m, n - m - 1, data) + 1
        data[y] = result
        return result
    result += splt_to(n - m, m, data)
    data[y] = result
    return result
    
if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            splt_dict = {'step': n + 1}
            print(splt_to(n, n, splt_dict))
        except:
            break
