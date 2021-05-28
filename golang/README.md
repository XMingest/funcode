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

# REF

- (unknown)[https://github.com/unknwon/the-way-to-go_ZH_CN]
