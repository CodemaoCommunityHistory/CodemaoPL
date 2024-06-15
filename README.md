# CodemaoPL

批量EDU号操作/注册 解决方案

**~~数字生命，启动！~~**

## 需求

1. 需要安装Python
2. 需要安装 `requests` ，`openpyxl` 库

## 使用

### 社区类（在根目录）

#### 登录

通过编程猫官方的登录API，获取账号的Token

`python3 login.py`

执行后输入Excel表格路径即可，仅支持 **.xlsx** 文件

登录后Token会保存到本地的`tokens.txt`文件内，其他脚本会自动获取Token，请注意安全保存

文件格式请查看下方的 **注意事项**

#### 签订友好协议

> 建议过一下，不过的话，不知道评论的时候会不会有问题

`python3 signature.py`

#### 关注

`python3 follow.py`

#### 点赞＋收藏

`python3 2l.py`

### EDU类（在/edu）

#### 自动注册

`python3 auto.py`

请先打开文件修改Token为自己的，再执行

默认创建100个班级（EDU上限）如果先前已创建则补齐100个班级，最多能创建100x100=10000个账号 / 每个EDU

全部创建后，可以在 https://teacher-edu.codemao.cn/studentManage 导出所有学生信息

学生名字默认为程序内的字典，不需要动

## 注意事项

### 表格文件的格式

​		直接下载的表格可能会有标题，请把他们变成这样的格式，或者查看 `example.xlsx`		

​		也就是没有标题，不要带标题就行，直接就 **账号名-账号-密码**

| {账号名} | {账号} | {密码} |
|:-----:|:----:|:----:|
| {账号名} | {账号} | {密码} |

> 官网下载的可能不是xlsx，记得另存为 .xlsx !

### 如何获取Token?

1. 使用API获取

    在 `/other` 目录下执行 `python3 get_mytoken.py` , 按照提示登录即可



2. 抓包提取请求头

    在请求头中寻找 **Authorization** 所对应的值，**Bearer**后面的**所有内容**（像乱码一样）就是你的Token



## 特别鸣谢

[编程猫API文档](https://api.docs.codemao.work/)

