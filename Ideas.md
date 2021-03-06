_过时已解决或者不成立的Ideas 及时用删除线标记_

# 路口识别问题
+ 考虑城市路况和非城市路况：  
    城市路况：有信号指示灯  
    非城市路况：可能没有指示灯  
    所以在判断路口的问题上就是**一个多信号识别过程，不仅仅通过识别路口指示灯，也通过其他的路口信息来处理**   

+ 要知道所使用的相机  
    + 单目相机还是双目相机
    + 分别安装在哪里
    + 通过相机型号对相机性能进行深入了解

+ 解决一下三个问题：  
    ~~1. 车现在在空间哪个位置 -- **定位问题**~~  
    ~~2. 这个位置现在在什么地方 -- **建模问题**~~  
    ~~3. 车要怎么继续往前走 -- **决策问题**~~  

    ~~综上，所了解到要处理问题是一个**视觉SLAM 问题**~~  
    ~~但是视觉SLAM 所解决的问题是空间定位问题，能够在路径识别等方向有贡献？~~  
    
+ 2017.11.25   
    在文献**计算机视觉算法与智能车应用** 中找到思路：  
    由于SLAM 属于立体视觉方向，这里并不需要，因此删除以上Idea
    路口识别分为两步：   
        1. 基于SURF 的粗定位   
            通过特征提取知道是否是一个路口，这样做可以减少计算量  
        2. 基于IPM的高精度实时定位   
            用于判断汽车在路口的具体位置

+ 2017.11.26  
    今天将论文的整体研究方向定好： [论文设计思路](E:\Dropbox\1.3-Masterarbeit\Projects\设计思路.pdf)  
    按照这个思路，将进行如下研究：  
    1. 弄清楚使用相机的情况，然后对相机进行深入了解；  
    2. 弄清楚路口应用场景，从而针对性做好路口特征库；  
    3. 弄懂SURF 理论，并找出关于SURF 在路口识别方向的论文或者代码学习；  
    4. 完成路口特征库的建立；  
    5. 针对具体的路况图像，根据SURF 方法提取特征，判断是否为路口；  
    6. 了解IPM 的理论原理；  
    7. 根据几何原理对汽车位置进行精准测量  

    _注：研究使用的工具情况：_  
    _+ 语言：**Python**_  
    _+ 使用**深度学习**的方法_  
    _+ 基于**CPU** 和**GPU** 的计算时间对比_  

+ 2017.12.04  
    需要确定团队所使用的工具：  
        1. OpenCV 版本  

+ 2017.12.06  
    需要确定哪些特征决定路口  
    需要考虑汽车实际在道路上的不同情况，比如汽车并不在某一条道路上行驶， 比如有其他物体干扰了视线  
    需要考虑摄像机在不同位置是否需要重新训练等情况  

+ 2017.12.12  
    先用OpenCV 的方法识别路口  
    然后使用深度学习的方法  

+ 2017.12.15  
    如何提取路口有效特征，在不考虑算法的前提下  
    算法是为了让特征提取更精确的方法  