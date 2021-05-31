# 环境变量

名 | 述
:-: | :-
GOARCH | 处理器架构，可以是`386` `arm`或者`amd64`
GOBIN | 编译器和链接器位置，通常是`$GOROOT/bin`，在`1.0.3`之后为空将使用默认值
GOOS | 系统，可以是`darwin` `freebsd` `linux` `windows`
GOROOT | 安装目录，在linux上一般为`$HOME/go`

## go module

要求`go version`版本在11以上

```
go env -w GO111MODULE=on
go env -w GONOSUMDB=*
go env -w GOPROXY=http://mirrors.tools.huawei.com/goproxy/
```

# linux上安装

安装C工具链

- bison
- ed
- gawk
- gcc
- libc6-dev
- make

获取源码执行`all.bash`

1.4之后go语言实现了自举，由此需要设置`GOROOT_BOOTSTRAP`变量，指向一个1.4版本的已安装的Go版本

# 目录结构

    /bin：包含可执行文件，如：编译器，Go 工具
    /doc：包含示例程序，代码工具，本地文档等
    /lib：包含文档模版
    /misc：包含与支持 Go 编辑器有关的配置文件以及 cgo 的示例
    /os_arch：包含标准库的包的对象文件（.a）
    /src：包含源代码构建脚本和标准库的包的完整源代码（Go 是一门开源语言）
    /src/cmd：包含 Go 和 C 的编译器和命令行脚本

# REF

- [Go REPL](https://github.com/sbinet/igo)
- [unknown/the-way-to-go_ZH_CN](https://github.com/unknwon/the-way-to-go_ZH_CN)
