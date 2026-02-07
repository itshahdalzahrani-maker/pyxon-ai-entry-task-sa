 AI-Powered Document Parser for RAG Systems


# Overview

This project is an AI-powered document parsing and retrieval pipeline designed for *Retrieval-Augmented Generation (RAG)* systems.
It supports reading multiple document formats, intelligent text chunking, Arabic language handling, and dual storage using both Vector DB and SQL DB.

The project was implemented as part of the * Pyxon AI Junior Engineer Entry Task *.



#نظره عامه

هذا المشروع عبارة عن نظام ذكي لمعالجة المستندات وتجهيزها للاستخدام مع أنظمة *RAG (Retrieval-Augmented Generation)*.
يدعم قراءة عدة صيغ ملفات، تقسيم النص بشكل ذكي، دعم اللغة العربية، وتخزين البيانات في كلٍ من قاعدة بيانات متجهية (Vector DB) وقاعدة بيانات تقليدية (SQL).


 - - - - - -


# Features

-  Supports PDF, DOCX, and TXT files
-  Intelligent overlapping chunking strategy
-  Full Arabic language support (UTF-8 safe, diacritics preserved)
-  Vector storage using ChromaDB for semantic retrieval
-  SQL storage using SQLite for metadata
-  Simple benchmark suite for retrieval evaluation
-  Designed to be easily integrated with RAG pipelines

 - - - - - -

# Project Structure

pyxon-project/
│
├── app/
│   ├── main.py
│   ├── parser.py
│   ├── chunker.py
│   ├── vector_db.py
│   ├── sql_db.py
│
├── data/
│   ├── sample.txt
│   └── output.txt

├── benchmarks/
│   └── benchmark.py
│
├── requirements.txt
└── README.md

 - - - - - -

# How to Run the Demo

1.	Install dependencies
```bash

pip install -r requirements.txt



2\.  Run the main pipeline



&nbsp; python app/main.py





###### \# The demo will:

* Read a document from the data folder
* Parse and chunk the content
* Store chunks in both Vector DB and SQL DB
* Perform a sample semantic search



 - - - - - -



###### &nbsp;# Benchmark 



* A simple recall-based benchmark is included to validate retrieval quality.



&nbsp;python benchmarks/benchmark.py



 - - - - - -



###### \# Architecture Decisions 



* Word-based chunking with overlap was chosen to ensure language-agnostic support and better semantic continuity.
* Dual storage was used
* Vector DB for semantic similarity search
* SQL DB for raw text and metadata storage
* The system is modular and easily extensible for future RAG enhancements such as Graph RAG or RAPTOR.



 - - - - - -



###### **# Notes**



* Arabic text may appear reversed in Windows terminals due to RTL rendering limitations.

The actual stored content is correct and can be verified via output.txt.



* Streamlit UI was intentionally omitted to prioritize code clarity and core functionality.



# Contact*



* Name: Shahad Alzahrani
* Email : itshahdalzahrani@gmail.com
* phone: (+966) 56511310





\

Thank you  for reviewing this sumbmission .
