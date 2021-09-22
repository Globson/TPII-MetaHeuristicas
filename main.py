'''
Samuel Pedro Campos Sena - EF3494
Trabalho prático 1 - CCF480 - MetaHeurísticas
'''

'''
Referências utilizadas:
https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/. Acesso em: 22 Set. 2021.
'''
import matplotlib.pyplot as plt
from numpy.random import seed, rand, randn
from numpy import sin, sqrt, asarray, mean, std


def objetivo1(v): #G6(x)
    x1, x2 = v
    return (pow((x1 - 10),3) + pow((x2-20),3))


def objetivo2(v):
    x, y = v
    return (1)


#1
Resultados1_AG_A = []
Resultados1_AG_B = []
#2
Resultados2_AG_A = []
Resultados2_AG_B = []
#fazer 30 vezes para cada funcao objetivo e algoritmo, adicionar em listas correspondentes


# adicionando seed de gerador rand
seed()

# definindo limites
limites1 = asarray([[13., 100.], 
                    [0., 100.]])
#limites2 ??

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
'''for i in range(30):
    _ , valor = ils(objetivo1, limites1a, iteracoes, Tam_passoHC, reinicios, Tam_P)
    Resultados1_AG_B.append(valor)
    _ , valor = melhor, valor = hc(objetivo1, limites1a, iteracoes, Tam_passoHC)   
    Resultados1_AG_A.append(valor)
    _ , valor = ils(objetivo1, limites1b, iteracoes, Tam_passoHC, reinicios, Tam_P)
    Resultados2_AG_B.append(valor)
    _ , valor = melhor, valor = hc(objetivo1, limites1b, iteracoes, Tam_passoHC)   
    Resultados2_AG_A.append(valor)
    _ , valor = ils(objetivo2, limites2c, iteracoes, Tam_passoHC, reinicios, Tam_P)
    Resultados2C_ILS.append(valor)
    _ , valor = melhor, valor = hc(objetivo2, limites2c, iteracoes, Tam_passoHC)   
    Resultados2C_HC.append(valor)
    _ , valor = ils(objetivo2, limites2d, iteracoes, Tam_passoHC, reinicios, Tam_P)
    Resultados2D_ILS.append(valor)
    _ , valor = melhor, valor = hc(objetivo2, limites2d, iteracoes, Tam_passoHC)   
    Resultados2D_HC.append(valor)'''

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
#plt.show()
archive.close()

'''
print(Resultados1_AG_A)
print(Resultados1_AG_B)
print(Resultados2_AG_A)
print(Resultados2_AG_B)
'''
