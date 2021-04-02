# pacman

```shell
# 查看镜像组
pacman -Sgg | awk '{print $1}' | uniq -c
# 查看仓库
pacman -Sl | awk '{print $1}' | uniq -c
# 忽略时间戳强制更新镜像信息
pacman -Syy
# 更新包
pacman -Syu
# 查看本地组
pacman -Qg | awk '{print $1}' | uniq -c
# 查看某个文件的包归属
pacman -Qo ${file}
# 查看有更新的包
pacman -Qu
```

# zypper

```shell
# 源
# 添加 addrepo|ar
zypper ar ${domain} ${repo_name}
# 删除 removerepo | rr
zypper rr ${repo_name}
# 查看包信息
zypper info
# 安装
zypper install
# 查看补丁
zypper patches
# 指定补丁安装
zypper patch ${patch}
# 移除
zypper remove
# 搜索
zypper search
```
