# rustup-init

通过[清华源](https://mirrors.tuna.tsinghua.edu.cn/rustup/rustup/archive/)下载相应版本`rustup-init.exe`

设置环境变量

```shell
# linux
RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup

# windows powershell
$env:RUSTUP_DIST_SERVER='https://mirrors.tuna.tsinghua.edu.cn/rustup'
```

运行`rustup-init.exe`便可以从清华源安装rust

# sysroot

通过指令`rustc --print sysroot`

# REF

1. [Rust程序设计语言简体中文版](https://kaisery.github.io/trpl-zh-cn/)
