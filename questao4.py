'''
maria fernanda alves mendes

'''
lista=list()


while True:
    a=int(input('digite um numero:'))
    lista.append(a)

    resp=input('deseja continuar? (s/n)')
    if resp == 'n' :
            break

    
if 5 in lista:
    print('esta na lista')
else:
    print('Não está na lista')
            
print(lista)
print('quantidades de numero ',len(lista))
