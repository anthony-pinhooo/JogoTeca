import mysql.connector
from mysql.connector import errorcode

print("Conectando...")

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password=''
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Exite algo de errado no nomme de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

cursor.execute(" CREATE DATABASE `jogoteca`;")

cursor.execute("USE `jogoteca`;")

#Criando tabelas
TABLES = {}
TABLES['Jogos'] = (''''
    CREATE TABLE `jogos`( 
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `nome` varchar(50) NOT NULL, 
    `categoria` varchar(40) NOT NULL,
    `console` varchar(20) NOT NULL,
    PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
    CREATE TABLE `usuarios`(
    `nome` varchar(20) NOT NULL,
    `nickname` varchar(8) NOT NULL,
    `senha` varchar(100) NOT NULL,
    PRIMARY KEY (`nickname`) 
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print("Criando tabela {}".format(tabela_nome), end='')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('já existe')
        else:
            print(err)
    else:
        print("OK")

#inserindo usuários
usuario_sql = 'INSERT INTO usuarios(nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ('Bruno Divino', 'BD', 'admin'),
    ('Camila Ferreira', 'Mila', 'pao'),
    ('Guilherme Louro', 'Cake', 'adm')
]

cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from jogoteca.usuarios')
print(' ---------- USUARIOS ----------')
for user in cursor.fetchall():
    print(user[1])

#inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
    ('Tetriz', 'Puzzle', 'Atari'),
    ('God of War', 'Hack n Slash', 'PS2'),
    ('Mortal Kombat', 'Luta', 'PS2'),
    ('Valorant', 'FPS', 'PC'),
    ('Crash Bandicoot', 'Hack n Slash', 'PS2')
]

cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from jogoteca.jogos')
print(" ---------- JOGOS ---------- ")
for jogo in cursor.fetchall():
    print(jogo[1])

#comitando se nao tem nada feito
conn.commit()

#fechando conexao
conn.close()
