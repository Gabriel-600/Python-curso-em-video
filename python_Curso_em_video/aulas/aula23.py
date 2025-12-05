try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite um numero: '))
    res = a / b

except (ValueError, TypeError):
    print('Tivemos problemas com os tipos de dados!')

except ZeroDivisionError:
    print('Não é possível dividir por zero!')

except Exception as erro:
    print(f'Infelizmente tivemos um problema! {erro.__class__}')

else:
    print(f'O resultado é {res}')

finally:
    print('Volte sempre!')