# 正则表达式
正则表达式(Regular Expression)是一种文本模式，包括普通字符（例如，a 到 z 之间的字母）和特殊字符（称为"元字符"）。
正则表达式使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串。

# re模块操作
## 1. re模块的使用过程
```
    #coding=utf-8

    # 导入re模块
    import re

    # 使用match方法进行匹配操作
    result = re.match(正则表达式,要匹配的字符串)

    # 如果上一步匹配到数据的话，可以使用group方法来提取数据
    result.group()
```
## 2. re模块示例
```
import re

# 匹配以life开头的语句

result = re.match("life", "life is sort,you need python!")

print(result.group())

```
## 3. 说明
- re.match() 能够匹配出以xxx开头的字符串

# 匹配单个字符
| 字符 | 功能 |
|:---:|:---:|
|  .  |匹配任意1个字符（除了\n）|
| []  |匹配[ ]中列举的字符|
| \d  |匹配数字，即0-9|
| \D  |	匹配非数字，即不是数字|
| \s  |	匹配空白，即 空格，tab键|
| \S  |	匹配非空白|
| \w  |	匹配单词字符，即a-z、A-Z、0-9、_|
| \W  |	匹配非单词字符|

## 1: .示例
```
import re

# .的使用
# 匹配单个字符
char = re.match('.', 'M')
print(char.group())

# 匹配一段文字
resultString = re.match("s.ort", "short is long!")

print(resultString.group())
```
## 2: []示例
```
import re

# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h", "hello Python")
print(ret.group())

# 如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match("H", "Hello Python")
print(ret.group())

# 大小写h都可以的情况
ret = re.match("[hH]", "hello Python")
print(ret.group())
ret = re.match("[hH]", "Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python", "Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]Hello Python", "7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]Hello Python", "7Hello Python")
print(ret.group())

# 匹配0到3，5到9这个区间的数字
ret = re.match("[0-35-9]Hello Python", "7Hello Python")
print(ret.group())

# 下面这个正则不能够匹配到数字4，因此ret为None
ret = re.match("[0-35-9]Hello Python", "4Hello Python")
# print(ret.group())
```
## 3: \d示例
```
import re

# 普通的匹配方式
ret = re.match("人间大炮1级", "人间大炮1级准备")
print(ret.group())

ret = re.match("人间大炮2级", "人间大炮2级准备")
print(ret.group())

ret = re.match("人间大炮3级", "人间大炮3级准备")
print(ret.group())

# 使用\d进行匹配
ret = re.match("人间大炮\d级", "人间大炮1级准备")
print(ret.group())

ret = re.match("人间大炮\d级", "人间大炮2级准备")
print(ret.group())

ret = re.match("人间大炮\d级", "人间大炮3级准备")
print(ret.group())
```
## 4: \D示例
```
import re

ret1 = re.match('人间大\D1级准备', "人间大炮1级准备")
ret2 = re.match('人间大\D2级准备', "人间大炮2级准备")
ret3 = re.match('人间大\D3级准备', "人间大炮3级准备")
print(ret1.group())
print(ret2.group())
print(ret3.group())
```
## 5: \s示例
```
import re

# \s示例
ret1 = re.match('人间大炮\s1级准备', "人间大炮 1级准备")
ret2 = re.match('人间大炮\s2级准备', "人间大炮 2级准备")
ret3 = re.match('人间大炮\s3级准备', "人间大炮 3级准备")
print(ret1.group())
print(ret2.group())
print(ret3.group())
```
## 6: \S示例
```
import re

# \S示例
ret1 = re.match('\S间大炮 1级准备', "人间大炮 1级准备")
ret2 = re.match('\S间大炮 2级准备', "人间大炮 2级准备")
ret3 = re.match('\S间大炮 3级准备', "人间大炮 3级准备")
print(ret1.group())
print(ret2.group())
print(ret3.group())
```
## 7: \w示例
```
import re
ret1 = re.match('\w人间大炮\w级准备', "a人间大炮1级准备")
ret2 = re.match('\w人间大炮\w级准备', "b人间大炮2级准备")
ret3 = re.match('\w人间大炮\w级准备', "c人间大炮3级准备")
print(ret1.group())
print(ret2.group())
print(ret3.group())
```
## 8: \W示例
```
import re

ret1 = re.match('\W人', "！人间大炮1级准备")
ret2 = re.match('\W人', "@人间大炮2级准备")
ret3 = re.match('\W人', "#人间大炮3级准备")
print(ret1.group())
print(ret2.group())
print(ret3.group())
```
# 匹配多个字符
|字符|功能|
|:---:|:---:|
|*|	匹配前一个字符出现0次或者无限次，即可有可无|
|+|	匹配前一个字符出现1次或者无限次，即至少有1次|
|?|	匹配前一个字符出现1次或者0次，即要么有1次，要么没有|
|{m}|	匹配前一个字符出现m次|
|{m,n}|	匹配前一个字符出现从m到n次|
## 1.*示例
```
import re

ret = re.match("[A-Z][a-z]*","M")
print(ret.group())

ret = re.match("[A-Z][a-z]*","MnnM")
print(ret.group())

ret = re.match("[A-Z][a-z]*","Aabcdef")
print(ret.group())
```
## 2.+示例
```
import re

names = ["name1", "_name", "2_name", "__name__"]

for name in names:
    ret = re.match("[a-zA-Z_]+[\w]*",name)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s 非法" % name)
```
## 3.?示例
```
import re

ret = re.match("[1-9]?[0-9]", "7")
print(ret.group())

ret = re.match("[1-9]?\d", "33")
print(ret.group())

ret = re.match("[1-9]?\d", "09")
print(ret.group())
```
## 4.{m}示例{m,n}示例 
```
import re

ret = re.match("[a-zA-Z0-9_]{6}","12a3g45678")
print(ret.group())

ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
print(ret.group())
```
## 练习：
**题目1：匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com**
```
import re

email = 'hello@163.com'
result = re.match(r'.{4,20}@', email)

print(result.group())
```
# 匹配开头结尾
|字符|	功能|
|:---:|:---:|
|^|	匹配字符串开头|
|$|	匹配字符串结尾|
## 示例
```
# 需求：匹配163.com的邮箱地址
import re

email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]

for email in email_list:
    ret = re.match("[\w]{4,20}@163\.com$", email)
    if ret:
        print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
    else:
        print("%s 不符合要求" % email)
```
# 匹配分组
|字符|	功能|
|:---:|:---:|
| &#124; |	匹配左右任意一个表达式|
|(ab)|	将括号中字符作为一个分组|
|\num|	引用分组num匹配到的字符串|
|(?P<name>)|	分组起别名|
|(?P=name)|	引用别名为name分组匹配到的字符串|


