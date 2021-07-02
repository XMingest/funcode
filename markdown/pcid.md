# 方案

方案 | 描述 | Windows | Linux
:- | :- | :- | :-
网卡MAC | 多个网卡会有多个mac地址，且可人工修改 | `ipconfig /all` | `dmesg`<br>`ifconfig -a`<br>`ip link`<br>`nmcli device show`
硬盘序列号 | 多个硬盘，且流动性大 | `wmic diskdrive get serialnumber` | `fdisk -l`<br>`lsblk`<br>`lsscsi`<br>`smartctl`<br>RAID阵列有各自相应管理工具
主板ID | 推荐，唯一且不随重装系统改变，只是部分厂商不提供，此时会返回全为F的无效ID | `wmic csproduct get UUID` | `dmidecode -s system-uuid`
CPU ID | 不唯一，同批次或某些情况会相同 | `wmic cpu get processorid` | `cat /proc/cpuinfo`<br>`dmidecode`<br>`lshw`
MachineGUID | Windows安装时生成的唯一GUID，重装系统后会改变 | `regedit` `HKEY_MACHINE\SOFTWARE\Microsoft\Cryptography` | -
Windows的产品ID | 不唯一，同个安装镜像或者克隆会相同 | `regedit` `HKEY_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion` | -

除此之外，类似设计程序为计算机生成保存唯一标识，或者使用硬件如USB设备进行外置验证，在不同应用场景同样可以起到标识特定计算机的作用

# REF

- [获取设备唯一标识（Unique Identifier）:Windows系统](https://blog.csdn.net/qq_32403473/article/details/81505664)
