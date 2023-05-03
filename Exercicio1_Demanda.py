num1 = (input('digite o primeiro numero:'))
num2 = (input('digte o segundo numero:'))
num3 = (input('digite o terceiro numero:'))
##Três iguais" OU "Dois iguais" OU "Três diferentes" OU "Dois diferentes"
if num1 == num2 == num3:
 print('Três iguais')
elif num1 == num2 or num1 == num3 or num2 == num3:
 print('Dois iguais')
elif num1 != num2 != num3:
 print ('Três diferentes')
else:
 print('Dois diferentes')