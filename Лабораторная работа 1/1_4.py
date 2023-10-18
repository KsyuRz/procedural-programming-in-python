users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
visites={"Общее количество":0,"Уникальные посещения":0} #Создаем словарь
count=len(users)
count_unique=len(set(users))
visites["Общее количество"]=count
visites["Уникальные посещения"]=count_unique
print(visites)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
