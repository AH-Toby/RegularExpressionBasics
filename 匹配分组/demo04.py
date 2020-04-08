# 提取区号和电话号码
import re
phoneNum = "010-12345678"
# [^-]*匹配以-开头的所有字符串
ret = re.match('([^-]*)-(\d+)',phoneNum)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
