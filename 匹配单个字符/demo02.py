import re

# 普通的匹配方式
ret = re.match("人间大炮1级", "人间大炮1级准备")
print(ret.group())

ret = re.match("人间大炮2级", "人间大炮2级准备")
print(ret.group())

ret = re.match("人间大炮3级", "人间大炮3级准备")
print(ret.group())

# 使用\d进行匹配
ret = re.match("人间大炮\d级", "人间大炮1级准备")
print(ret.group())

ret = re.match("人间大炮\d级", "人间大炮2级准备")
print(ret.group())

ret = re.match("人间大炮\d级", "人间大炮3级准备")
print(ret.group())
