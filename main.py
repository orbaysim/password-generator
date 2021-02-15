
letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=["!","^","(",")","-","*","."]

import random

letter_count=int(input("How many letters do you want? "))
number_count=int(input("How many numbers do you want? "))
symbols_count=int(input("How many symbols do you want? "))

password=""

while [letter_count,number_count,symbols_count]>[0,0,0]:
  if random.randint(0,5)>3:
    if letter_count>0:
      password=password+letters[random.randint(0,len(letters)-1)]
      letter_count-=1
  elif random.randint(0,4)>2:
    if number_count>0:
      password=password+str(numbers[random.randint(0,len(numbers)-1)])
      number_count-=1
  else:
    if symbols_count>0:
      password=password+symbols[random.randint(0,len(symbols)-1)]
      symbols_count-=1

print(password)

