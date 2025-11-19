from src.config.version import VERSION
import threading
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DB_NAME")


class Logger:
    @staticmethod
    def inserir_log(tramite, centros, especialidade, linguas, itinerancias, status, duracion):
        try:
            connection = psycopg2.connect(
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT,
                dbname=DBNAME
            )
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO public.botcxtlogs
                (created_at, version, tramite, centros, especialidade, linguas, itinerancias, status, duracion)
                VALUES (NOW(), %s, %s, %s, %s, %s, %s, %s, %s);
            """, (VERSION, tramite, centros, especialidade, linguas, itinerancias, status, duracion))

            connection.commit()
            print("Log da execución gardado")
        except Exception as e:
            print(f"[Erro DB] Non se puido inserir o log: {e}")
        finally:
            try:
                cursor.close()
                connection.close()
            except:
                pass

    @staticmethod
    def inserir_log_async(tramite, centros, especialidade, linguas, itinerancias, status, duracion):
        thread = threading.Thread(
            target=Logger.inserir_log,
            args=(tramite, centros, especialidade, linguas, itinerancias, status, duracion),
            daemon=True
        )
        thread.start()
