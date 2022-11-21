import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

numEpocas = 10000     # Número de épocas.
q = 1000             # Número de padrões.
bias = 1              # Bias.

eta = 0.01            # Taxa de aprendizado.
m = 5                 # Número de neurônios na camada de entrada.
N = 10                 # Número de neurônios na camada escondida.
L = 1                 # Número de neurônios na camada de saída.

marca = pd.read_csv('treinamento.csv', usecols=[0])
marca = np.array(marca)
marca = np.transpose(marca)

ano = pd.read_csv('treinamento.csv', usecols=[1])
ano = np.array(ano)
ano = np.transpose(ano)

milhagem = pd.read_csv('treinamento.csv', usecols=[2])
milhagem = np.array(milhagem)
milhagem = np.transpose(milhagem)

com = pd.read_csv('treinamento.csv', usecols=[3])
com = np.array(com)
com = np.transpose(com)

preco = pd.read_csv('treinamento.csv', usecols=[4])
preco = np.array(preco)
preco = np.transpose(preco)

res = pd.read_csv('treinamento.csv', usecols=[5])
res = np.array(res)
res = np.transpose(res)

W1 = np.random.random((N, m + 1))
W2 = np.random.random((N, m + 1))
W3 = np.random.random((L, N + 1))

# Array para amazernar os erros.
E = np.zeros(q)
Etm = np.zeros(numEpocas)

X = np.vstack((marca, ano, milhagem, com, preco)) 

for i in range(numEpocas): #repete o numero de vezes terminado, no caso 20
    for j in range(q): #repete o numero de "dados" existentes (nesse exemplo 13)
        
        # Insere o bias no vetor de entrada (apresentação do padrão da rede)
        Xb = np.hstack((bias, X[:,j])) #empilhamos pelo hstack junto ao bias e ficamos 
                                       #com unico vetor [bias peso PH]

        # Saída da Camada Escondida.
        o1 = np.tanh(W1.dot(Xb))            # Equações (1) e (2) juntas. 
                                            # (W1.dot(Xb))
                                            # np.tanh  ==> tangente hiperbólica
                                            # Geremos o vetor o1 = saida da camada intermediária

        # Incluindo o bias. Saída da camada escondida é a entrada da camada
        # de saída.
        o1b = np.insert(o1, 0, bias)
        
        o2 = np.tanh(W2.dot(o1b))
        
        o2b = np.insert(o2, 0, bias)

        # Neural network output
        Y = np.tanh(W3.dot(o2b))            # Equações (3) e (4) juntas.
                                            #Resulta na saída da rede neural
        
        e = res[j] - Y                        # Equação (5).

        # Erro Total.
        E[j] = (e.transpose().dot(e))/2     # Equação de erro quadrática.
        
        # Imprime o número da época e o Erro Total.
        # print('i = ' + str(i) + '   E = ' + str(E))
   
        # Error backpropagation.   
        # Cálculo do gradiente na camada de saída.
        delta3 = np.diag(e).dot((1 - Y*Y))          # Eq. (6)
        vdelta3 = (W3.transpose()).dot(delta3)      # Eq. (7)
        delta2 = np.diag(1 - o2b*o2b).dot(vdelta3)  # Eq. (6)
        vdelta2 = (W2.transpose()).dot(delta2)      # Eq. (7)
        delta1 = np.diag(1 - o1b*o1b).dot(vdelta2)  # Eq. (8)

        # Atualização dos pesos.
        W1 = W1 + eta*(np.outer(delta1[1:], Xb))
        W2 = W2 + eta*(np.outer(delta2, o1b))
        W3 = W3 + eta*(np.outer(delta3, o2b))
    
    #Calculo da média dos erros
    Etm[i] = E.mean()

print(Etm)

Error_Test = np.zeros(q)

for i in range(q):
    # Insere o bias no vetor de entrada.
    Xb = np.hstack((bias, X[:,i]))

    # Saída da Camada Escondida.
    o1 = np.tanh(W1.dot(Xb))            # Equações (1) e (2) juntas.      
    #print(o1)
    
    # Incluindo o bias. Saída da camada escondida é a entrada da camada
    # de saída.
    o1b = np.insert(o1, 0, bias)
    
    o2 = np.tanh(W2.dot(o1b))
        
    o2b = np.insert(o2, 0, bias)

    # Neural network output
    Y = np.tanh(W3.dot(o2b))            # Equações (3) e (4) juntas.
    print(Y)
    
    Error_Test[i] = res[i] - (Y)
    
print(Error_Test)
print(np.round(Error_Test) - res)
