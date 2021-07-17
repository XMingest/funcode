---
title: Msys2配置
author: X_Mingest
authorLink: http://xm.tsohlac.online
date: 2020-08-29 14:31:49
---

# 注册表

```reg
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\Msys2]
"icon"="\"D:\\Programs\\msys64\\msys2.ico\""

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\Msys2\command]
@="\"D:\\Programs\\msys64\\msys2_shell.cmd\" -here"
```

# 软件列表

```shell
pacman -S base-devel clang cmake compression development \
        git libraries llvm msys2-devel perl-modules \
        python-devel python-pip sqlite tree vim-plugins
```

## 其余软件

- ffmpeg: mingw-w64-x86_64-ffmpeg
- Gimp: mingw-w64-x86_64-gimp
- Graphviz: mingw-w64-x86_64-graphviz
- lua: mingw-w64-x86_64-lua mingw-w64-x86_64-lua-lpeg mingw-w64-x86_64-lua-luarocks mingw-w64-x86_64-lua-mpack
- Qt: mingw-w64-x86_64-clang mingw-w64-x86_64-cmake mingw-w64-x86_64-qt-creator mingw-w64-x86_64-gdb
- Ruby: mingw-w64-x86_64-ruby
- Rust: mingw-w64-x86_64-rust
    - 通常需要添加Windows用户目录下的.cargo/bin到PATH中
    - 相应配置文件在windows用户目录下而非msys2用户目录

# 配置shell run config

## bashrc

```shell
# rust
export RUSTUP_DIST_SERVER='https://mirrors.tuna.tsinghua.edu.cn/rustup'

# 每等待输入即显示，其中使用了方框绘制字符
export PS1='\n╭\[\e[31m\]AT\[\e[0m\] \[\e[32m\]\t\[\e[0m\] \[\e[31m\]IN\[\e[0m\] \[\e[33m\]\w\[\e[0m\]\n╰'

# alias
alias cnvgbk='iconv -f gbk'
alias code='/c/Program\ Files/VSCode/Code'
alias git='/d/Programs/Git/cmd/git'
alias la='ls -A'
alias ll='ls -hl'

# path
PATH="/mingw64/bin:/mingw64/bin/core_perl:/mingw64/bin/site_perl/5.28.0:/mingw64/bin/vendor_perl"
PATH="$PATH:/c/Users/X_Mingest/.cargo/bin"
PATH="$PATH:/usr/local/bin:/usr/bin:/bin"
PATH="$PATH:/c/Windows/SysWOW64:/c/Windows:/c/Windows/SysWOW64/Wbem:/c/Windows/SysWOW64/WindowsPowerShell/v1.0"
PATH="$PATH:/d/Programs/node"
```

# 依赖

`msys-2.0.dll`

# 默认SHELL

- mingw32.ini | mingw64.ini | msys2.ini
```ini
SHELL=/usr/bin/zsh
```
- msys2_shell.cmd
```bat
set "LOGINSHELL=zsh"
```

# 相关

1. [Msys2](https://mirrors.tuna.tsinghua.edu.cn/msys2/distrib/msys2-x86_64-latest.exe)
1. [TUNA开源镜像](https://mirrors.tuna.tsinghua.edu.cn/)
