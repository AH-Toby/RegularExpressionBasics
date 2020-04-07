import re

# \D示例
ret1 = re.match('人间大\D1级准备', "人间大炮1级准备")
ret2 = re.match('人间大\D2级准备', "人间大炮2级准备")
ret3 = re.match('人间大\D3级准备', "人间大炮3级准备")
print(ret1.group())
print(ret2.group())
print(ret3.group())
