'''
questao 7
maria fernanda alves mendes
'''
Qp=0
peso=[]
nome=[]
while True:
    Qp=1+Qp
    n= input('digite seu nome:')
    p= int(input('digite seu peso:'))
    nome.append(n)
    peso.append(p)

    resposta = input('deseja sair? (s/n)')
    if resposta == 's':
        break
    
maxx =max(peso)
posiçao = peso.index(maxx)

print('quantidade de pessoas',Qp)
print('peso maximo:',maxx)
print('nome ', nome[posiçao])

minx = min(peso)
posiçao = peso.index(minx)

print('peso minimo:' ,minx)
print('nome:',nome[posiçao])

mediana =(maxx - minx) / 2

pessoas_mais_leves =[]
pessoas_mais_pesadas =[]
cont = 0
for n in peso:
    if n < mediana:
         pessoas_mais_leves.append([nome[cont],n])
    else:
         pessoas_mais_pesadas.append([nome[cont],n])
    cont+=1
print(pessoas_mais_leves)
print(pessoas_mais_pesadas)
    
     
    





           
 






