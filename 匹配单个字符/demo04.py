import re

# \s示例
ret1 = re.match('人间大炮\s1级准备', "人间大炮 1级准备")
ret2 = re.match('人间大炮\s2级准备', "人间大炮 2级准备")
ret3 = re.match('人间大炮\s3级准备', "人间大炮 3级准备")
print(ret1.group())
print(ret2.group())
print(ret3.group())
