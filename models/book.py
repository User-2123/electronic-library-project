class Book:
    def __init__(self, book_id, title, author, year, keywords):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.keywords = keywords

    def __str__(self):
        return f"{self.book_id}: {self.title} — {self.author} ({self.year})"
