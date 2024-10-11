input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
n=int(data)
n_3=0
if n==1:
    pass
elif n==2:
    pass
elif n==4:
    pass 
else:
    while n > 4 or n==3:
        n-=3
        n_3+=1
if n==4:
    n=4*3**n_3
if n==2:
    n=2*3**n_3
if n==0:
    n=3**n_3
output_data = open('output.txt','w')
output_data.write(str(n))
input_data.close()
output_data.close()

