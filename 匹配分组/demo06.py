import re

htmls = ["<html><h1>www.baidu.cn</h1></html>", "<html><h1>www.baidu.cn</h2></html>",
         "<html><h1>www.shouhu.cn</h1></html>"]

for html in htmls:
    # (?P<name>)中间字段(?P=name)
    ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", html)
    if ret:
        print("%s是符合要求的html标签" % ret.group())
    else:
        print("%s不是符合要求的html标签" % html)
