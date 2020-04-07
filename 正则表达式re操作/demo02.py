import re

# .的使用
# 匹配单个字符
char = re.match('.', 'M')
print(char.group())

# 匹配一段文字
resultString = re.match("s.ort", "short is long!")

print(resultString.group())
