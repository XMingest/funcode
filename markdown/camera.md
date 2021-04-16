# 摄像头

基本原理

1. 镜头聚光成像
1. 传感器转换为电信号（此处作用等同传统相机的底片）
1. 模拟数字转换器（可简称为ADC或AD）转为数字信号
1. 曝光增益控制等各种图像信号处理
1. 按照一定时序与格式输出数字图像信号

## 基本结构

- 补强（依结构和工艺情况）
- 传感器芯片（sensor chip）
- 红外滤光片（IR filter）
- 镜头（lens）
- 镜头座（lens holder）
- 连接器
- 柔性印刷电路板（flexible printed circuit board，FPC）
- 印制电路板（printed circuit board，PCB）

相同结构可以按照不同工艺分为

- COB（chip on board）
- COF（chip on flex）
- CSP（chip scale package）

结构上存在更多差别巨大的模组

如FPC+BTB结构模组由以下物料构成

- Connector
- FPC
- Holder
- Lens
- PCB 6*6
- Poron
- Protect Film
- Sensor 380

Socket结构物料则无需FPC、Connector

## 重要模组

- 模拟信号处理器
- 时序发生器
- 数字视频端口
- 图像传感器阵列
- ADC（A/D转换器，模拟数字转换器）
- ISP（image sensor processor，图像传感器处理器）
- SCCB接口（serial camera control bus）
- ...

## 传感器

最基本的三层结构为微镜头、滤色片、感光像素阵列

#### 微镜头

微镜头涉及BSI（后向透光）与FSI（前向透光），为有效地利用入射光线，需保证每个像素上有一个微镜头

#### 滤色片

在光电传感器地正方形网格上布置透过不同颜色地阵列，以此获得色彩信息

如拜尔滤色镜（bayer filter），以`[[R, G], [G, B]]`形式排列，所以也被称为RGGB、RGBG、GRGB

#### 感光像素阵列

由感光单元、行列读取电路、输出缓冲器组成

## 分类

按像素大小分为

    10M   352x288    CIF
    30M   640x480    VGA
    130M  1280x1024  SXGA
    200M  1600x1200  UXGA
    320M  2048x1536  QXGA

按焦距是否可变分为

    FF  fixed-focus   固定焦点或无焦点
    MF  manual-focus  手动对焦
    AF  auto-focus    自动对焦

按IC工作原理分为CCD与CMOS，相比较而言CMOS集成度高，续航强，速度快，正在逐步成为主流

    电行耦合元件（charge-coupled device，CCD）,是一种半导体器件，上植入微小的光敏物质像素（pixel）
    互补金属氧化物半导体（complementary metal–oxide–semiconductor），是电压控制的放大器件，也叫complementary-symmetry metal–oxide–semiconductor（COS-MOS）

按输出数据格式分为JPEG、Raw、RGB、YUV

    事实上早期照片与电视都是黑白的，彼时图像只需要Y数据

    也就是亮度，某种程度上与灰度类似，参考常见灰度公式为 $$0.299 * R + 0.587 * G + 0.114 * B$$（人眼对RGB三种色彩的感知不同，所以基于不同的权重，该权重只适用于sRGB空间），而亮度有时直接计算RGB的均值，但也存在一些系统将它与灰度同样通过一定的权重运算

    后来彩色图像出现，便通过YUV/YIQ来处理，这种格式数据的好处就在于只使用Y数据就可以兼容黑白设备，而UV为彩色设备提供色度支持，但事实上彩色设备诞生至今，大都使用RGB数据最终完成图像输出的，因此YUV格式的数据除了在黑白设备上，都会最终转换为RGB

    但YUV有另一方面的优势，按照部分学者研究，人眼对亮度事实上敏感超过色彩，由此将亮度单独保存的YUV格式可以进行一定程度的过压缩，从而在尽可能不影响观感的情况下获得比RGB格式更好的压缩率，这也是为什么大量相机采用YUV格式

按接口分为

    MDDI 高通
    MIPI 移动行业处理器接口（mobile industry processor interface），除了高通，甚至苹果都在用
    Parallel 并口，也叫数字视频端口（digital video port，DVP）

按传感器光学尺寸分为

    1/3.2"
    1/4"
    1/5"
    1/11"


# REF

1. [Danny明泽.CCD与CMOS的区别？](https://blog.csdn.net/qq_36955294/article/details/109669787)
