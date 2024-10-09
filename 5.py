input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
data=data.split()
a=int(data[0])
b=int(data[1])
c=int(data[2])
d=int(data[3])
x3=' '
x1=' '
x2=' '
for i in range(-100,101):
    if (a*i**3+b*i**2+c*i+d)==0:
        x1=i
        for v in range(i+1,101):
            if (a*v**3+b*v**2+c*v+d)==0:
                x2=v
                for w in range(v+1,101):
                    if (a*w**3+b*w**2+c*w+d)==0:
                        x3=w
                        break
                break
        break
output_data = open('output.txt','w')
if x3 != ' ': 
    output_data.write(str(x1)+' '+str(x2)+' '+str(x3))
elif x2 != ' ':
    output_data.write(str(x1)+' '+str(x2))
else:
    output_data.write(str(x1))
input_data.close()
output_data.close()

