# 需求：统计出python、c、c++相应文章阅读的次数
import re

stingVlue = "python = 9999, c = 7890, c++ = 12345"
rets = re.finditer(r"\d+", stingVlue)
for ret in rets:
    print(ret.group())
