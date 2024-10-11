input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
n=data
k=0
S=0
for i in range(0,len(n)):
    if n[i] == '0':
        k+=1
        if k>S:
            S+=1
    else:
        k=0
output_data = open('output.txt','w')
output_data.write(str(S))
input_data.close()
output_data.close()