'''
Samuel Pedro Campos Sena - EF3494
Saulo Miranda Silva - EF3475
Trabalho prático 2 - CCF480 - MetaHeurísticas
'''


import matplotlib.pyplot as plt
from numpy.random import seed, rand, randn
from numpy import sin, sqrt, asarray, mean, std
from AG import *

limInferior = [13, 0]
limSuperior = [100, 100]
pop = gerarPopulacaoInicial(100, 2, limInferior, limSuperior)
for i in range(100):
  print(pop[i])

resultados = funcaoFitness(100, pop)
for i in range(100):
  print(resultados[i])

teste = selecaoTorneio(100, pop, pop)
for i in range(50):
  print(teste[i])

print(cruzamentoFlat(2, [[2, 3], [4, 1], [10, 9]]))

teste = selecaoTorneio(100, pop, pop)
for i in range(50):
  print(teste[i])

print(cruzamentoFlat(2, [[2, 3], [4, 1], [10, 9]]))

muta = [[13, 5], [30, 28]]
for j in range(2):
  muta[j] = mutacaoUniforme(muta[j], limInferior, limSuperior)
print(muta)

print(questao1())

#1
Resultados1_AG_A = []
Resultados1_AG_B = []
#2
Resultados2_AG_A = []
Resultados2_AG_B = []
#fazer 30 vezes para cada funcao objetivo e algoritmo, adicionar em listas correspondentes


# adicionando seed de gerador rand
seed()


archive = open('Resultados.txt', 'w')
archive.write("\nConfiguracoes:")
'''archive.write("\nIteracoes no HC: " + str(iteracoes))
archive.write("\nTamanho do passo no HC: " + str(Tam_passoHC))
archive.write("\nQuantidade de reinicios no ILS: " + str(reinicios))
archive.write("\nTamanho da pertubação no ILS: " + str(Tam_P))
archive.write("\n\nRealizando 30 iteracoes dos algoritmos...")'''
print("Configuracoes:")
'''print("Iteracoes no HC: ", iteracoes)
print("Tamanho do passo no HC: ",Tam_passoHC)
print("Quantidade de reinicios no ILS: ", reinicios)
print("Tamanho da pertubação no ILS: ", Tam_P)
print("\nRealizando 30 iteracoes dos algoritmos...")'''
for i in range(30):
   Resultados1_AG_A.append(questao1())

archive.write("\n----------------------")
archive.write("\nFuncao Objetivo 1 - AG  Config A:")
archive.write("\nMin: " + str(min(Resultados1_AG_A)))
archive.write("\nMax: " + str(max(Resultados1_AG_A)))
archive.write("\nMedia: " + str(mean(Resultados1_AG_A)))
archive.write("\nStd: " + str(std(Resultados1_AG_A)))
print("Funcao Objetivo 1 - AG  Config A:")
print("Min: ",min(Resultados1_AG_A))
print("Max: ",max(Resultados1_AG_A))
print("Media: ",mean(Resultados1_AG_A))
print("Std: ",std(Resultados1_AG_A))
plt.boxplot(Resultados1_AG_A)
plt.title("Resultado 1 AG_A")
plt.savefig('plots/1_AG_A.png', format='png')
#plt.show()
'''
archive.write("\n\nFuncao Objetivo 1 - AG  Config B:")
archive.write("\nMin: " + str(min(Resultados1_AG_B)))
archive.write("\nMax: " + str(max(Resultados1_AG_B)))
archive.write("\nMedia: " + str(mean(Resultados1_AG_B)))
archive.write("\nStd: " + str(std(Resultados1_AG_B)))
archive.write("\n----------------------")
print("Funcao Objetivo 1 - AG  Config B:")
print("Min: ", min(Resultados1_AG_B))
print("Max: ", max(Resultados1_AG_B))
print("Media: ", mean(Resultados1_AG_B))
print("Std: ", std(Resultados1_AG_B))
plt.clf()
plt.boxplot(Resultados1_AG_B)
plt.title("Resultado 1 AG_B")
plt.savefig('plots/1_AG_B.png', format='png')
#plt.show()


archive.write("\nFuncao Objetivo 2 - AG  Config A:")
archive.write("\nMin: " + str(min(Resultados2_AG_A)))
archive.write("\nMax: " + str(max(Resultados2_AG_A)))
archive.write("\nMedia: " + str(mean(Resultados2_AG_A)))
archive.write("\nStd: " + str(std(Resultados2_AG_A)))
print("Funcao Objetivo 2 - AG  Config A:")
print("Min: ",min(Resultados2_AG_A))
print("Max: ",max(Resultados2_AG_A))
print("Media: ",mean(Resultados2_AG_A))
print("Std: ",std(Resultados2_AG_A))
plt.clf()
plt.boxplot(Resultados2_AG_A)
plt.title("Resultado 2 AG_A")
plt.savefig('plots/2_AG_A.png', format='png')
#plt.show()

archive.write("\n\nFuncao Objetivo 2 - AG  Config B:")
archive.write("\nMin: " + str(min(Resultados2_AG_B)))
archive.write("\nMax: " + str(max(Resultados2_AG_B)))
archive.write("\nMedia: " + str(mean(Resultados2_AG_B)))
archive.write("\nStd: " + str(std(Resultados2_AG_B)))
archive.write("\n----------------------")
print("ILS: ")
print("Min: ", min(Resultados2_AG_B))
print("Max: ", max(Resultados2_AG_B))
print("Media: ", mean(Resultados2_AG_B))
print("Std: ", std(Resultados2_AG_B))
plt.clf()
plt.boxplot(Resultados2_AG_B)
plt.title("Resultado 2 AG_B")
plt.savefig('plots/2_AG_B.png', format='png')
#plt.show()'''
archive.close()

'''
print(Resultados1_AG_A)
print(Resultados1_AG_B)
print(Resultados2_AG_A)
print(Resultados2_AG_B)
'''
