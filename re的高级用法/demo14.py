import re

pattern = re.compile(r'\d+')
ret = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配)
print(ret.group())
