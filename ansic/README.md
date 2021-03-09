# 命名

类型 | 命名风格
:- | :-
函数<br>结构<br>枚举<br>联合<br>typedef定义 | 帕斯卡[^1]
局部变量<br>函数参数<br>宏参数<br>结构字段<br>联合体成员 | 驼峰[^2]
全局变量 | `g_`前缀驼峰[^3]
宏<br>常量<br>枚举值<br>`goto`标签 | 大写下划线[^4]

[^1]: PascalCase
[^2]: camelCase
[^3]: g_camelCase
[^4]: UNIX_LIKE

# 格式

```c
// 单行注释
/*
 * 多行
 * 注释
 */

// 注释只能在上右两处
int max(int a, int b) // Allman风格，左括号另起并独占一行
{
    return b ? a < b : a; // 右注释至少留1空格，三目运算`?``:`左右空格
} // 右括号独占一行，除非`do ... while`语句、逗号、分号

int foo(void)
{
    const int STEP = 100;         // 可保持左侧对齐
    const float PI = 3.141592654; // 同类注释

    // 行字符不超过120，假设此处需要换行，则尽量使操作符居行末
    if (windowsType & FRAME ||
        windowsType & WIDGET)
    {
        // 如存在关联，换行时应考虑可读性
        int result = ResizeWindow(left.x, left.y
                                right.x, right.y); // 参数与参数缩进一致
    } // `if`、`while`、`for`等只包含单条语句，也应使用`{}`

    switch (op) // `switch` `if` `while` `for`等与括号间添加空格
    {
        case '+':
            break; // switch不使用大括号形式
        default:
            int *p1; // `*`等一元操作符左空格右无空格
            break;
    }
}

/*
 * 头文件都应使用define保护，而非`#pragma once`
 * 保护符使用唯一，比如项目名称相对路径及文件名
 */
#ifndef FUN_XMINGEST_UTILS_TIMER_H
#define FUN_XMINGEST_UTILS_TIMER_H
#endif
```

## 空白

- `,` `;` `:`左无空格右加，除结构体中表示位域的`:`以外
- `if` `switch` `case` `do` `while` `for`等关键字之后加空格
- 避免连续空行，文件末应有空行
- 二元操作符与三目操作符左右加空格，除成员操作符`.` `->`以外
- 数组中括号无需空格，但初始化的大括号内部应有空格，如`int arr[] = { 10, 20 };`
- 行末无空格
- 一元操作符左侧空格右侧无空格

## 引用

顺序为
1. C标准库
1. 操作系统库
1. 平台库
1. 项目公共库
1. 自己或其他依赖

```c
#include <stdlib.h> // C 标准库
#include <string.h>

#include <linux/list.h> // 操作系统库
#include <linux/time.h>

#include "platform/base.h" // 平台库
#include "platform/struct.h"

#include "project/public/log.h" // 项目公共库

#include "bar.h" // foo.c 的依赖 bar.h

#include "foo.h" // foo.c 对应头文件放最后一个
```
