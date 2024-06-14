# @author:Wangs_official
# 先过签订友好协议再进行批量评论什么的
import control as c
import json
import os
import time

if not os.path.exists("tokens.txt"):
    exit("未找到Tokens文件")

tokens = open("tokens.txt", "r").read().split("\n")
print("已加载Token数量：" + str(len(tokens)))

al = 0

for _ in tokens:
    start_time = time.time()
    al = al + 1
    req = c.call_api("nemo/v3/user/level/signature", "{}", _)
    if not req.status_code == 200:
        print(f"   第{al}个请求失败 : {req.text}\n----------")
    else:
        ut = time.time() - start_time
        speed = int(60 / ut)
        print(f"\r第{al}个已完成(共{len(tokens)}个) | 速度: {speed} 个/分钟", end="")

print("\r请求完毕",end="")
