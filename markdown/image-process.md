# 数字图像处理

图像处理可分为在空间域或频率域进行，在空间域进行的变换直接对图像像素进行操作，可由下式表示
$$g \left( x, y \right) = T \left[ f \left( x, y \right) \right]$$
其中`f(x, y)`为输入图像，`g(x, y)`为输出图像，T对点`(x, y)`领域进行操作的算子

而在频率域进行的操作，在图像的傅里叶变换上执行

## 亮度

球面度，sr，立体角单位，用以描述三维的弧度，当立体角顶点位于球心，对应球面表面积与球体半径平方比值，如球体表面积为
$$4 \pi r^2$$
则完整球面的球面度为
$$\frac {4 \pi r^2}{r^2} = 4 \pi \left( sr \right)$$

流明，lm，光通量单位，指单位时间内由光源所发出或由被照物所吸收的总光能

坎德拉，cd，光强单位，指光源在给定方向上每单位立体角内所发出的光通量，可通过光通量与球面度计算
$$cd = lm / sr$$

尼特，nit，亮度单位，是坎德拉每平方米的别称
$$nit = cd / m^2$$

朗伯（Lambert） 简称L，la或者Lb，亮度单位，对应国际标准制亮度单位换算如下
$$1L = \frac {1}{\pi} cd / cm^2 = \frac {10^4}{\pi} cd / m^2$$

当亮度小于千分之几尼特时，锥状细胞失去活性，杆状细胞开始工作，提供感光功能，这时的视觉叫做暗视觉，在暗视觉中人只能分辨明暗，没有颜色感觉，辨别物体细节的能力大大降低

而根据实验数据，主观亮度大约是进入人眼的光强的对数函数，适应范围广，从暗阈值（`e-9`L）到强闪光（10L）,其中暗视觉与亮视觉的过渡范围为
$$10^{-6}L \sim 10^{-4}L$$

然而主观亮度，或称感知亮度并不是简单的强度的函数，这一认知基于数个基本的事实

视觉系统在不同强度区域的边界处出现“下冲”或“上冲”现象，比如两个光强不同的色块边界，从光强较弱的边缘至较强边缘，前者会出现“下冲”现象，后者相反，厄恩斯特马赫于1865年首次描述了这一现象，被称为马赫带

第二种现象被称为同时对比，背景更亮的中心方块主管亮度会变得更暗

还有许多来自于错觉的现象，在这些现象中，往往会填充不存在的信息，或错误地感知了物体的几何特点，这些错觉至今没有被人类完全了解

## 色彩

1666年，牛顿发现了光的色散，从而人类得以逐步揭开色彩于电磁波谱的奥秘

我们感受到的可见光的彩色范围只占电磁波的一小部分，波谱一端是无线电波，波长是可见光的几十亿倍，另一端是伽马射线，波长只有可见光的几百万分之一

波长（λ），频率（ν）与光速（c）之间存在下列关系，因此短波高频，长波低频
$$\lambda = c / \nu$$

而引入普朗克常数（h）后，可以计算电磁波谱各个分量的能量如下
$$E = h \nu$$

人感受一个物体的颜色由物体反射光的性质决定，以所有可见波长相对平衡地反射光的物体对观察者而言是白色的，相反，只反射有限范围波长的物体则会呈现出色彩，如绿色物体反射波长为500nm~570nm的光，吸收其他波长的大部分能量

## 图像

设`V`为图像集合，比如在二值图像中，$$V = \left\{ 1 \right\}$$

在RGBA图像中，$$V = \left\{ \left( r, g, b, a \right) \mid r, g, b \le 255 \land r, g, b \in N \land a \in \left[ 0, 1 \right] \right\}$$

诸如此类，对于某个图像，单位色块值在指定集合`V`中则称为一个像素

对单个像素的引用往往使用`p` `q`这类小写字母

## 邻接

对于一个点`(x, y)`，有四个水平或垂直的相邻像素，分别是

    (x + 1, y)
    (x - 1, y)
    (x, y + 1)
    (x, y - 1)

表示为$$N_4 \left( p \right)$$

同时有四个对角相邻像素

    (x + 1, y + 1)
    (x - 1, y + 1)
    (x + 1, y - 1)
    (x - 1, y - 1)

表示为$$N_D \left( p \right)$$

上述八个邻点，一起称为8邻域，表示为$$N_8 \left( p \right)$$

4邻接，`p`与`q`4邻接意味着$$q \in N_4 \left( p \right)$$

8邻接，`p`与`q`8邻接意味着$$q \in N_8 \left( p \right)$$

m邻接（混合邻接），`p`与`q`混合邻接意味着8邻接但两者不存在有意义的公共4邻接像素，即$$q \in N_8 \left( p \right) \land \left[ \forall s \in N_4 \left( p \right) \land s \in V \to s \notin N_4 \left( q \right) \right]$$

## 空间分辨率

图像中可辨别的最小细节的度量，通常使用每单位距离线对数和每单位距离点数

例如图像中线宽为`0.1 mm`，那么图像分辨率可以是`5 线对/mm`

又比如报纸上每英寸由75个点印刷，此时图像分辨率为`75 dpi`

图像分辨率事实上与尺寸息息相关，但现实生活中，诸如视频信息等处往往会仅标注像素宽高，事实上那并不反应分辨率，需要将其与载体尺寸结合空间分辨率才有意义

## 灰度分辨率

同上，灰度分辨率指在灰度级中可分辨的最小变化

如果一幅图像的灰度被量化为256个等级，那么它有`8 bit`的灰度分辨率，也称为灰度级数

基于硬件考虑，灰度级数被设定为2的幂数，最通用的灰度级数是`8 bit`

也存在`10 bit`与`12 bit`的系统，它们属于一些特例，在某些图像增强应用中，会用到`16 bit`，再往上，`32 bit`的灰度级数就非常罕见了

早期部分研究通过把一些图像改变灰度级数，然后要求观察者主观地对图像排序

研究中发现，细节更多的图片偏爱度相对灰度级数变化更小，这表现出细节更多的图片可能只需要较少的灰度级数

同时排除误差，在部分间隔内灰度级数降低并没有影响偏爱值，甚至导致偏爱值增加，可能的原因是灰度级数降低使得对比度增加，导致人们感觉图片更为清晰分明

## 缩放

#### 最近邻内插

将原图像中最近邻的像素赋给新位置

如将`x * y`的图像`img`等比缩放`d`倍

```python
def fake_func(path, d):
    # 假设Image类存储图像数据
    img: Image = Image.open(path)
    # 原宽高
    x, y = img.get_size()
    # 新宽高
    w = round(x * d)
    h = round(y * d)
    img_new = Image(width=w, height=h)
    # 最近邻
    for i in range(w):
        for j in range(h):
            img_new.set(i, j,
                        img.get(round(i / d), round(j / d)))
```

该方法简单但并不常用，因为它存在产生不希望的人为缺陷的倾向，如某些边缘的严重失真

#### 双线性内插

用4个最近邻去计算给定位置的像素

#### 双三次内插

用16个最近邻去计算给定位置的像素，商业图像编辑程序通常会使用双三次内插法，如Adobe Photoshop和Corel Photopaint

# 句

它的与众不同之处在于，是透过光线看阴影还是透过阴影看亮度<p align="right">——大卫·林赛</p>

# REF

1. 《数字图像处理》第三版 冈萨雷斯