#ALGUMAS HABILIDADES QUE APRENDI COM PESQUISAS

#OPERAÇÕES VETORAIS EM PYTORCH

import torch

vetor_A = torch.tensor([20, 10, 40, 60, 50])
vetor_B = torch.tensor([25, 45, 33, 80, 22])

print(vetor_A * 2)
print(vetor_A / 2)
print(vetor_A ** 2)
print(vetor_A + vetor_B)
print(vetor_A * vetor_B)



#VERIFICAR NÚMERO DE VEZES QUE UMA SUBSTRING OCORRE EM UMA DETERMINADA STRING



texto = """
    Classificada! Nesta segunda-feira (28), no Estádio 974, em Doha, a Seleção Brasileira venceu a Suíça por 1 a 0, em jogo válido pela segunda rodada do Grupo G. 
    Com seis pontos, o Brasil confirmou a vaga antecipada nas oitavas de final. A Canarinho encerra a fase de grupos diante de Camarões, na sexta-feira (02),
    às 16h (Horário de Brasília), no Estádio Nacional de Lusai.

    O jogo começou equilibrado com boas chances para os dois lados. Após um primeiro tempo amarrado, a Seleção Brasileira encontrou o caminho do gol na etapa final,
    primeiro com Vinicius Junior, aos 20 min, mas a arbitragem marcou impedimento na jogada. 

"""

print(texto.count("jogo"))



#PROGRAMA PYTHON PARA DIVIDIR UNIU CARACTERES SEMELHANTES CONSECUTIVOS

#VOU USAR: JOIN() + LIST COMPREENSÃO + GROUPBY()



from itertools import groupby

string_teste = 'jjkkkqppzmaayyyyyyy'

print("A sequência original é: " + str(string_teste))

res = ["".join(group) for valor, group in groupby(string_teste)]

print("String de divisão consecutiva é: " + str(res))


#PROGRAMA PYTHON PARA VEREFICAR SE DUAS FRASES PODEM SER IGUAIS REORGANIZANDO AS PALAVRAS

#USANDO SORT() E SPLIT()


def ReArrangeStrings(string1, string2):

    list1 = list(string1.split())
    list2 = list(string2.split())

    list1.sort()
    list2.sort()

    if (list1 == list2):
        return True
    else:
        return False


S1 = "Brasil será campeão"
S2 = "campeão será Brasil"

if (ReArrangeStrings(S1, S2)):
    print("Sim")
else:
    print("Não")


#PROGRAMA PYTHON PARA TESTAR SE TODOS OS ELEMENTOS NA LISTA ESTÃO SEPARADOS NO MÁXIMO DE K

#USANDO MIN() + MAX()



teste_list = [455, 467, 432, 470, 578, 555]

print("A lista original é: " + str(teste_list))

K = 100

res = max(teste_list) - min(teste_list) < K

print("São elementos no intervalo? " + str(res))

