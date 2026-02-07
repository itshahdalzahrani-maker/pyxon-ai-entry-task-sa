from parser import parse_file
from chunker import chunk_text
from vector_db import VectorDB
from sql_db import SQLDB

def main():
    file_path = "../data/sample.txt"

    # قراءة الملف
    text = parse_file(file_path)

    
    chunks = chunk_text(text, max_words=400)

    
    sql_db = SQLDB()
    sql_db.insert_chunks(chunks)

    
    vector_db = VectorDB()
    vector_db.add_texts(chunks)

if __name__ == "_main_":
    main()