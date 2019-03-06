#CONSTRUA UM DADO ONDE PEGUE OS PONTOS DE X e Y e DIGA A DISTANCIA

#Declaração de variavél x1.
#Leitura do valor de x1.
#Conversão do valor de x1 para inteiro.
x1 = int(input("Digite o valor de x1 :"))

#Imprimir o valor de x1.
print("valor de x1: ", x1)

y1 = int(input("Digite o valor de y1 :"))
print("valor de y1 :", y1)

#<------------------------------------>

x2 = int(input("Digite o valor de x2 :"))
print("valor de x2 :", x2)

y2 = int(input("Digite o valor de y2 :"))
print("valor de y2 :", y2)

#Calcular a diferença do eixo 'x'

dx = (x2-x1)**2
print("Diferença de x(x1-x2) :", dx)

dy = (y2-y1)**2
print("Diferença de y(y1-y2) :", dy)

#calcular a diferença
d = (dx+dy)
print("Diferença :", d)

#calcular a distancia
da = d**(1/2)
print("Distancia : ", da)