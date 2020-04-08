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
## 1.&#124;示例
```
# 需求：匹配出0-100之间的数字
import re

ret = re.match("[1-9]?\d","8")
print(ret.group())  # 8

ret = re.match("[1-9]?\d","78")
print(ret.group())  # 78

# 不正确的情况
ret = re.match("[1-9]?\d","08")
print(ret.group())  # 0

# 修正之后的
ret = re.match("[1-9]?\d$","08")
if ret:
    print(ret.group())
else:
    print("不在0-100之间")

# 添加|
ret = re.match("[1-9]?\d$|100","8")
print(ret.group())  # 8

ret = re.match("[1-9]?\d$|100","78")
print(ret.group())  # 78

ret = re.match("[1-9]?\d$|100","08")
# print(ret.group())  # 不是0-100之间

ret = re.match("[1-9]?\d$|100","100")
print(ret.group())  # 100
```
## 2.()示例
```
# 需求：匹配出163、126、qq邮箱
import re

ret = re.match("\w{4,20}@163\.com", "test@163.com")
print(ret.group())  # test@163.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret.group())  # test@126.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
print(ret.group())  # test@qq.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
if ret:
    print(ret.group())
else:
    print("不是163、126、qq邮箱")  # 不是163、126、qq邮箱
```
```
# 不是以4、7结尾的手机号码(11位)
import re

tels = ["13100001234", "18912344321", "10086", "18800007777"]

for tel in tels:
    ret = re.match(r'1\d{9}[0-35-68-9]', tel)
    if ret:
        print("%s符合不是以4、7结尾的手机号码要求" % ret.group())
    else:
        print("%s不符合" % tel)
```
```
# 提取区号和电话号码
import re
phoneNum = "010-12345678"
# [^-]*匹配以-开头的所有字符串
ret = re.match('([^-]*)-(\d+)',phoneNum)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
```
## 3.\示例
```
# 需求：匹配出<html>hh</html>
import re

htmls = ["<html>hh</html>", "<html>hh</htmlbalabala>"]

for html in htmls:
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", html)
    if ret:
        print("%s是符合要求的html标签" % ret.group())
    else:
        print("%s不是符合要求的html标签"% html)
```

## 4.(?P<name>) (?P=name)示例
```
import re

htmls = ["<html><h1>www.baidu.cn</h1></html>", "<html><h1>www.baidu.cn</h2></html>",
         "<html><h1>www.shouhu.cn</h1></html>"]

for html in htmls:
    # (?P<name>)中间字段(?P=name)
    ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", html)
    if ret:
        print("%s是符合要求的html标签" % ret.group())
    else:
        print("%s不是符合要求的html标签" % html)
```
```
例：身份证 1102231990xxxxxxxx

import re
s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())
此分组取出结果为：

{'province': '110', 'city': '223', 'born_year': '1990'}
```
# re模块的高级用法
## match
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。\
函数语法：\
`re.match(pattern, string, flags=0)`
函数参数说明：

|参数|	描述|
|:---:|:---:|
|pattern|匹配的正则表达式|
|string|要匹配的字符串。|
|flags|标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。|

匹配成功re.match方法返回一个匹配的对象，否则返回None。

我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。

|匹配对象方法|	描述|
|:---:|:---:|
|group(num=0)|	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。|
|groups()|	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。|
### 示例1：
```
import re

print(re.match('www', 'www.baidu.com').span())  # 在起始位置匹配
print(re.match('com', 'www.baidu.com'))  # 不在起始位置匹配
```
### 示例2：
```
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")
```

## search
re.search 扫描整个字符串并返回第一个成功的匹配。\
函数语法：\
`re.search(pattern, string, flags=0)`

函数参数说明：

|参数|	描述|
|:---:|:---:|
|pattern|	匹配的正则表达式|
|string|	要匹配的字符串。|
|flags|	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。|

匹配成功re.search方法返回一个匹配的对象，否则返回None。\
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。

|匹配对象方法|	描述|
|:---:|:---:|
|group(num=0)|	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。|
|groups()|	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。|

### 示例1：
```
import re

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

```
### 示例2：
```
import re

line = "Cats are smarter than dogs";

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")
```
### 小练习
```
# 需求：匹配出文章阅读的次数
import re

sting1 = "阅读次数为 9999"
result = re.search(r"\d+", sting1)
print(result.group())
```

### re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

## findall
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

**注意**： match 和 search 是匹配一次 findall 匹配所有。\
语法格式为：\
`findall(string[, pos[, endpos]])`

|参数|参数描述|
|:---:|:---:|
|string|  待匹配的字符串。|
|pos| 可选参数，指定字符串的起始位置，默认为 0。|
|endpos|  可选参数，指定字符串的结束位置，默认为字符串的长度。|
### 示例1：
```
import re

pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)
```
### 小练习
```
# 需求：统计出python、c、c++相应文章阅读的次数
import re

stingVlue = "python = 9999, c = 7890, c++ = 12345"
ret = re.findall(r"\d+", stingVlue)
print(ret)
```
## finditer
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。\
语法格式：\
`re.finditer(pattern, string, flags=0)`\
参数：

|参数|	描述|
|:---:|:---:|
|pattern|	匹配的正则表达式|
|string|	要匹配的字符串。|
|flags|	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。|
### 示例1：
```
import re

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())
```
### 小练习
```
# 需求：统计出python、c、c++相应文章阅读的次数
import re

stingVlue = "python = 9999, c = 7890, c++ = 12345"
rets = re.finditer(r"\d+", stingVlue)
for ret in rets:
    print(ret.group())
```
## sub 将匹配到的数据进行替换
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。\
语法：\
`re.sub(pattern, repl, string, count=0, flags=0)`\
参数：

|参数|参数描述|
|:---:|:---:|
|pattern|正则中的模式字符串。|
|repl|替换的字符串，也可为一个函数。|
|string|要被查找替换的原始字符串。|
|count|模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。|

### 示例1：
```
import re

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)
```
### 小练习：
```
import re


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r"\d+", add, "python = 997")
print(ret)

ret = re.sub(r"\d+", add, "python = 99")
print(ret)
```
## split 根据匹配进行切割字符串，并返回一个列表
split 方法按照能够匹配的子串将字符串分割后返回列表\
语法\
`re.split(pattern, string[, maxsplit=0, flags=0])`
参数：

|参数|	描述|
|:---:|:---:|
|pattern|	匹配的正则表达式|
|string|	要匹配的字符串。|
|maxsplit|	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。|
|flags|	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。|
### 示例1：
```
import re
ret = re.split('\W+', 'runoob, runoob, runoob.')
print(ret)
```
### 小练习：
```
import re

ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
print(ret)
```
## compile  
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。\
语法格式为：
`re.compile(pattern[, flags])`\
参数：

|参数|参数描述|
|:---:|:---:|
|pattern|一个字符串形式的正则表达式|
|flags|可选，表示匹配模式，比如忽略大小写，多行模式等|
flags参数：
- re.I 忽略大小写
- re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
- re.M 多行模式
- re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
- re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
- re.X 为了增加可读性，忽略空格和 # 后面的注释

在上面，当匹配成功时返回一个 Match 对象，其中：

|方法|方法描述|
|:----:|:----:|
|group([group1,…])| 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；|
|start([group]) |方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；|
|end([group]) |方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；|
|span([group]) |方法返回 (start(group), end(group))。|

### 示例1：
```
import re

pattern = re.compile(r'\d+')
ret = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配)
print(ret.group())
```
# 贪婪和非贪婪
Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；

非贪婪则相反，总是尝试匹配尽可能少的字符。

在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。
## 示例1：
```
>>> s="This is a number 234-235-22-423"
>>> r=re.match(".+(\d+-\d+-\d+-\d+)",s)
>>> r.group(1)
'4-235-22-423'
>>> r=re.match(".+?(\d+-\d+-\d+-\d+)",s)
>>> r.group(1)
'234-235-22-423'
>>>
```
正则表达式模式中使用到通配字，那它在从左到右的顺序求值时，会尽量“抓取”满足匹配最长字符串，在我们上面的例子里面，“.+”会从字符串的启始处抓取满足模式的最长字符，其中包括我们想得到的第一个整型字段的中的大部分，“\d+”只需一位字符就可以匹配，所以它匹配了数字“4”，而“.+”则匹配了从字符串起始到这个第一位数字4之前的所有字符。

**解决方式：非贪婪操作符“？”，这个操作符可以用在"*","+","?"的后面，要求正则匹配的越少越好。**
## 示例2：
```
>>> re.match(r"aa(\d+)","aa2343ddd").group(1)
'2343'
>>> re.match(r"aa(\d+?)","aa2343ddd").group(1)
'2'
>>> re.match(r"aa(\d+)ddd","aa2343ddd").group(1)
'2343'
>>> re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
'2343'
>>>
```
# r的作用
说明

Python中字符串前面加上 r 表示原生字符串，

与大多数编程语言相同，正则表达式里使用"\"作为转义字符，这就可能造成反斜杠困扰。假如你需要匹配文本中的字符"\"，那么使用编程语言表示的正则表达式里将需要4个反斜杠"\\"：前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。

Python里的原生字符串很好地解决了这个问题，有了原生字符串，你再也不用担心是不是漏写了反斜杠，写出来的表达式也更直观。
## 示例1：
```
>>> mm = "c:\\a\\b\\c"
>>> mm
'c:\\a\\b\\c'
>>> print(mm)
c:\a\b\c
>>> re.match("c:\\\\",mm).group()
'c:\\'
>>> ret = re.match("c:\\\\",mm).group()
>>> print(ret)
c:\
>>> ret = re.match("c:\\\\a",mm).group()
>>> print(ret)
c:\a
>>> ret = re.match(r"c:\\a",mm).group()
>>> print(ret)
c:\a
>>> ret = re.match(r"c:\a",mm).group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
>>>
```

# 正则表达式修饰符 - 可选标志
正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：

|修饰符|	描述|
|:---:|:---:|
|re.I|	使匹配对大小写不敏感|
|re.L|	做本地化识别（locale-aware）匹配|
|re.M|	多行匹配，影响 ^ 和 $|
|re.S|	使 . 匹配包括换行在内的所有字符|
|re.U|	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.|
|re.X|	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。|
