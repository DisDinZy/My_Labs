import psycopg2  # PostgreSQL-мен жұмыс істеу үшін кітапхана
import csv       # CSV файлдарымен жұмыс істеу үшін кітапхана

# PostgreSQL дерекқорына қосылу
conn = psycopg2.connect(
    dbname="BAzA",        # Дерекқордың атауы
    user="postgres",      # Пайдаланушы аты
    password="12345678",  # Құпиясөз
    host="localhost",     # Жергілікті хост
    port="5432"           # PostgreSQL әдепкі порты
)
cur = conn.cursor()  # SQL сұраныстарын орындау үшін курсор жасау

# 📌 1. Кесте құру
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (  -- Егер кесте жоқ болса, осыны жасайды
        id SERIAL PRIMARY KEY,              -- Бірегей автоматты ID (басты кілт)
        name VARCHAR(50),                   -- Адамның аты (50 таңбаға дейін)
        phone VARCHAR(20)                   -- Телефон нөмірі (20 таңбаға дейін)
    );
""")
conn.commit()  # Өзгерістерді дерекқорда сақтау

# 📌 2. CSV файлдан деректерді жүктеу
def load_from_csv():
    with open('psycopg2.csv', 'r') as f:          # CSV файлын оқу үшін ашу
        reader = csv.reader(f)                    # CSV оқу объектісі
        next(reader)                              # Бірінші жолды (тақырып) өткізіп жіберу
        for row in reader:                        # Әр жолды оқу
            if len(row) >= 2:                     # Егер аты мен номері бар болса
                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                    (row[0], row[1])              # Атын және номерін енгізу
                )
    conn.commit()                                 # Өзгерістерді сақтау
    print("CSV жүктелді!")                        # Хабарлама шығару

# 📌 3. Қолмен дерек енгізу
def insert_manually():
    name = input("Атың: ")                        # Пайдаланушыдан аты сұралады
    phone = input("Нөмірің: ")                    # Пайдаланушыдан номер сұралады
    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)                             # Дерекқорға енгізу
    )
    conn.commit()                                 # Өзгерісті сақтау
    print("Дерек қосылды!")                       # Хабарлама

# 📌 4. Деректі жаңарту
def update_entry():
    name = input("Қай атты өзгертеміз? ")         # Қай адамның номерін өзгертетінімізді сұрау
    new_phone = input("Жаңа номер: ")             # Жаңа номерді енгізу
    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (new_phone, name)                         # Көрсетілген адамға жаңа номер беру
    )
    conn.commit()                                 # Өзгерісті сақтау
    print("Жаңартылды!")                          # Хабарлама

# 📌 5. Адамды аты бойынша іздеу
def query_data():
    filter_name = input("Аты бойынша іздеу: ")    # Іздеу үшін аты енгізіледі
    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        ('%' + filter_name + '%',)                # ІLIKE — регистрге тәуелсіз іздеу
    )
    results = cur.fetchall()                      # Барлық табылған жолдарды алу
    for row in results:
        print(row)                                # Әр табылған жолды басып шығару

# 📌 6. Адамды өшіру
def delete_entry():
    name = input("Кімді өшіресіз (аты): ")        # Өшіру үшін аты енгізіледі
    cur.execute(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)                                   # Көрсетілген атты өшіру
    )
    conn.commit()                                 # Өзгерісті сақтау
    print("Өшірілді!")                            # Хабарлама

# 📌 7. Негізгі мәзір: қай функцияны таңдайтынын сұраймыз
while True:
    print("\n===== PHONEBOOK МӘЗІРІ =====")
    print("1. CSV-тен жүктеу")
    print("2. Қолмен енгізу")
    print("3. Жаңарту")
    print("4. Іздеу")
    print("5. Өшіру")
    print("0. Шығу")

    choice = input("Таңда: ")                     # Таңдау енгізу
    if choice == "1":
        load_from_csv()                           # 1 → CSV жүктеу
    elif choice == "2":
        insert_manually()                         # 2 → қолмен енгізу
    elif choice == "3":
        update_entry()                            # 3 → дерек жаңарту
    elif choice == "4":
        query_data()                              # 4 → іздеу
    elif choice == "5":
        delete_entry()                            # 5 → өшіру
    elif choice == "0":
        break                                     # 0 → бағдарламадан шығу
    else:
        print("Қате таңдау!")                     # Басқа таңдау болса — қате

# 📌 8. Бағдарлама соңында — бәрін жабу
cur.close()                                       # Курсорды жабу
conn.close()                                      # Дерекқор байланысын жабу
