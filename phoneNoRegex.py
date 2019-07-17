import re

PhoneNoRegex = re.compile(r'^((\+234\s?90|70|80|81)|(080|070|090|081))-?\d{8}$')

mo = PhoneNoRegex.search('080323742299')
mo1 = PhoneNoRegex.search('08032374229')
mo2 = PhoneNoRegex.search('0813237422')
mo3 = PhoneNoRegex.search('+23432374229')
mo4 = PhoneNoRegex.search('23432374229')
mo5 = PhoneNoRegex.search('323742299')

# mo.group()
# print('********************')
# mo1.group()
# print('********************')
# mo2.group()
# print('********************')
# mo3.group()
# print('********************')
# mo4.group()
# print('********************')
mo5.group()
print('********************')

