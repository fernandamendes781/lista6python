lista= list()
for x in range (5):
    numero = int(input('digite um numero:'))


    #tamanha da lista len 
    if len (lista)==0 or  lista(-1)< numero:
        lista.append(numero)
        continue

        
        #-1 o ultimo numero da lista
    
    pos= 0
    while numero > lista[pos]:
        pos=pos+1
    lista.insert(pos,numero)
print(lista)
    
    




    
