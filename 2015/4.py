#!/usr/bin/env python3

import hashlib
import re

pattern5: str = r'^00000'
pattern6: str = r'^000000'
key: str = "bgvyzdsv"
postfix: int = 0

while True:
    result = hashlib.md5((key + str(postfix)).encode())
    result: str = result.hexdigest()
    if re.findall(pattern5, result):
        print(f'Hash with 5 zeros {postfix}')
    if re.findall(pattern6, result):
        print(f'Hash with 6 zeros {postfix}')
    postfix += 1
