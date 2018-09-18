#!/usr/bin/python
import re

phone = "602-343-8747"

code_find = re. findall('^\d\d\d',phone)
print "The area code is:", code_find[0]


