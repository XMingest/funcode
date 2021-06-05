# 极差修改工具

门限文件解析，并且按照预定规则展示修改前后比较，可由用户进行检查并进一步修改

建议使用3.8+版本，在3.8之后，ElementTree不会自动重排节点属性

## pyinstaller

1. 基本环境
```shell
python -m venv pyvenv
cd pyvenv
Scripts/Activate.ps1
pip install wheel
python -m pip install -U pip setuptools
pip install openpyxl pyinstaller PySide2 QDarkStyle
# TODO: icon图标文件处理
cp Lib/site-packages/shiboken2/shiboken2.abi3.dll Lib/site-packages/PySide2  # 解决WARNING: lib not found: shiboken2.abi3.dll
pyinstaller --add-data "icon.ico;." -F -i icon.ico -n 极差修改工具 -w __main__.py  # add-data中的图标文件名在程序中规定，不能更改，但`-i icon.ico`可以与其不同
```

## ui to py

`pyside2-uic -o ui_main_window.py main_window.ui`
