input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
n=int(data)
n=2**n
output_data = open('output.txt','w')
output_data.write(str(n))
input_data.close()
output_data.close()