input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
a=int(data)
b=bin(a)
n=0
for i in range(1,len(b)):
    if b[i]=='1':
        n+=1
output_data = open('output.txt','w')
output_data.write(str(n))
input_data.close()
output_data.close() 