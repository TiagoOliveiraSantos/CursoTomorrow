numero =int(input('Informe o número: '))
for i in range(1,numero + 1):
 
  print(f'-----Tabuada do {i}-----')
  for j in range(1,11):
    print(f'{i} x {j} = {(i*j)}')