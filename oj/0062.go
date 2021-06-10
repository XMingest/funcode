/*
题目描述
把自然数顺序地写下来得到一个数列123456789101112131415161718192021…，请问这个数列中的第N个数字是什么
输入
N[1,1e8]
输出
输出数列中的第N个数字
*/
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var (
		c, d, i, n, t int
	)
	fmt.Scanln(&n)
	c = 8
	d = 10
	for i = 1; n*9 > c*d+1; i++ {
		c += 9
		d *= 10
	}
	c -= 9
	d /= 10
	t = n - (c*d+1)/9 - 1
	fmt.Printf("%c\n", strconv.Itoa(t/i + d)[t%i])
}
