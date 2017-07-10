import re
a=input()
try:
    assert re.search(r"^[0-9]{6}$",a)
    temp=re.findall(r"(\d)(?=\d\1)",a)
    assert not len(temp)>1
except:
    print(False)
else:
    print(True)