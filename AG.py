import random
import pandas as pd
from copy import deepcopy


def G6(x1, x2):  # função  com penalidades
  g1 = max(0, ((-(x1-5)**2) - ((x2-5)**2) + 100))
  g2 = max(0, (((x1-6)**2) + ((x2-5)**2) - 82.81))
  return (x1-10)**3 + (x2-20)**3 + 0.1*g1 + 0.1*g2

def respeitaLimite(gene, limiteMin, limiteMax):
  contador = 0
  for i in range(len(gene)):
    contador += 0 if (gene[i]<=limiteMax[i] and gene[i]>=limiteMin[i]) else 1
  return contador == 0


def gerarPopulacaoInicial(quantidade, tamanho, limiteMin, limiteMax):
  populacao = []
  for i in range(0, quantidade):
    novo = [0 for i in range(tamanho)]
    for j in range(0, tamanho):
      novo[j] = random.uniform(limiteMin[j], limiteMax[j])
    populacao.append(novo)
  return populacao


def funcaoFitness(quantidade, vetorEntrada):
  fitness = []
  for i in range(quantidade):
    fitness.append(G6(vetorEntrada[i][0], vetorEntrada[i][1]))
  return fitness


def selecaoTorneio(quantidade, candidatos, pais):
  selecionados = []
  resultados = funcaoFitness(quantidade, candidatos)
  resultadosPais = funcaoFitness(quantidade, pais)
  for i in range(int(quantidade*0.7)):
    indice = random.randint(0, quantidade-1)
    candidato = resultados[indice]
    for j in range(3):
      novoIndice = random.randint(0, quantidade-1)
      novoCandidato = resultados[novoIndice]
      if (novoCandidato <= candidato):
        candidato = novoCandidato
        indice = novoIndice
    selecionados.append([candidatos[indice]])

  for i in range(int(quantidade*0.3)):
    indice = random.randint(0, quantidade-1)
    candidato = resultadosPais[indice]
    for j in range(3):
      novoIndice = random.randint(0, quantidade-1)
      novoCandidato = resultadosPais[novoIndice]
      if (novoCandidato <= candidato):
        candidato = novoCandidato
        indice = novoIndice
    selecionados.append([candidatos[indice]])
  return selecionados

def cruzamentoFlat(tamanho, pais):
  filho = [0,0]
  n = len(pais)
  geracao = []
  for j in range(0, n):
    filho = [0,0]
    for i in range(tamanho):
      filho[i] = (random.uniform(pais[random.randint(0,n-1)][i], pais[random.randint(0,n-1)][i]))
    geracao.append(filho)
  return geracao

def mutacaoUniforme(filho, limiteMin, limiteMax):
  sigma = 0.1
  vk = [0 for i in range(len(filho))]
  pm = 0.9
  if (random.uniform(0, 1) > pm):
    for i in range(len(filho)):
      vk[i] = (sigma*(limiteMax[i]-limiteMin[i])*random.uniform(-1,1)) + filho[i]
    while (respeitaLimite(vk, limiteMin, limiteMax) != True):
      for j in range(len(filho)):
        vk[j] = (sigma*(limiteMax[j]-limiteMin[j])*random.uniform(-1,1)) + filho[j]
    return vk
  else:
    return filho

#FUNÇÃO FINAL


def questao1_A():
  limInferior = [13, 0]
  limSuperior = [100, 100]
  n = 10000  # quantidade
  t = 2  # tamanho do vetor
  filhos = [[0, 0] for i in range(n)]
  random.seed()
  populacao = gerarPopulacaoInicial(n, t, limInferior, limSuperior)
  filhos = cruzamentoFlat(t, populacao)
  for i in range(n):
    filhos[i] = mutacaoUniforme(filhos[i], limInferior, limSuperior)

  contador = 0
  minimo = min(funcaoFitness(n, filhos))

  while (contador < 5):
    selecionados = selecaoTorneio(n, filhos, populacao)
    populacao = deepcopy(filhos)
    filhos = cruzamentoFlat(t, populacao)

    for i in range(n):
      filhos[i] = mutacaoUniforme(filhos[i], limInferior, limSuperior)

    if (min(funcaoFitness(n, filhos)) > (minimo - abs(minimo)*0.01)):
      contador += 1
    else:
      minimo = min(funcaoFitness(n, filhos))
      contador = 0

  return minimo


def questao1_B():
  limInferior = [13, 0]
  limSuperior = [100, 100]
  n = 100000  # quantidade
  t = 2  # tamanho do vetor
  filhos = [[0, 0] for i in range(n)]
  random.seed()
  populacao = gerarPopulacaoInicial(n, t, limInferior, limSuperior)
  filhos = cruzamentoFlat(t, populacao)
  for i in range(n):
    filhos[i] = mutacaoUniforme(filhos[i], limInferior, limSuperior)

  contador = 0
  minimo = min(funcaoFitness(n, filhos))

  while (contador < 10):
    selecionados = selecaoTorneio(n, filhos, populacao)
    populacao = deepcopy(filhos)
    filhos = cruzamentoFlat(t, populacao)

    for i in range(n):
      filhos[i] = mutacaoUniforme(filhos[i], limInferior, limSuperior)

    if (min(funcaoFitness(n, filhos)) > (minimo - abs(minimo)*0.01)):
      contador += 1
    else:
      minimo = min(funcaoFitness(n, filhos))
      contador = 0

  return minimo
