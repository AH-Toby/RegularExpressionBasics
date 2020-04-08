# 需求：匹配出<html>hh</html>
import re

htmls = ["<html>hh</html>", "<html>hh</htmlbalabala>"]

for html in htmls:
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", html)
    if ret:
        print("%s是符合要求的html标签" % ret.group())
    else:
        print("%s不是符合要求的html标签"% html)
