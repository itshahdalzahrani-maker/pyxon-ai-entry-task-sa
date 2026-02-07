def chunk_text(text: str, max_words: int = 400, overlap: int = 50):
    words = text.split()

    if len(words) <= max_words:
        return [text]

    chunks = []
    start = 0

    while start < len(words):
        end = start + max_words
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))

        
        start = end - overlap

    return chunks