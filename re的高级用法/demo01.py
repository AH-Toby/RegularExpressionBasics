# match

import re

print(re.match('www', 'www.baidu.com').span())  # 在起始位置匹配
print(re.match('com', 'www.baidu.com'))  # 不在起始位置匹配
