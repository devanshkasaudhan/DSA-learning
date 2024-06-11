import sqlite3

conn = sqlite3.connect('questions.db')
cursor = conn.cursor()
cursor.execute('DELETE FROM QUESTIONS')
conn.commit()
conn.close()
