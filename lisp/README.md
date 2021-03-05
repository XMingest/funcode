# 环境

从[sbcl/sbcl](https://github.com/sbcl/sbcl)安装

Windows下需确认环境变量`SBCL_HOME`存在，值为安装目录

可`sbcl --core /path/to/some.core`启动，无需`SBCL_HOME`

# Hello, World

编写`hello.cl`

```lisp
(defun hello-world ()
  "Now everything begins"
  (format t "Hello, World!"))
```

通过`sbcl --script hello.cl`直接执行，不过由于这段代码只有声明，所以直接执行不会有理想的效果
需要在后面添加`(hello-world)`

运行`sbcl`，`(load "hello.cl")`执行该文件，`(load (compile-file "hello.cl"))`编译为`hello.fasl`并执行
