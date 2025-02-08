import os
import pandahouse
from dotenv import load_dotenv


# Загружаем переменные окружения из файла .env
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

class Getch:
    def __init__(self, query, db='default'):
        self.connection = {
            'host': DB_HOST,
            'database': db,
            'user': DB_USER,
            'password': DB_PASSWORD
        }
        self.query = query
        self.getchdf

    @property
    def getchdf(self):
        self.df = pandahouse.read_clickhouse(self.query, connection=self.connection)

        