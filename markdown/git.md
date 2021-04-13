---
title: Git
author: X_Mingest
authorLink: http://xm.tsohlac.online
date: 2020-08-25 09:54:57
---

# 版本控制系统（VCS）

版本控制是一种记录一个或若干文件内容变化，以便将来查阅特定版本修订情况的系统

它通常意味着提供使用者查看任意一次记录，以及回到该次记录的功能

而VCS中，git在提供记录的同时有着自己的快照形式、对文本文档的深度支持以及协作开发上高度优化

# 安装git

gitlab依赖于本地已安装git程序，可在命令提示符或者powershell等终端中输入`git --version`，如果返回`git version X.XX.X`则说明已安装

未安装可打开[仓库链接](http://mirrors.tools.huawei.com/git-for-windows/)，选择相应版本目录下`Git-*-64-bits.exe`下载安装

安装完成后可在终端中按照需要运行以下指令完成基础设置

```shell
# 编码问题
git config --global i18n.commitencoding utf-8

# 向gitlab代码仓库上传代码需要设置，将显示在相应上传信息中
git config --global user.email ${邮箱}
git config --global user.name ${用户名}

# 不影响本地换行符时维持仓库内换行符正常，同时避免提交代码时报错无法进行
git config --global core.autocrlf input
git config --global core.eol lf
git config --global core.safecrlf false

# 添加代理，可访问github仓库，密码部分如果有:@替换为%3A%40
git config --global http.proxy http://${W3用户名}:${W3密码}@proxy.huawei.com:8080
git config --global https.proxy http://${W3用户名}:${W3密码}@proxy.huawei.com:8080
```

其中`${...}`指对应项的具体值

# ssh密钥生成

在终端中运行

```shell
ssh-keygen -o -t rsa -b 4096 -C ${邮箱} # 根据指定邮箱使用RSA算法生成4096位的密钥
# 默认情况下，私钥文件保存在~/.ssh/id_rsa，公钥保存在~/.ssh/id_rsa.pub
cat ~/.ssh/id_rsa.pub | clip # 读取公钥内容到剪贴板，可直接粘贴
# cat在git bash，powershell等终端可以使用，cmd不支持cat
```

# git子仓库

git代码仓库中的某个下级目录本身即引用一个git仓库，或者应当单独进行开发维护复用

举个例子，假设有两个仓库，分别为main和lib，而main需要使用lib作为子仓库，这时就用到了`git submodule`[^1]

ps: 第三方的`git subtree`同样可以实现子仓库[^2]

## 实现

```shell
git clone ${main_repo_url} main/
cd main
git submodule add ${lib_repo_url}
```

以上命令执行之后，事实上main就有了子目录lib即相应仓库的文件，同时git自动创建了一个.gitmodules的文件在主仓库main下面

```properties
[submodule "lib"]
	path = lib
	url = ${lib_repo_url}
```

将这个文件暂存提交到main仓库中，子仓库客观上就已经构建好了

# 相关链接

- [Git官方文档中文版v2](https://git-scm.com/book/zh/v2)

[^1]: https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97
[^2]: https://juejin.im/post/6844904034722119694
