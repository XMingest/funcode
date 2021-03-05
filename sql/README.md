# mysql

## windows

可在各大镜像源下载，建议下载zip包，如`mysql-8.0.21-winx64.zip`

解压后添加`bin`至系统`PATH`

```shell
# 初始化，这里会生成默认密码，可删除data目录之后重新初始化
mysqld --initialize --console
# 安装或卸载服务
mysqld --install
mysqld --remove
# 启动mysql服务
net start mysql
# 修改mysql密码，-p与旧密码之间不能有空格
mysqladmin -u${user} -p${pswd} password ${new_pswd}
```

## 数据

`load data`通常效率高于`insert`

而`insert into ${table_name} values (...), (...)`通常效率高于分别写两条insert

有索引的情况下效率会降低

因此应当采取`load data`插入数据，并在数据完成后建立索引

如存在文件`data`如下

```
"张三","20","法外狂徒"
"李四","16","受害者"
```

执行以下指令就会分别将每一个`\n`之前`,`分隔的三个`"`分别对应`name`，`age`，`description`插入到表`ct`中

```sql
load data infile 'data' replace into table ct
fields terminated by ','
enclosed by '"'
lines terminated by '\n' (`name`,`age`,`description`);
```

将表导出成相应文件的指令如下

```sql
select `name`, `age`, `description` from ct into outfile 'data'
fields terminated by ','
enclosed by '"'
lines terminated by '\n';
```
