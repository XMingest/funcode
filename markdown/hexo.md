---
title: hexo
author: X_Mingest
authorLink: 'http://xm.tsohlac.online'
date: 2021-03-01 10:52:58
---

# 简介

基于Node.js的博客框架

# 终端

## 安装

```shell
npm install hexo-cli -g
hexo init blog
cd blog
```

## 服务

```shell
hexo clean  # 清理
hexo s
```

## 新博文

```shell
hexo new "hello_world"
```

## 构建

```shell
hexo g
```

# 变量

变量 | 描述
:- | :-
site | 网站变量
page | 针对该页面的内容以及front-matter中自定义的变量
config | 网站配置`/_config.yaml`
theme | 主题配置`/themes/*/_config.yaml`，继承自网站配置
path | 当前页面的路径不含根路径
url | 当前页面的完整网址
env | 环境变量

## site

变量 | 描述
:- | :-
site.posts | 所有文章
site.pages | 所有分页
site.categories | 所有分类
site.tags | 所有标签

## page

变量 | 描述
:- | :-
page.title | 页面标题
page.date | 页面建立日期
page.updated | 页面更新日期
page.comments | 留言是否开启
page.layout | 布局名称
page.content | 页面的完整内容
page.excerpt | 页面摘要
page.more | 除了页面摘要的其余内容
page.source | 页面原始路径
page.full_source | 页面的完整原始路径
page.path | 页面网址，不含根路径，我们通常在主题中使用`url_for(page.path)`
page.permalink | 页面的完整网址
page.prev | 上一个页面，如果此为第一个页面则为`null`
page.next | 下一个页面，如果此为最后一个页面则为`null`
page.raw | 文章的原始内容
page.photos | 文章的照片，用于相簿
page.link | 文章的外部链接，用于链接文章

#### post

变量 | 描述
:- | :-
page.published | 文章是否已发布
page.categories | 该文章的所有分类
page.tags | 该文章的所有标签

#### index

变量 | 描述
:- | :-
page.per_page | 每页显示的文章数量
page.total | 总页数
page.current | 目前页数
page.current_url | 目前分页的网址
page.posts | 本页文章，Data Model
page.prev | 上一页的页数，如果此页是第一页的话则为0
page.prev_link | 上一页的网址，如果此页是第一页的话则为''
page.next | 下一页的页数，如果此页是最后一页的话则为0
page.next_link | 下一页的网址，如果此页是最后一页的话则为''
page.path | 当前页面的路径，不含根目录，我们通常在主题中使用`url_for(page.path)`

#### archive

与index布局相同，但新增以下变量

变量 | 描述
:- | :-
page.archive | 归档为`true`
page.year | 年份归档`0000-9999`
page.month | 月份归档`1-12`

#### category

与index布局相同，但新增以下变量

变量 | 描述
:- | :-
page.category | 分类名称

#### tag

与index布局相同，但新增以下变量

变量 | 描述
:- | :-
page.tag | 标签名称

# 相关链接

1. [hexo](https://github.com/hexojs/hexo)
1. [hexo-renderer-markdown-it](https://github.com/hexojs/hexo-renderer-markdown-it)
