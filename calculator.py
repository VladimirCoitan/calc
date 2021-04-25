#introducem primul numar

a = float(input('Introduceti primul numar: '))

#alegem ce vom face cu doua numere

calc = input('Alege ce vrei sa faci: ')

#introducem al doilea numar

b = float(input('Introduceti al doilea numar: '))

if calc == '+':
    c = a + b
    print('Rezultatul este ' + str(c))
    
elif calc == '-':
    c = a - b
    print('Rezultatul este ' + str(c))
    
elif calc == '*':
    c = a * b
    print('Rezultatul este ' + str(c))
    
elif calc == '/':
    c = a / b
    print('Rezultatul este ' + str(c))
    
elif calc == '**':
    c = a ** b
    print('Rezultatul este ' + str(c))
    
elif calc == '%':
    c = a % b
    print('Rezultatul este ' + str(c))
    
else: print('Ai introdus semnul incorect! Mai incearca.')

input()

