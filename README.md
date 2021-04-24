
# 爱抢购商品监控 Python脚本

## 主要功能
- 对爱抢购app上的商品进行价格以及状态监控
	- 输入商品id、期待价格expect-price、是否连接代理池isproxy
- 连接代理池
	- 用于解决爱抢购服务器反爬机制 tips:因为代理池免费，可能不稳定
- 铃声提示
	- 商品当前价格达到商品期望价格时，会**持续播放提醒音乐**，直到商品被抢光
	
## 运行环境

- [Python 3](https://www.python.org/)

## 第三方库

- 需要使用到的库已经放在requirements.txt，使用pip安装的可以使用指令  
`python3 -m pip install -r requirements.txt`
- 如果国内安装第三方库比较慢，可以使用以下指令进行清华源加速
`python3 -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/`

## 使用教程

#### 1.获取商品id

- 打开爱抢购app，找到需要监控的商品，分享商品至QQ，对话框里url中id参数的值即是

#### 2.运行程序

- 进入程序目录
`cd iqg-monitor`

- 执行iqianggou.py 其中id为必填项

```python
python3 iqianggou.py [-h] [-expect-price EXPECT_PRICE] [-isproxy ISPROXY] id

positional arguments:
  id                    商品id 获取方式：分享商品至QQ，url中id参数的值

optional arguments:
  -h, --help            show this help message and exit
  -expect-price EXPECT_PRICE  期待商品价格 默认为1                      
  -isproxy ISPROXY      是否连接代理池 默认为0
```


## 注意事项
- 代理池不稳定，提示代理出错后会重连，**不需要重新执行程序**，如果多次报错，为不影响监控效果，请重新运行程序并不启用代理池
- 商品当前价格未达到期待价格时，程序不会有太多输出（连接池重连除外），放在后台运行即可
- 代码出现bug请提交issue，不定时查看并更新
- 本代码仅供学习交流，须在法律允许范围内使用！

## 关于
项目作者：ve99tr
作者博客：https://blog.csdn.net/qq_42939527


