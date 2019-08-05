import os, re

filepath = r'C:\Users\D SCIPHER\Desktop\Python Challenges\randomQuizGenerator.py'

subRegex = re.compile(r'(.*)?capitals(.*)?')

randomQuizGeneratorFile = open(filepath, 'r')
NewRandomQuizGeneratorFile = open(r'C:\Users\D SCIPHER\Desktop\Python Challenges\NewrandomQuizGenerator.py', 'w')

copyrandomQuizGeneratorFile = randomQuizGeneratorFile.read()

newSubFile = subRegex.sub('states&capitals', copyrandomQuizGeneratorFile)

NewRandomQuizGeneratorFile.write(newSubFile)



randomQuizGeneratorFile.close()
NewRandomQuizGeneratorFile.close()
