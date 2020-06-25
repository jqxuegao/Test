import re

# 正则切割

string = 'login/${id}/${id2}'


p1 = re.compile(r'[{](.*?)[}]', re.S)
# findall(匹配规则，匹配字段)
print(re.findall(p1, string))

#

string = 'abe(ac)ad)'

p1 = re.compile(r'[(](.*?)[)]', re.S) #最小匹配
p2 = re.compile(r'[(](.*)[)]', re.S)  #贪婪匹配

print(re.findall(p1, string))
print(re.findall(p2, string))

#

string = 'login/${id}/${id2}'

# p1 = re.compile(r'[{](.*?)[}]', re.S)
# findall(匹配规则，匹配字段)
print(re.findall('(?<=\$\{)\w+(?=\})', string))