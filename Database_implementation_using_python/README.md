# Python PostgreSQL Database Operations

A simple Python project demonstrating how to connect to a PostgreSQL database using the `psycopg2` library and perform basic database operations such as creating tables, inserting data, fetching records, using `WHERE` conditions, accepting user input, and truncating a table.

## Features

* Connects Python to a PostgreSQL database
* Creates a `users` table
* Inserts predefined user records
* Fetches and displays all records
* Accepts user input and inserts it dynamically
* Uses parameterized SQL queries for user input
* Retrieves records using a `WHERE` condition
* Truncates the table using `TRUNCATE`
* Closes the database connection after execution

## Technologies Used

* **Python**
* **PostgreSQL**
* **psycopg2**

## Database Structure

The program creates a table named `users` with the following columns:

| Column | Data Type | Description      |
| ------ | --------- | ---------------- |
| `name` | TEXT      | Name of the user |
| `age`  | INTEGER   | Age of the user  |
| `id`   | INTEGER   | User ID          |

## Prerequisites

Make sure you have the following installed:

1. Python
2. PostgreSQL
3. `psycopg2` Python library

Install `psycopg2` using:

```bash
pip install psycopg2
```

## PostgreSQL Configuration

The program connects to the PostgreSQL server using:

```python
psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="YOUR_PASSWORD",
    host="localhost",
    port="5432"
)
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

> **Security Note:** Avoid storing your real database password directly in code, especially when uploading the project to GitHub. Use environment variables instead.

## How the Program Works

### 1. Establish Database Connection

The program first connects to the PostgreSQL database using `psycopg2`.

```python
conn = psycopg2.connect(...)
cursor = conn.cursor()
```

### 2. Create the Table

The `create_table()` function creates the `users` table if it does not already exist.

```sql
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    age INTEGER,
    id INTEGER
);
```

### 3. Insert Initial Data

The `insert_data()` function inserts two predefined users:

* Anna
* Bob

### 4. Display Data

The `display_data()` function retrieves all records using:

```sql
SELECT * FROM users;
```

The results are then displayed using `fetchall()`.

### 5. Insert Data Using User Input

The program asks the user to enter:

* Name
* Age
* ID

The values are inserted using a parameterized query:

```python
cursor.execute(
    '''INSERT INTO users (name, age, id) VALUES (%s, %s, %s)''',
    (name, age, id)
)
```

Using parameterized queries helps prevent SQL injection.

### 6. SELECT with WHERE

The program retrieves users whose age is greater than 20:

```sql
SELECT * FROM users WHERE age > 20;
```

### 7. TRUNCATE

Finally, the program removes all records from the `users` table:

```sql
TRUNCATE TABLE users;
```

The table itself remains available, but all rows are deleted.

## Example Output

```text
Connection established successfully
Table created successfully
Data inserted successfully

('Anna', 12, 1)
('Bob', 25, 2)

Enter name: Charlie
Enter age: 30
Enter id: 3

Data inserted successfully
Current data in the table:

('Anna', 12, 1)
('Bob', 25, 2)
('Charlie', 30, 3)

Users older than 20:
('Bob', 25, 2)
('Charlie', 30, 3)

Table truncated successfully
```

## SQL Operations Covered

This project demonstrates the following basic SQL operations:

* `CREATE TABLE`
* `INSERT INTO`
* `SELECT`
* `WHERE`
* `TRUNCATE`

## Learning Outcomes

After completing this project, you will understand:

* How Python connects to PostgreSQL
* How to execute SQL queries from Python
* How to insert and retrieve database records
* How to accept user input and store it in a database
* How parameterized queries work
* How `WHERE` filters database records
* The difference between deleting records and truncating a table

## How to Run

1. Start your PostgreSQL server.
2. Make sure the `postgres` database exists.
3. Update the database password in the Python file.
4. Run the Python script:

```bash
python filename.py
```

5. Follow the instructions displayed in the terminal.

## Note

The program uses `TRUNCATE TABLE users` at the end, so all records inserted during the execution will be removed before the program finishes.
