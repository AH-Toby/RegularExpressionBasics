import re

# 匹配以life开头的语句

result = re.match("life", "life is sort,you need python!")

print(result.group())
