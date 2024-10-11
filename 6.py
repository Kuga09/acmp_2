input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
data=data.split()
a=int(data[0])
b=int(data[1])
a1=a
b1=b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
LCM=(a1*b1)/(a+b)
output_data = open('output.txt','w')
output_data.write(str(int(LCM)))
input_data.close()
output_data.close()  