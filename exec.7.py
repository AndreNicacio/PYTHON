#DEFINIR A PORCENTAGEM DA VENDA DO CARRO APOS ELE SER VENDIDO DA FABRICA

fabrica = float(input("Qual o valor do carro na fabrica ?"))
a1 = 28*fabrica
a2 = a1/100
b1 = 45*fabrica
b2 = b1/100
b3 = b2+a1
b4 = b3+fabrica
print("<--------------------------------------------->")
print("O valor final para o consumidor seria de :", b4 ,"reais")
print("<--------------------------------------------->")