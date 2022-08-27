# challenge = string in içinde substringden kaç tane var buldur
import re

string = input("enter your text")
substring = input("please enter the pattern")

matches = re.findall(substring , string)

print (len(matches))

# normalde karmaşık bir çözümü var ama re modülü ile 4 satırda yapılabiliyor