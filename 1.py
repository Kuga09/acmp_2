input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
a=int(data)
s=0
if a < 0:
 for i in range(a,2):
  s=s+i
elif a > 0:
 for i in range(1,a+1):
  s=s+i
else:
 s=1
output_data = open('output.txt','w')
output_data.write(str(s))
input_data.close()
output_data.close()