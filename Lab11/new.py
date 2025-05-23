import psycopg2  # PostgreSQL-мен жұмыс істеу үшін кітапхана

# Дерекқорға қосылу
conn = psycopg2.connect(  # Байланыс жасау үшін дерекқор параметрлерін көрсету
    dbname="BAzA",             # Дерекқордың атауы
    user="postgres",           # Қолданушы аты
    password="12345678",       # Құпия сөз
    host="localhost",          # Сервер (жергілікті)
    port="5432"                # PostgreSQL әдепкі порты
)
cur = conn.cursor()  # SQL сұраныстарын орындау үшін курсор жасау

# 1. Функция: шаблон арқылы іздеу (аты немесе номері бойынша)
def search_pattern():
    pattern = input("Шаблон енгіз (аты немесе номері): ")  # Қолданушыдан іздеу шаблонын сұрау
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))  # Функцияны шақырып, шаблонмен іздеу
    results = cur.fetchall()  # Барлық нәтижелерді алу
    for row in results:
        print(row)  # Әр жолды басып шығару

# 2. Процедура: қолданушыны қосу немесе бар болса - жаңарту
def insert_or_update():
    name = input("Аты: ")  # Қолданушы атын енгізу
    phone = input("Телефон: ")  # Қолданушы номерін енгізу
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))  # Процедураны шақыру
    conn.commit()  # Өзгерістерді сақтау
    print("Қосылды немесе жаңартылды.")  # Растау хабарламасы

# 3. Процедура: бірнеше қолданушыны қосу және дұрыс емес номерлерді тексеру
def insert_many():
    names = input("Аттарды енгіз (үтірмен бөл): ").split(",")  # Қолданушы аттарын енгізу және бөлу
    phones = input("Номерлерді енгіз (үтірмен бөл): ").split(",")  # Номерлерді енгізу және бөлу
    cur.execute("CALL insert_many_users(%s, %s, %s)", (names, phones, None))  # Көп қолданушыны қосу процедурасы
    conn.commit()  # Өзгерістерді сақтау
    print("Қосу аяқталды. Нәтижені тексер.")  # Растау хабарламасы

# 4. Функция: деректерді бөліктермен шығару (пагинация)
def paginate():
    limit = int(input("Қанша жазба шығару керек? "))  # Қанша жазбаны көрсету керек екенін енгізу
    offset = int(input("Қаншасынан бастаймыз? "))  # Қай жолдан бастаймыз (ауыстыру мәні)
    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))  # Пагинация функциясын шақыру
    for row in cur.fetchall():
        print(row)  # Әр жазбаны басып шығару

# 5. Процедура: қолданушыны атымен немесе номерімен өшіру
def delete_user():
    val = input("Аты немесе номері: ")  # Қолданушыдан өшіру үшін мән сұрау
    cur.execute("CALL delete_user(%s)", (val,))  # Өшіру процедурасын шақыру
    conn.commit()  # Өзгерістерді сақтау
    print("Өшірілді.")  # Растау хабарламасы

# Негізгі мәзір – қолданушыға әрекет таңдату
while True:
    print("\n===== LAB 11: PHONEBOOK ФУНКЦИЯЛАР =====")  # Мәзір тақырыбы
    print("1. Іздеу (pattern)")
    print("2. Бір қолданушыны қосу/жаңарту")
    print("3. Көп қолданушыны қосу (тексеруімен)")
    print("4. Пагинация")
    print("5. Өшіру аты/номер арқылы")
    print("0. Шығу")

    choice = input("Таңда: ")  # Қолданушы таңдау енгізеді
    if choice == "1":
        search_pattern()  # Іздеу функциясын шақыру
    elif choice == "2":
        insert_or_update()  # Қосу/жаңарту процедурасын шақыру
    elif choice == "3":
        insert_many()  # Көп қолданушыны қосу
    elif choice == "4":
        paginate()  # Пагинация функциясы
    elif choice == "5":
        delete_user()  # Өшіру процедурасы
    elif choice == "0":
        break  # Шығу
    else:
        print("Қате таңдау!")  # Қате енгізілген жағдайда хабарлама

cur.close()  # Курсорды жабу
conn.close()  # Дерекқор байланысын жабу
