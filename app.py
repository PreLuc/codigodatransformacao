print('ola mundo')
print('eu era bom')
print('salve zona sul')

caixa='celular'

print(caixa)

caixa='bike a sla'

print(caixa)

caixa='teclado'

print(caixa)

nome= 'pedro'
idade=  16
altura= 1.79
estudante= True
print(nome,idade,altura,estudante)

mensagem= 'estou ficando inteligente'
print(mensagem.strip())
print(mensagem.upper())
print(mensagem.lower())

name=input('insira o seu nome!')
print(f'ola {nome}, seja muito bem vindo ao meu site')

from datetime import datetime

nome= input('qual e o seu nome')
agora= datetime.now()
hora_atual=agora.strftime('%H:%M')
print(f'ola, {nome}! Agora sao {hora_atual}')

