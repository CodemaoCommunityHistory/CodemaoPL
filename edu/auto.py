# @author:Wangs_official
import json
import random
import time

try:
    import requests
except ImportError:
    exit("请先 pip3 install requests")

# 请在此处填写Token 如何获取请查看README中的注意事项
token = "eyJraWQiOiIwZTBhOTFlOS03MDM3LTQ0ZTYtOWYwZS1lM2QyMWZlNDkwNzkiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoiV0VCIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjE0NTgyMjcxMDMiLCJhdGhfdHlwIjoxLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJhdGhfdmVyIjoiMS4wLjAiLCJleHAiOjE3MTg0NTk3MzgsImlhdCI6MTcxODQ1MjUzOCwianRpIjoiQUFBQmtCdkF6UU5LMUVuYXVCWngyRXdkR0NPR0ljVDQifQ.TCjwj1u67HuZvMm5ZtPmuolbMSUK-H38XFeOLxDWkWyHk7QrbQ6B5-0tG9UdLE6Oxk1ywkW1gk9V1__DhFNCNhY0ReuPwq5-Cl2cMl723TbLmD-cIErZ6-sIAUU--9L-HdV9vvTfGweXjI3P0qIbxyq682Tp7vjnHz48YfVyx5UYXKbUlBOhZz2exGg7NCkY_wcXymO-0ledbaSJoRBGLRXnn52OwXh2GGeyNA3c3MqOmZCqKwTRLs06VXt7sUrjyw5y3qvzozgqPs6fNWT89t88ka-6jNG6ydponFgOtA54GbXC2FP7r5XgsY5cqgEzXFaeZoCq6LoQspg3KoLl4w"
print("班级名将为随机十二位字母")

edu_createclass_url = "https://eduzone.codemao.cn/edu/zone/class"
header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Authorization": f"Bearer {token}"
}

all_cls = requests.get(f"https://eduzone.codemao.cn/edu/zone/classes?page=1&TIME={int(time.time())}", headers=header)
if all_cls.status_code == 200:
    all_cls = json.loads(all_cls.text).get("total")
    willcreate_cls = 400 - all_cls
    print(f"将创建{willcreate_cls}个班级 | 共{all_cls}个")
else:
    exit(f"请求失败：{str(all_cls.text)}")

for _ in range(willcreate_cls):
    li = []
    for i in range(12):
        temp = random.randrange(65, 91)
        c = chr(temp)
        li.append(c)
    result = "".join(li)
    wc_name = f"{result}"

    create_class_requests = requests.post(edu_createclass_url, data=json.dumps({"name": wc_name}), headers=header)
    if create_class_requests.status_code == 200:
        id = json.loads(create_class_requests.text).get("id")
        print(f"班级{result}创建成功，ID:{id}")
    else:
        exit(f"请求失败：{str(all_cls.text)}")

    stud_names = json.dumps({"student_names": ["vlokud", "mgstop", "waidtk", "ruabon", "ncxjsb", "apgtxw", "sqnpfx",
                                               "qvxpgr", "yihsdm", "vzgsub", "fxywlt", "smqwvt", "qdrjoe", "rohgzt",
                                               "fpzuvd", "zfcuhy", "kfmlsd", "uxdwsc", "qyvkle", "vstunq", "pqbcjx",
                                               "hcxfyd", "caewzx", "obaxfu", "qfobkc", "inrdqg", "ftizlb", "jahdoz",
                                               "himayz", "fdrjnv", "lzjxpd", "lzqguo", "zvywpa", "batmqp", "vdtgzf",
                                               "qihpke", "lgdtxn", "mevsfn", "gkpzth", "naxtby", "oejtmv", "vpwbga",
                                               "twfpav", "mabxio", "zbhyoc", "xgfshv", "zumfnp", "tmajfv", "qtwzma",
                                               "fozhjb", "sgaouk", "odkxzy", "hkexpl", "byuzpc", "vjlxsh", "gdczwr",
                                               "urhtav", "txyjrc", "oalhkz", "yfkxbg", "mliqdx", "osqxck", "adbtro",
                                               "qdzfeb", "ldjvuw", "glhkns", "flevyk", "lrkxta", "lamjey", "fphkcr",
                                               "hxolyc", "euvdmh", "vpdkue", "bqonci", "fmibrj", "zfvjcm", "efhyvj",
                                               "ljguwc", "ckamsg", "hwlned", "utzxer", "mtdnwy", "xitflg", "xgdofl",
                                               "gvirnt", "zvbkos", "gvcjhi", "wqceok", "lvhnto", "caurnj", "xhwnfl",
                                               "qeykzn", "tkefna", "hbamgv", "sinrpq", "xponme", "zpwquc", "hebomj",
                                               "bzsxlp", "mjcotf"]})
    create_class_stud = requests.post(f"https://eduzone.codemao.cn/edu/zone/class/{id}/students", data=stud_names,
                                      headers=header)
    if create_class_stud.status_code == 200:
        pass
    else:
        exit(f"请求失败：{str(create_class_stud.text)}")
