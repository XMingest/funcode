---
title: bat script
author: X_Mingest
authorLink: http://xm.tsohlac.online
date: 2020-09-01 09:23:50
---

# 注释

## REM

注释命令，当在批处理脚本中使用并且`@echo on`时依旧会回显，可用于config.sys文件中作为注释，也在VB中使用

## :

以`:`为首的行统一被认作标号，但只有`:`加上数字字母才是有意义的标号，这类标号通常会配合`goto`语句实现跳转

而诸如`:-` `::` `:?` `:!`等无意义的标号可以起到注释的作用，且即使`@echo on`也不会回显

## % comment %

`rem`与`::`只能作为整行注释，事实上在批处理文件中可以使用`% comment %`这种方式实现行内注释

但由于批处理文件本身调用变量也使用同样的语法，所以行内注释是一种使用需要极其谨慎的语法

## @

`@`开头的指令并非注释，它依旧会执行，但这类指令即时`@echo on`也不会回显

# 特殊变量

## 环境参数

- `%path%` 命令提示符path参数
- `nul` 表示null，常用的如`pause > nul`可以不显示默认暂停信息

## 批处理文件

- `%0` `%1` .. `%9` 命令行参数，通常`%0`为绝对路径，如果参数多于九个，需要使用`shift`获取更多参数，此时会使`%0` = `%1` ... `%9` = next，而在NT内核之后还可使用`shift /n`以第一参数为基准反复移动起始指针

# 数值计算

## set

```bat
set /a "a = 24, b = 8"
set /a "result = %a% + %b%"
:: 32

set /a "(9 + 3) * 9 / 2"
:: 54

set /a "1 << 10"
:: 1024

set /a "0xEFFFFF"
:: 15728639

set /a "078787878"
:: 无效数字。数字常数只能是十进制(17)，十六位进制(0x11)或八进制(021)

set /a "07777654"
:: 2097068
```

#### 增删改查

```bat
set PR
:: 查看所有变量名PR开头的参数表及其值

set a=32
:: 注意，set直接赋值时如果写作`set a = 32`将会把空格当作变量名，即名为`a `的变量赋值为` 32`

set a=
:: 当以等号结尾时将删除参数
```

#### 从标准输入中读入

```bat
set /p a=请输入一个数字：
```

# 字符串处理

```bat
set tststr=abcdefghijklmnopqrstuvwxyz0123456789

echo %tststr:~1,5%
:: bcdef
echo %tststr:~-6,5%
:: 45678

echo %tststr:~5%
:: fghijklmnopqrstuvwxyz0123456789

echo %tststr:~-5%
:: 56789

echo %tststr:~0,-5%
:: abcdefghijklmnopqrstuvwxyz01234

echo %tststr:~1,-5%
:: bcdefghijklmnopqrstuvwxyz01234

echo %tststr:abc=123%
:: 123defghijklmnopqrstuvwxyz0123456789(`tststr` not change)
```

# 条件

```bat
if errorlevel 1 set el=8
if errorlevel 2 set el=22
if errorlevel 3 set el=43
if errorlevel 4 set el=39
if errorlevel 5 set el=5
:: if errorlevel <number>时，系统事实上是判定>=
:: PS: if errorlevel=1不会报错，但=会被忽略

if errorlevel 5 goto el5
if errorlevel 4 goto el4
if errorlevel 3 goto el3
if errorlevel 2 goto el2
if errorlevel 1 goto el1
:: 因为判定方式事实上为>=，所以如果要跳转到相应标号就需要从大到小

if exist "C:\Users\xwx968142" echo @echo off>>"C:\Users\xwx968142\test.bat"
:: if exist可以接目录路径与文件路径

if httpcode=="404" echo "NOT FOUND"
:: if ==
```

## 命令扩展

cmd /e:on可以为某次会话启用命令扩展，也可以通过以下两个注册表项设置默认值0x1开启或0x0关闭

- HKEY_LOCAL_MACHINE\Software\Microsoft\Command rocessor\EnableExtensions
- HKEY_CURRENT_USER\Software\Microsoft\Command Processor\EnableExtensions

也可以通过`setlocal enableextensions`启用，且优先级依次是`setlocal` > `cmd /e:on` > `regedit:current_user` > `regedit:local_machine`

命令扩展对if有一定的改动

1. 允许使用if defined检测参数声明
1. 允许使用if cmdextversion检测版本
1. 允许使用`EQU`(==) `NEQ`(!=) `LSS`(<) `LEQ`(<=) `GTR`(>) `GEQ`(>=)作为比较运算符

## else

`else`与`else if`，以及批处理文件中用括号构成if代码块的例子见[函数](#函数)部分

# 函数

以下是一个计算最大公约数的脚本，在批处理脚本中使用call指令调用函数，而函数声明与标号没有差别

```bat
@echo off

setlocal enabledelayedexpansion
setlocal enableextensions

:: main
call :gcd %1 %2
goto eof

:: greatest common divisor
:gcd
if %~1 == %~2 (
    echo %~1
    goto eof
) else (
    set /a "result = %~1 - %~2"
    if "!result:~0,1!" == "-" (
        call :gcd %~2 %~1
    ) else (
        set /a "rest = %~1 %% %~2"
        if !rest! == 0 (
            echo %~2
            goto eof
        )
        set /a "rest1 = %~1 %% !rest!"
        set /a "rest2 = %~2 %% !rest!"
        if rest1 == 0 if rest2 == 0 (
            echo !rest!
            goto eof
        )
        call :gcd %~2 !rest!
    )
)

:eof
```

# 路径处理

通过`pushd`与`popd`进行路径处理

```bat
:: 进入当前批处理文件所在目录
pushd %~dp0
:: 回到之前的目录，当前目录被从目录栈中移除
popd
:: 回到之前的目录，但是保留当前目录为上一目录
pushd
```

`popd +2` `pushd +2`有类似的效果

事实上通过`dirs`可以处理目录栈，也可以通过`cd -`实现类似`pushd`的效果

# 相关链接

1. [bat中的算术运算](https://blog.csdn.net/sanqima/article/details/37902463)
1. [bat批处理之字符串操作](https://blog.csdn.net/cpwolaichile/article/details/74170979)
1. [bat脚本的基本命令语法](https://www.cnblogs.com/lizm166/p/11132601.html)
1. [windowsCMD命令大全及详细解释和语法](http://xstarcd.github.io/wiki/windows/windows_cmd_syntax.html)
