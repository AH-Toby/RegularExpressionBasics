# 不是以4、7结尾的手机号码(11位)
import re

tels = ["13100001234", "18912344321", "10086", "18800007777"]

for tel in tels:
    ret = re.match(r'1\d{9}[0-35-68-9]', tel)
    if ret:
        print("%s符合不是以4、7结尾的手机号码要求" % ret.group())
    else:
        print("%s不符合" % tel)
