input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
a=float(data)
if a != 5:
 a1=int(a/10)
 b=a1*(a1+1)
 s=str(b)+'25'
else:
 s='25'
output_data = open('output.txt','w')
output_data.write(str(s))
input_data.close()
output_data.close()