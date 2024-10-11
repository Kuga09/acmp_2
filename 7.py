input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
N=int(data)
fact_N=1
for i in range(2,N+1):
    fact_N=fact_N*i
output_data = open('output.txt','w')
output_data.write(str(fact_N))
input_data.close()
output_data.close()  
