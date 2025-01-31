thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#По умолчанию sort()метод чувствителен к регистру, в результате чего все заглавные буквы сортируются перед строчными:

thislist1 = ["banana", "Orange", "Kiwi", "cherry"]
thislist1.sort()
print(thislist1)