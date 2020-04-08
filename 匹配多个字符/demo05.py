# 题目1：匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
import re

email = 'hello@163.com'
result = re.match(r'[^@]*', email)

print(result.group())

