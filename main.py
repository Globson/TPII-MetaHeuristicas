'''
Samuel Pedro Campos Sena - EF3494
Saulo Miranda Silva - EF3475
Trabalho prático 2 - CCF480 - MetaHeurísticas
'''


import matplotlib.pyplot as plt
from numpy import mean, std
from AG import *







'''
print(questao1_A())
print(questao1_B())
'''
#1
Resultados1_AG_A = []
Resultados1_AG_B = []
#2
Resultados2_AG_A = []
Resultados2_AG_B = []
#fazer 30 vezes para cada funcao objetivo e algoritmo, adicionar em listas correspondentes




archive = open('Resultados.txt', 'w')
archive.write("\nConfiguracoes 1 AG Config A:")
archive.write("\nTamanho da população: 10000")
archive.write("\nCritério de parada:")
archive.write("\n\tQuantidade de iterações sem uma melhora significativa: 5")
archive.write("\n\nConfiguracoes 1 AG Config B:")
archive.write("\nTamanho da população: 100000")
archive.write("\nCritério de parada:")
archive.write("\n\tQuantidade de iterações sem uma melhora significativa: 10")
archive.write("\n\nRealizando 30 iteracoes dos algoritmos...")

print("Configuracoes 1 AG Config A:")
print("Tamanho da população: 10000")
print("Critério de parada:")
print("\tQuantidade de iterações sem uma melhora significativa: 5")
print("\nConfiguracoes 1 AG Config B:")
print("Tamanho da população: 100000")
print("Critério de parada:")
print("\tQuantidade de iterações sem uma melhora significativa: 10")
print("\nRealizando 30 iteracoes dos algoritmos...")

for i in range(30):
   Resultados1_AG_A.append(questao1_A())
   Resultados1_AG_B.append(questao1_B())

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
plt.title("Resultado 1 AG Config A")
plt.savefig('plots/1_AG_A.png', format='png')
#plt.show()

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
plt.title("Resultado 1 AG Config B")
plt.savefig('plots/1_AG_B.png', format='png')
#plt.show()

'''
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
