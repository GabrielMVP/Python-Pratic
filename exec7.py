verdadeiro = 'True'
falso = 'False'

verdadeiro_text = verdadeiro.lower() == 'true'
falso_text = falso.lower() == 'true'

pergunta = input("Escolha uma das opções (True ou False): ").lower()
resposta = pergunta == 'true'

if verdadeiro_text and resposta:
    print("Ambos são VERDADEIRO.")
elif falso_text and not resposta:
    print("Ambos são FALSO.")
else:
    print("Um é VERDADEIRO e o outro é FALSO.")
