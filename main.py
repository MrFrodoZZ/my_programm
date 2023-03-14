import os
import sqlite3

db = sqlite3.connect('db.db')
sql = db.cursor()


def createRow(values):
	sql.execute("""
	INSERT INTO myTable VALUES (?,?,?,?,?,?,?,?,?)""", values)
	db.commit()


def deleteRow(key):
	sql.execute("""
	DELETE FROM myTable WHERE""", ())
	db.commit()


def selectRow(key):
	return sql.execute(f"""
	SELECT * FROM myTable WHERE {key}""").fetchall()


running = True
while running:
	action = int(input("""Выбери действие:
	1 - Внести новые данные
	2 - Найти данные
		
	0 - Завершить программу
	
	"""))
	
	if action == 1:
		values = []
		values.append(input('ФИО: '))
		values.append(input('Дата рождения: '))
		values.append(input('Вид страхования: '))
		values.append(input('Срок страхования: '))
		values.append(int(input('Страховая сумма: ')))
		values.append(int(input('Страховая премия: ')))
		values.append(input('Агент: '))
		values.append(int(input('КВ общий (%): ')) / 100 * values[4])
		values.append(int(input('КВ отдающий (%): ')) / 100 * values[5])
		print(values)
		createRow(values)
		print('Запись создана.\n\n')
		
	
	if action == 2:
		search = int(input("""Выбери фильтр поиска:
1 - Имя/Фамилия/Отчество
2 - Дата рождения
3 - Вид страхования
4 - Срок страхования
5 - Страховая сумма
6 - Страховая премия
7 - Агент"""))
		if search == 1:
			for i in selectRow(f'name LIKE "%{input()}%"'):
				print(i)
		elif search == 2:
			for i in selectRow(f'birth LIKE "%{input()}%"'):
				print(i)
		elif search == 3:
			for i in selectRow(f'subject LIKE "%{input()}%"'):
				print(i)
		elif search == 4:
			for i in selectRow(f'length LIKE "%{input()}%"'):
				print(i)
		elif search == 5:
			for i in selectRow(f'sum LIKE "%{input()}%"'):
				print(i)
		elif search == 6:
			for i in selectRow(f'prem LIKE "%{input()}%"'):
				print(i)
		elif search == 7:
			for i in selectRow(f'agent LIKE "%{input()}%"'):
				print(i)
		finally:
			print(),
	
	if action == 0:
		running = False
	
db.close()
