from math import fabs 
input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.readlines() # Читаем в другую переменную содержимое всего файла
a=str(data[0])
b=str(data[1])
a=a.split()
b=b.split()
x1=int(a[0])
y1=int(a[1])
r1=int(a[2])
x2=int(b[0])
y2=int(b[1])
r2=int(b[2])
d=(x1-x2)**2+(y1-y2)**2
if (r1-r2)**2<=d<=(r1+r2)**2:
    output_data = open('output.txt','w')
    output_data.write('YES')
else:
    output_data = open('output.txt','w')
    output_data.write('NO')
input_data.close()
output_data.close()  

