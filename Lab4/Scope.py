def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

'''Если вы используете nonlocalключевое слово, 
переменная будет принадлежать внешней функции: '''