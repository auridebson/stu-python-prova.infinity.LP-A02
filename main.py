# [LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, 
# exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

#----------------------------------------------------------------------------------------------------
# Há uma pequena falha na questão pois entre 80 e 81 é um ponto cedo para o departamento de multas
# então, converti na possibilidade de enviar uma advertência ao infrator.
#----------------------------------------------------------------------------------------------------

def ln(x):
    print("-"*x)

ln(30)
print("O sistema atual coletará a velociade medida \ne decidirá a ação de acordo com o resultado.")
ln(30)
velAtual = float(input("Digite a velocidade do carro: "))

if (velAtual > 80):
    ln(15)
    print("ATENÇÃO:\nMulta aplicada!")
    ln(15)
    kmExtra = velAtual - 80
    vlrMulta = kmExtra * 20
    if (vlrMulta < 20):
        print(f'ATENÇÃO:\nProcure a administração para converter em advertência.')
    else:
        print(f'BOLETO:\nMulta calculada por km excedido:\nTota: R${vlrMulta}')
