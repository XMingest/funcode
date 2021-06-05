# HERE

## computer_on

根据Windows事件日志得到每天电脑第一次活动与最后一次活动的时间，进而推算当日的工作时间

默认每日12:00-13:30，18:00-18:30休息，不计入工作时间

## limit_xlsx_gen

通过特定格式的门限文件（xml）生成相应表格文件

pyinstaller构建

```shell
# requirements.txt - openpyxl pyinstaller
pyinstaller -F -i icon.ico -n 门限表格生成 -w limit_xlsx_gen.py
```

## mandelbrot

Mandelbrot集合，曼德博集合，设

$$
\begin{array}{}
  Z_1 \left( c \right) = c \\
  Z_{n + 1} \left( c \right) = Z^2_n \left( c \right) + c \\
  n \ge 1 \land n \in N
\end{array}
$$

则

$$ M = \left \{ c | c \in C \land \exists a \in R \forall i \left| Z_i \right| \lt a \right \} $$

存在三个定理

1. $$ \left| c \right| \le \frac14 \to c \in M $$
1. $$ \left| c \right| \gt 2 \to c \notin M $$
1. $$ c \in M \to \forall i \left| Z_i \right| \le 2 $$

因此只需要`|c|`在`(0.25, 2]`区间，迭代一定次数后仍旧不大于`2`的复数并展示即可

# 包结构修复

```shell
find -type d | while read folder; do
  if [ ! -f "$folder/__init__.py" ]; then
    echo '# -*- coding: UTF-8 -*-'>$folder/__init__.py
  fi
done
```

# Python规范

## 空格规范

- 运算符 注释所用`#` 都应前后加且仅加一个空格，例如`s = (n + 1) * n / 2 # 1+..+n的求和公式`
- `,` `:` 应只在后面跟且仅跟一个空格，例如`pr_link_li = {val: 2, next: {val: 3, next: None}}`
- `*`(非乘号) `**` `.` 前后不加空格，例如`def __new__(cls, *args, **kwargs):`以及`self.val = 2**n - 1`
- `if` `for` `while` 后如果有括号应有空格隔开，例如`if (a + b) / 2 > c:`
- 函数 参数 下标 不加空格，例如`ans['even-top'] = max(num[0::2])`
- 指明函数参数与参数默认值的赋值符号左右不加空格，例如`def __init__(self, max_length=100):`

## 文件规范

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 标准库
import sys
import os
from subprocess import Popen, PIPE

# 第三方库
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import expon, norm

# 项目
import foo.bar.yourclass
from myclass import MyClass

#############
# statement #
#############

if __name__ == '__main__':
    main()
```

## 命名规范

- 函数命名全小写加下划线而非驼峰，即`maxLength`为错，应为`max_length`
- 常量命名全大写加下划线，例如`MAX_LENGTH`
- 模块名亦文件名 应尽量简短 全小写 以下划线分割单词 模块名同理 特别的 C/C++模块名应如`_socket`以下划线起始
- 禁止使用`l` `I` `O`作为单字符的变量名
- 类命名`CapWord` 模块内类名`_CapWord` 特别的应在后面加上后缀`Error` `Singleton` `Factory` `Dlg` `Ctrl` `Mgr`等表示异常 单例 工厂 对话框 控件 管理

## 代码规范

- 对于序列`string` `list` `tuple`长度是否为空的判断 使用`if seq` `if not seq`
- 较复杂的正则应使用`re.VERBOSE`
- 避免使用BOOL参数

ps^[代码规范本质上时为了代码可读性，并非python语法强制规定，尽可能遵守，但无需奉为圭臬]

# Python单例

装饰器实现方式，目前了解到的比较理想的实现

```python
import functools
import threading


def singleton(cls):
    cls.__instance = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(clazz, *args, **kwargs):
        # 同步锁
        with threading.Lock():
            it = clazz.__dict__.get('__it__')
            if it is not None:
                return it
            clazz.__it__ = it = clazz.__instance(clazz, *args, **kwargs)
            it.__init_original__(*args, **kwargs)
            return it

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__
    return cls
```

# JSON生成文件

`json.dumps(data, ensure_ascii=False, indent=2)`可以生成`data`对应的json字符串，同时维持非ASCII码字符以及添加缩进
