#importamos base de datos
import sqlite3
class RegaloDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.crear_tabla()
        
    def crear_tabla(self):
        cursor = self.conn.cursor()
        # Guardaremos: El plan elegido y la hora
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS eleccion (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plan TEXT NOT NULL,
                hora TEXT,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def guardar_plan(self, plan, hora):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO eleccion (plan, hora) VALUES (?, ?)", (plan, hora))
        self.conn.commit()

    def ver_eleccion(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM eleccion ORDER BY id DESC LIMIT 1")
        return cursor.fetchone()