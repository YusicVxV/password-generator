import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '[]{}()*:;/.,_-@&'

allznaki = lower + upper + numbers + symbols
lenght = 16
password = ''.join(random.sample(allznaki, lenght))
print(password)