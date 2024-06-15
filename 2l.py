# @author:Wangs_official
import control as c
import json
import os
import time
if not os.path.exists("tokens.txt"):
    exit("未找到Tokens文件")

tokens = open("tokens.txt", "r").read().split("\n")
print("已加载Token数量：" + str(len(tokens)))

al = 0
zid = input("请输入作品ID : ")
if len(zid) == 0:
    exit("?")

for _ in tokens:
    start_time = time.time()
    al = al + 1
    req = c.call_api(f"nemo/v2/works/{zid}/collection", "{}", _)
    req2 = c.call_api(f"nemo/v2/works/{zid}/like", "{}", _)
    if not req.status_code == 200:
        print(f"   (点赞)第{al}个请求失败 : {req.text}\n----------")
    if not req2.status_code == 200:
        print(f"   (收藏)第{al}个请求失败 : {req2.text}\n----------")
    else:
        ut = time.time() - start_time
        speed = int(60 / ut)
        print(f"\r第{al}个已完成(共{len(tokens)}个) | 速度: {speed} 个/分钟", end="")