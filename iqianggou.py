import requests
import argparse
from fake_useragent import UserAgent
import json
from playsound import playsound
import time


def getip():
    api = "http://118.24.52.95:5010/get/"
    re = requests.get(api).json()
    proxy_ip = re.get("proxy")
    return proxy_ip

def iqianggou(id,expect_price,times,isproxy):
    url = "https://m.api.iqianggou.com/api/item/%d"%(id)
    # print("URL: ",url)
    re = requests.get(url)
    re.encoding="UTF-8"
    re_text = json.loads(re.text)
    item_statu = re_text['data']['stock_status']
    print("\033[0;32;40m[+]监控商品：%s    \n[+]商品状态:%s\033[0m\n\n\033[0;32;40m[+]监控状态：正在监控\033[0m"%(re_text['data']['name'],item_statu))
    if isproxy:
        print("\033[0;32;40m[+]是否连接代理池状态：true\033[0m\n")
    else:
        print("\033[0;33;40m[-]是否连接代理池状态：false\033[0m\n")

    ua = UserAgent()
    while("正在抢购" in item_statu):
        try:
            proxy_ip = getip()
            headers = {"User-Agent" : ua.chrome}
            if isproxy:
                re = requests.get(url,headers=headers,proxies={"https": "http://{}".format(proxy_ip)},timeout=5)
            else:
                re = requests.get(url,headers=headers,timeout=5)

            re = requests.get(url)
            re.encoding="UTF-8"
            re_text = json.loads(re.text)
            curr_price = re_text['data']['current_price']
            if curr_price<=expect_price:
                print("\n-------------- 已达到预期价格，请速抢！ ---------------")
                print("商品名称：",re_text['data']['name'])
                print("商品描述：",re_text['data']['description'])
                print("\n\033[0;32;40m[+]商品期待价格：%d元\033[0m"%(expect_price))
                print("\033[0;32;40m[+]商品当前价格：%d元\033[0m"%(curr_price))
                item_statu = re_text['data']['stock_status']
                if "正在抢购" in item_statu:
                    print("\033[0;32;40m[+]商品当前状态：%s\033[0m"%(item_statu))
                    playsound("./alarm.mp3")
                else:
                    print("\033[0;31;40m[x]商品当前状态：%s\033[0m"%(item_statu))
            else:
                time.sleep(times)
        except Exception as e:
            if "SSLError" in str(e) or "ProxyError" in str(e):
                print("\n\033[0;31;40m[x]代理出错，正在重试...\033[0m\n")
            elif "timed out" in str(e):
                print("\n\033[0;31;40m[x]代理超时，正在重试...\033[0m\n")
            else:
                print("\n\033[0;31;40m%s\033[0m\n"%(str(e)))
            continue
    print("\n\033[0;31;40m[x]商品售空，监控结束...\033[0m\n")
    playsound("./end.mp3")
    return 0



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('id', type=int, default=781395, help="商品id 获取方式：分享商品至QQ，url中id参数的值")
    parser.add_argument('-expect-price', type=int, default=1, help="期待商品价格 默认为1")
    parser.add_argument('-times',type=int,default=10,help="监控时间间隔 默认为5秒/次")
    parser.add_argument('-isproxy', type=int, default=0, help="是否连接代理池 默认为0")
    args = parser.parse_args()
    iqianggou(args.id,args.expect_price,args.times,args.isproxy)

