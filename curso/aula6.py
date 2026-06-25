# converção de tipos, coarção
# type conversion, typecasting, coercion
# é o ato de converter um tipo de dado em outro tipo de dado
# tipos imutáveis e primitivos: str, int, float, bool
# str -> int, float, bool
print('1' + 1) # TypeError: can only concatenate str (not "int") to str
print(int('1') + 1) # 2, a função int() converte a string '1' em um número inteiro 1
print(float('1') + 1) # 2.0, a função float() converte a string '1' em um número float 1.0
print(bool('1') + 1) # 2, a função bool() converte a string '1' em um valor booleano True, e True é equivalente a 1 em operações aritméticas