# \w示例
import re


ret1 = re.match('\w人间大炮\w级准备', "a人间大炮1级准备")
ret2 = re.match('\w人间大炮\w级准备', "b人间大炮2级准备")
ret3 = re.match('\w人间大炮\w级准备', "c人间大炮3级准备")
print(ret1.group())
print(ret2.group())
print(ret3.group())
