# 需求：匹配出文章阅读的次数
import re

sting1 = "阅读次数为 9999"
result = re.search(r"\d+", sting1)
print(result.group())