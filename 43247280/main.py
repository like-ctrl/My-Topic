# coding=utf-8

# json 清除代码 (for DeBug , don't use it anywhere!)
# DON'T RUN IT!!!
# fl = "here.json"
# with open(fl,"w") as obj:
#     json.dump("0",obj)


import datetime
y = datetime.datetime.now()  #获取当地时间
print(y)  
y = str(y)  #转换为字符串，便于切片
h = y[11:13]  #切片为精确的小时
print(h)

if h[:1] == "0":  # 处理 05 等开头为 0 时间引发的错误
    h = h[1:2]
    print(h)
h = int(h)

#  判断时间
if h <= 10:
    text = "早上好!"
elif h <= 14:
    text = "中午好!"
elif h <= 17:
    text = "下午好!"
else:
    text = "晚上好!"

import json
fl = "here.json"
with open(fl,"r") as obj:
    th = json.load(obj)
    print(th)
with open(fl,"w") as obj:
    th += 1
    print(th)
    json.dump(th,obj)

from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html" , text=text , th = th)

@app.route("/works")
def works():
    return render_template("works.html")

@app.route("/face")
def face():
    return render_template("face.html")

if __name__ == "__main__":
    app.run()