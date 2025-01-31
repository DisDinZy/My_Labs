thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Чтобы добавить элементы из другого списка в текущий список, используйте extend()метод.
#Метод extend()не обязательно должен добавлять списки , вы можете добавлять любой итерируемый объект (кортежи, наборы, словари и т. д.).
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)