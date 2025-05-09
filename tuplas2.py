#pessoa= {'nome':'dave','idade':'19','cidade':'san francisco'}
#print(pessoa['idade'])


estádio={'nome':'morumbi','capacidade':'600000'}


print(estádio.keys())

print(estádio.values())

print(estádio.items())

print(estádio.get('nome','morumbi'))

estádio.update({"capacidade":85000})
print(estádio)
