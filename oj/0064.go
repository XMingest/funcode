/*
#题目描述
Lucky Number也就是幸运数，我们这么定义幸运数：若k能被x、y、z任意一个数整除就可认为k是幸运数。现在你的任务是计算区间[1,n]之间一共有多少个幸运数
#输入
包含四个整数n,x,y,z(1<N <= 10^9,1< x,y,z<100)。
#输出
幸运数的个数。
*/
package main

import "fmt"

func lcm(a int, b int) int {
	if a < b {
		return lcm(b, a)
	}
	for i := 2; i*i <= b; i++ {
		if b%i == 0 {
			if (a*i)%b == 0 {
				return a * i
			}
			if (a*b/i)%b == 0 {
				return a * b / i
			}
		}
	}
	return a * b
}

func main() {
	var (
		n, x, y, z, xy, xz, yz, xyz int
	)

	fmt.Scanln(&n, &x, &y, &z)
	xy = lcm(x, y)
	xz = lcm(x, z)
	yz = lcm(y, z)
	xyz = lcm(xy, z)
	fmt.Printf("%d\n", n/x+n/y+n/z-n/xy-n/xz-n/yz+n/xyz)
}
