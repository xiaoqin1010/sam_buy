# sam_buy
山姆买菜

platform: ios15;


app version: v5.0.45.1;


python version: 3.8.6;


## 代码中有注释，遵循注释进行修改 运行即可

# 关于抓包
鄙人用的是http catcher(applestore可以下载)，实测charles也可以。

至于https包显示unknown请自行查阅https抓包的问题（多半是证书配置问题）

# 疫情当下上海买菜太难了

getCapacityData跑通了后（计数器开始）,记得测试一下commitpay方法。

测试方法：

把代码中唯一一句 if not 中的not去掉然后运行脚本，显示配送时间预约满 即为测试成功.

显示库存不足或者其他的错误需要检查commitpay方法的data.

另外 测试完成后记得还原if not.

下单成功后会有音乐响起，需要自行前往app付款


## 倡导大家只够买必需品！不要浪费运力
交流群

![Alt text](https://github.com/azhan1998/sam_buy/blob/main/QRcode.jpg)

# 仅供学习交流，不可用于非法牟利。
# 版权说明
本项目为 GPL3.0 协议，请所有进行二次开发的开发者遵守 GPL3.0协议，并且不得将代码用于商用。
