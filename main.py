import random
import string

#Набор символов верхнего и нижнего регистров + набор всех цифр + всех знаков препинания
sequence = string.ascii_letters + string.digits + string.punctuation

#Установление пароля длинной в 20 символов
lenght = 20


password = ''.join(random.sample(sequence, lenght))
print(password)

 
