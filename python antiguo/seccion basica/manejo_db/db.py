import sqlite3

conn = sqlite3.connect("database.db")

db = conn.cursor()

db.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    edad INTEGER
)
''')

conn.commit()


question = int(input("Bienvenido al sistema de base de datos de yoscarmjp\npara continuar puedes elegir unas de las opciones a continuacion.\n\n  1 - Registrar un usuario en la base de datos.\n  2 - Loguearte segun los datos que esten en la base de datos\n  3 - Revisar los usuarios registrados en la base de datos.\n\nEliges la opcion: "))

if question == 1:
    while True:
        user = input("\nIngresa tu nombre: ")
        db.execute('SELECT COUNT(*) FROM usuarios WHERE nombre = ?', (user,))
        user_exist = db.fetchone()[0]
        if user_exist > 0:
            print("\nEste usuario ya existe en la base de datos.")
        else:
            while True:
                email = input("\nIngresa tu email: ")
                db.execute('SELECT COUNT(*) FROM usuarios WHERE email = ?', (email,))
                email_exist = db.fetchone()[0]
                if email_exist > 0:
                    print("\nEse correo electronico ya se encuentra registrado en la base de datos")
                else:
                    while True:
                        try:
                            year = int(input("\nIngresa tu edad: "))
                            if year < 18:
                                print("\nDebes tener al menos 18 años para poder registrarte.")
                            else:
                                db.execute(f'''
                                INSERT INTO usuarios (nombre, email, edad)
                                VALUES (?, ?, ?)
                                ''',(user,email,year))
                                db.execute('SELECT * FROM usuarios')
                                conn.commit()
                                users = db.fetchall()
                                print(f"\nUsuarios registrados:\n\n{users}\n")
                                quit()
                        except ValueError:
                            print("\nLa edad debe ser un numero entero.")

        continue_add_user = input("\nQuieres agregar otro usuario? (S/N): ")
        if continue_add_user.lower() != "s":
            break   

    conn.close

elif question == 2:
    while True:
        user = input("\nIngresa tu nombre de usuario: ")
        db.execute('SELECT COUNT(*) FROM usuarios WHERE nombre = ?', (user,))
        user_exist = db.fetchone()[0]
        if user_exist > 0:
            while True:
                password = input("\nIngresa tu contraseña: ")
                db.execute('SELECT COUNT(*) FROM usuarios WHERE edad = ?', (password,))
                pass_exist = db.fetchone()[0]
                if pass_exist > 0:
                    print("\nIniciando sesion...")
                    quit()
                else:
                    print("\nTu contraseña no es correcta, intentalo de nuevo.")

        else:
            print("\nEste usuario no existe en la base de datos.")
elif question == 3:
    db.execute("SELECT * FROM usuarios")
    users_in_db = db.fetchall()
    print(f"\nUsuarios registrados en la base de datos:\n\n{users_in_db}")
else:
    print("\nLa opcion seleccionada no es valida.")