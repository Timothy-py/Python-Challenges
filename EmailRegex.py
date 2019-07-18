import re

emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')

mo1 = emailRegex.search('adeyeyetimoty33@yahoo.com')

mo2 = emailRegex.search('aaro@teragonltd.com')

mo3 = emailRegex.search('adeyeye@gmail.co')

mo1.group()
mo2.group()
mo3.group()

