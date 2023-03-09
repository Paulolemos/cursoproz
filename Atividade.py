QtdRodas = 4
Peso = 6000
QtdPessoas = 4



if QtdRodas < 4:
    print('Habilitação categoria A')
elif QtdRodas >= 4 and QtdPessoas <= 8 and Peso > 3500 :
    print('Habilitação categoria B')
elif QtdRodas >= 4 and Peso > 3500:
    print('Habilitação categoria C')
else:
    print('Habilitação categoria D')
