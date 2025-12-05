def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *=2
        pos += 1
    
valores = [3, 6, 9, 12, 15]
dobra(valores)
print(valores)





def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(F' SOmando os valores {valores} temos {s}')

soma(5, 7)
soma(10,50)