input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.readlines() # Читаем в другую переменную содержимое всего файла
a=int(data[0])
b=int(data[1])
if a<b:
    result='<'
elif a>b:
    result='>'
else:
    result='='
output_data = open('output.txt','w')
output_data.write(result)
input_data.close()
output_data.close()