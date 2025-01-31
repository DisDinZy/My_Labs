#Если имеется более одного элемента с указанным значением, remove()метод удаляет первое вхождение:

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


#Ключевое delслово также удаляет указанный индекс
#Ключевое delслово также может полностью удалить список.

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Метод clear()очищает список.
#Список сохранился, но в нем нет содержания.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)