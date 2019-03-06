#RESOLVER AS EQUAÇÕES LINEARES

a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))
d = int(input("Digite o valor de D:"))
e = int(input("Digite o valor de E:"))
f = int(input("Digite o valor de F:"))
#RESOLUÇÕES DA EQUAÇÃO 'X' <------------>
#Se o primeiro valor inserido for menor
#que o segundo valor o resultado sera negativo!!
a1 = (c*e)-(b*f)
a2 = (a*e)-(b*d)
a3 = a1/a2
x = a3
#<---------------------->
b1 = (a*f)-(c*d)
b2 = (a*e)-(b*d)
b3 = b1/b2
y = b3
#<--------------------->
print("VALOR DE 'X' :", x)
print("VALOR DE 'Y' :", y)