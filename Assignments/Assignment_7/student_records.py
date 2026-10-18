import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("StudentRecords.db")
cursor = conn.cursor()

# Remove any existing StudentRecords table, then create it
cursor.execute("DROP TABLE IF EXISTS StudentRecords")
cursor.execute("""
    CREATE TABLE StudentRecords (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Age INTEGER,
        Major TEXT NOT NULL
    )
""")

# Add 5 students with fixed values
students = [
    (1, "Alice Johnson", 20, "Computer Science"),
    (2, "Bob Smith", 21, "Biology"),
    (3, "Carol Davis", 19, "History"),
    (4, "David Wilson", 22, "Mathematics"),
    (5, "Emma Brown", 20, "Psychology"),
]

cursor.executemany("""
    INSERT INTO StudentRecords (ID, Name, Age, Major)
    VALUES (?, ?, ?, ?)
""", students)
conn.commit()

# Print each student's name, age, and major (no ID)
print("Current students:")
cursor.execute("SELECT Name, Age, Major FROM StudentRecords")
for row in cursor.fetchall():
    print(f"  Name: {row[0]}, Age: {row[1]}, Major: {row[2]}")

# Ask whether to add a new student (accept yes/no in any capitalization)
while True:
    answer = input("\nDo you want to add a new student? (yes/no): ").strip().lower()
    if answer in ("yes", "no"):
        break
    print("Please enter 'yes' or 'no'.")

if answer == "yes":
    # Get and validate name
    while True:
        name = input("Enter the student's name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please try again.")

    # Get and validate age (must be a whole number)
    while True:
        age_input = input("Enter the student's age: ").strip()
        try:
            age = int(age_input)
            break
        except ValueError:
            print("Age must be a whole number. Please try again.")

    # Get and validate major
    while True:
        major = input("Enter the student's major: ").strip()
        if major:
            break
        print("Major cannot be empty. Please try again.")

    # Find the next available ID
    cursor.execute("SELECT MAX(ID) FROM StudentRecords")
    max_id = cursor.fetchone()[0]
    new_id = (max_id or 0) + 1

    # Insert using ? placeholders
    cursor.execute("""
        INSERT INTO StudentRecords (ID, Name, Age, Major)
        VALUES (?, ?, ?, ?)
    """, (new_id, name, age, major))

    print(f"\nStudent '{name}' added successfully with ID {new_id}.")

# Commit changes and close the connection
conn.commit()
conn.close()
print("Database connection closed.")
