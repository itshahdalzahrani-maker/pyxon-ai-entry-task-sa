import sqlite3
from typing import List


class SQLDB:
    def _init_(self, db_path="metadata.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT
            )
        """)
        self.conn.commit()

    def insert_chunks(self, chunks: List[str]):
        cur = self.conn.cursor()
        cur.executemany(
            "INSERT INTO documents (content) VALUES (?)",
            [(c,) for c in chunks]
        )
        self.conn.commit()

    def fetch_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT content FROM documents")
        return [row[0] for row in cur.fetchall()]