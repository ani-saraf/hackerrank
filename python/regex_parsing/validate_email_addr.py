import re
from email.utils import *

n = int(input())
pattern = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'

for _ in range(n):
    email = parseaddr(input())
    if re.search(pattern, email[1], re.I):
        print(formataddr(email))