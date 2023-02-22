# 文档

## user_guide

次目录为学习 `reportlab` 包时，摘录出来的生成官方用户手册的汉化版本。（机翻+人工翻）

需要环境：`python 3.6+` , 安装 `reportlab` 包,

中文版图表示例，需要安装安装reportlab官网 "**rlextra**" 包， 需要注册用户.

生成 `reportlab` 的用户手册请按下列方法执行：

```shell script
# 英文原版 和 中文对照版
cd user_guid  
python genuserguide.py
# 中文整理版
cd user_guide_cn  
python gen_cn_user_guide.py
```

开源字体解决方案：

参考:

   1. <https://github.com/adobe-fonts/source-han-sans/blob/master/README-CN.md>  
   2. <https://sspai.com/post/26251#!>

True Type 字体介绍：<https://blog.csdn.net/gaojinshan/article/details/80319856>

思源黑体、思源宋体TTF介绍：<https://www.v2ex.com/t/399030>

1. <https://github.com/be5invis/source-han-sans-ttf/releases>
2. <https://github.com/junmer/source-han-serif-ttf>
3. <https://github.com/Pal3love/Source-Han-TrueType>

## 示例

* [example_cn.pdf](./example_cn.pdf) 是仅仅只有中文的使用说明
* [example_en_cn.pdf](./example_en_cn.pdf) 是英文原文和中文对照的使用说明
