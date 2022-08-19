import pymysql


try:
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='user',
        password='password',
        database='database',
    )
    print("Подключение выполнено...")

    try:
        def prints():
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `users`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        #create
        def create():
            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
                                    " name varchar(32)," \
                                    " password varchar(32)," \
                                    " age varchar(32), PRIMARY KEY (id));"
                cursor.execute(create_table_query)
                print("таблица сделана")
#create person
        def createperson():
            with connection.cursor() as cursor:
                b = str(input)
                insert_query = "INSERT INTO `users` (name, password, age) VALUES ('anna', 'qwerty', '8');"
                cursor.execute(insert_query)
                connection.commit()

# update
        def update():
                with connection.cursor() as cursor:
                    print('введите id пользователя')
                    n = input()
                    update_query = "UPDATE `users` SET password = 'xxxxx' WHERE id = %s;"
                    cursor.execute(update_query,(n,))
                    connection.commit()

# delete
        def delete():
            with connection.cursor() as cursor:
                print('введите id пользователя')
                n = input()
                delete_query = "DELETE FROM `users` WHERE id = %s"
                cursor.execute(delete_query,(n,))
                connection.commit()
                prints()

        i = 1
        while i != 0:
            print('выберите функцию')
            print('1 - delete')
            print('2 - update')
            print('3 - create')
            print('4 - print')
            i = int(input())
            if i == 1:
                delete()
            elif i == 2:
                update()
            elif i == 3:
                createperson()
            elif i == 4:
                prints()
            else:
                print('неверное число')
    finally:
        connection.close()


except Exception as ex:
    print("подключение разорвано...")
    print(ex)
