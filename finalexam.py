'''Write a User Defined Function (UDF) for generating 20 words for the given word "PAKISTAN". Now generate 7 letter, and 6 letter words.
ii. Such as 7 Letter words you can make with PAKISTAN
pastina patinas pinatas taipans
iii. 6 Letter words you can make with PAKISTAN
Atkins akitas askant paints paisan patina patins pinata pintas ptisan taipan takins tankas'''

import random

word='pakistan'
word_lst=[]
for letter in word:
    word_lst.append(letter)

print("WORD =        PAKISTAN")
print('\n')
six_letter_list=[]
for x in range(10):
    six_letter = random.sample(word_lst, 6)
    six_letter_join=' '.join(six_letter)
    six_letter_list.append(six_letter_join)

seven_letter_list=[]
for y in range(10):
    seven_letter= random.sample(word_lst,7)
    seven_letter_join=' '.join(seven_letter)
    seven_letter_list.append(seven_letter_join)

counter_1=1
for yyy in six_letter_list:
    print('{}: {:<15}'.format(str(counter_1)+") Six letter random sample",yyy.upper()))
    counter_1+=1
counter_2=1

print('\n')
for xxx in seven_letter_list:
    print('{}- {:<30}'.format(str(counter_2)+") Seven letter random sample",xxx.upper()))
    counter_2+=1


