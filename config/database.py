# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
db_path = '/home/pxl/wsl-mnt/weather_to_db/config/'
conn = sqlite3.connect('{0}base1.db'.format(db_path), check_same_thread=False)

def ins(temp: float, datetime: str):
    cursor = conn.cursor()
    cursor.execute('insert into temperature(temp, datetime ) values (:temp,:datetime)',
                   {
                       'temp': temp,
                       'datetime': datetime,
                       })
    conn.commit()

    return 'ok'
