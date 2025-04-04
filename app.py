print('olá mundo')
print('vamo são paulo')
print('jordan goat')

caixa= 'mahomes'
print(caixa)
nome= 'Pedro miguel'
idade=16
altura=1.78
estudante= True
print(nome,idade,altura,estudante)

mensagem='até mais tarde'
print(mensagem.strip())
print(mensagem.upper())
print(mensagem.lower())

#endereco=input('onde voce mora? ' )
#print(f'moro no {endereco}, atras do  shopping')

from datetime import datetime
nome=input('qual é o seu nome? ')
agora=datetime.now()
hora_atual=agora.strftime('%H:%M')
print(f'olá! {nome} agora são {hora_atual}')





