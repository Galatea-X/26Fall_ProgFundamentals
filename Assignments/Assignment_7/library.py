import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Remove any existing books table
cursor.execute("DROP TABLE IF EXISTS books")

# Create the books table
cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        genre TEXT,
        copies INTEGER,
        rating INTEGER
    )
""")

# Add one book with a single INSERT statement
cursor.execute("""
    INSERT INTO books (id, title, author, year, genre, copies, rating)
    VALUES (1, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction', 5, 5)
""")

# Add the rest with executemany and ? placeholders
books = [
    (2, '1984', 'George Orwell', 1949, 'Fiction', 4, 5),
    (3, 'A Brief History of Time', 'Stephen Hawking', 1988, 'Science', 3, 4),
    (4, 'The Da Vinci Code', 'Dan Brown', 2003, 'Mystery', 6, None),
    (5, 'Pride and Prejudice', 'Jane Austen', 1813, 'Fiction', 2, 5),
    (6, 'Sapiens', 'Yuval Noah Harari', 2011, 'History', 3, 4),
    (7, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 2005, 'Mystery', 1, None),
    (8, 'Cosmos', 'Carl Sagan', 1980, 'Science', 4, 5),
    (9, 'Guns, Germs, and Steel', 'Jared Diamond', 1997, 'History', 2, 4),
]

cursor.executemany("""
    INSERT INTO books (id, title, author, year, genre, copies, rating)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", books)

conn.commit()

# 1. Books published after 1990
print("Books published after 1990:")
cursor.execute("SELECT title, author FROM books WHERE year > 1990")
for row in cursor.fetchall():
    print(f"  {row[0]} by {row[1]}")

# 2. Fiction books with more than 2 copies (AND)
print("\nFiction books with more than 2 copies:")
cursor.execute("SELECT title FROM books WHERE genre = 'Fiction' AND copies > 2")
for row in cursor.fetchall():
    print(f"  {row[0]}")

# 3. Books published before 1900 or rated 5 (OR)
print("\nBooks published before 1900 or rated 5:")
cursor.execute("SELECT title FROM books WHERE year < 1900 OR rating = 5")
for row in cursor.fetchall():
    print(f"  {row[0]}")

# 4. Books that are not in the Mystery genre (NOT)
print("\nBooks that are not Mystery:")
cursor.execute("SELECT title FROM books WHERE NOT genre = 'Mystery'")
for row in cursor.fetchall():
    print(f"  {row[0]}")

# 5. Books in either Science or History genre (IN)
print("\nBooks in Science or History genre:")
cursor.execute("SELECT title FROM books WHERE genre IN ('Science', 'History')")
for row in cursor.fetchall():
    print(f"  {row[0]}")

# 6. Authors whose names start with a user-provided letter (LIKE)
letter = input("\nEnter a letter to search for authors: ").strip().upper()
print(f"Authors whose names start with '{letter}':")
cursor.execute("SELECT author FROM books WHERE author LIKE ?", (letter + '%',))
for row in cursor.fetchall():
    print(f"  {row[0]}")

# 7. Books that have no rating (IS NULL)
print("\nBooks with no rating:")
cursor.execute("SELECT title FROM books WHERE rating IS NULL")
for row in cursor.fetchall():
    print(f"  {row[0]}")

# Close the connection
conn.close()
print("\nDatabase connection closed.")
