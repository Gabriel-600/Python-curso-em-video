cid = str(input('Em que cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')


#PROCURAR SANTO NO NOME DA CIDADDE errado
cid = str(input('Digite sua cidade: '))
print ('santo, Santo, SANTO' in cid)