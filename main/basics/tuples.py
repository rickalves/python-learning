# Estudo de lista heterogêneas imutáveis em Python class 'tuple'
dias_semana = (
    "Domingo",  
    "Segunda-Feira", 
    "Terca-Feira", 
    "Quarta-Feira", 
    "Quinta-Feira", 
    "Sexta-Feira",
    "Sabado"
    )
frutas = ["banana", "laranja", "maca", "uva"]
novas_frutas = tuple(frutas)
print(type(dias_semana))
print(type(frutas))
print(type(novas_frutas))
print(dias_semana)