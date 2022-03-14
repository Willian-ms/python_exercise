item = input('Produto: ')
qtde = float(input('Quantidade Comprada: '))
vlr_un = float(input('Valor unitário: '))
vlr_total = qtde * vlr_un
desc = float(input('Desconto: '))
vlr_desc = vlr_total * (desc/100)

vlr_final = vlr_total - vlr_desc

print(item, vlr_final)
