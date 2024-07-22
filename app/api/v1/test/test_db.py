import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from app.api.v1.config.database import engine, Base
from sqlalchemy import text

def test_connection():
    try:
        # Ejecutar una consulta simple para verificar la conexión
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Database connection successful!")
            print("Result:", result.fetchone())
    except Exception as e:
        print("Error connecting to the database:", e)

if __name__ == "__main__":
    test_connection()
