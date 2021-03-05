# 包结构修复

```shell
find -type d | while read folder; do
  if [ ! -f "$folder/__init__.py" ]; then
    echo '# -*- coding: UTF-8 -*-'>$folder/__init__.py
  fi
done
```
