import re

pattern = re.compile(r"([a-zA-Z]).([a])")
string = 'search this search inside of this text please'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
# print(a.span())
# print(a.start())
# print(a.end())
print(a.group())
