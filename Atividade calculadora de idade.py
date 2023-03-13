from datetime import date
current_date = date.today()
Nome = input("Informe seu nome:")
data_nascimento= int(input("Ano de nascimento:"))
data_actual = current_date.year
idade =data_actual-data_nascimento

print(Nome)   
print(idade)