from app.vector_db import VectorDB

def simple_recall_test():
    db = VectorDB()

    docs = [
        "الذكاء الاصطناعي مجال متطور"
    ]

    db.add_texts(docs)

    query = "الذكاء الاصطناعي"
    results = db.search(query, k=1)

    success = "الذكاء الاصطناعي" in results[0]
    print("Recall@1:", success)

if __name__ == "_main_":
    simple_recall_test()