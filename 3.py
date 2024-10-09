input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
data=data.split()
a=int(data[0])
b=int(data[1])
c=int(data[2])
if a > b:
    if a > c:
        max=a
    else:
        max=c
else:
 if b > c:
   max=b
 else:
  max=c
output_data = open('output.txt','w')
output_data.write(str(max))
input_data.close()
output_data.close()