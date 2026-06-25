"""
CONSTANTE = "Variaveis" que não mudam, por convenção, são escritas em letras maiúsculas. Exemplo: PI = 3.14
Muitas condições no mesmo if (ruim)
Contagem de complexidade (ruim)
"""

velocidade = 61 #velocidade do carro
local_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local do radar 1
RADAR_RANGE = 1 #alcance do radar

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade > RADAR_1:
    print('Velocidade acima do permitido no radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
    print('Carro multado no radar 1')
