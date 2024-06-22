# Project: Python - Object-relational mapping

### Overview
This project aims to bridge Python programming with relational databases using both direct SQL queries and SQLAlchemy, an Object-Relational Mapping (ORM) tool. By working through various tasks, you'll gain hands-on experience connecting to MySQL databases, querying data, and utilizing SQLAlchemy to interact with databases in a more Pythonic way.

### Learning Objectives
By the end of this project, you will:
- Understand the benefits of using Python for database interactions.
- Connect to a MySQL database using Python (MySQLdb).
- Execute SELECT and INSERT queries using MySQLdb.
- Implement safe query execution to prevent SQL injection attacks.
- Utilize SQLAlchemy to abstract database interactions and map Python classes to database tables.
- Create models using SQLAlchemy's ORM approach.
- Perform CRUD (Create, Read, Update, Delete) operations using SQLAlchemy.



### Background Context

In traditional database interactions without ORM, developers typically use libraries like `MySQLdb` to establish a direct connection to the MySQL database and execute SQL queries. For example:

```python
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

In contrast, using SQLAlchemy ORM abstracts the database interactions into Python objects. Here's how it simplifies database operations:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Define a base class for our ORM models
Base = declarative_base()

# Define a sample ORM model
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Connect to the MySQL database via SQLAlchemy engine
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)  # Create tables based on defined models

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Query and print states using ORM, no raw SQL required
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))

# Close the session
session.close()
```

### Setup Instructions

#### 1. Install and Activate Virtual Environment

First, create and activate a Python Virtual Environment (`venv`) to manage dependencies:

```bash
$ sudo apt-get install python3.8-venv  # Install venv if not already installed
$ python3 -m venv venv  # Create a virtual environment named 'venv'
$ source venv/bin/activate  # Activate the virtual environment
```

#### 2. Install MySQLdb Module (version 2.0.x)

Ensure MySQL is installed (see [How to install MySQL 8.0 in Ubuntu 20.04](https://example.com/mysql-installation-guide)) and then install `MySQLdb`:

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==2.0.x  # Replace '2.0.x' with the specific version
```

Verify installation in Python:

```python
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
>>> exit()
```

#### 3. Install SQLAlchemy Module (version 1.4.x)

Install SQLAlchemy for ORM functionality:

```bash
$ sudo pip3 install SQLAlchemy==1.4.x  # Replace '1.4.x' with the specific version
```

Verify installation in Python:

```python
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
>>> exit()
```

### Additional Notes

- **Warning Message**: If you encounter a warning related to `@@SESSION.GTID_EXECUTED` being deprecated, you can ignore it as it pertains to MySQL server configuration rather than SQLAlchemy usage.


#### Tasks
1. **Get all states**
   - Write a script to list all states from a database using MySQLdb.
   - Sort results by state id in ascending order.

2. **Filter states**
   - Write a script to list states whose names start with 'N' using MySQLdb.
   - Sort results by state id in ascending order.

3. **Filter states by user input**
   - Write a script to list states based on user-provided input using MySQLdb.
   - Prevent SQL injection vulnerabilities in the query.

4. **Cities by states**
   - Write a script to list all cities from a database using MySQLdb.
   - Sort results by city id in ascending order.

5. **All cities by state**
   - Write a script to list all cities of a specific state using MySQLdb.
   - Sort results by city id in ascending order.

6. **First state model**
   - Define a Python class `State` mapped to a MySQL table using SQLAlchemy.
   - Ensure the class inherits from `Base` and maps to the `states` table.
   - Include attributes for `id` (auto-generated), and `name`.

7. **All states via SQLAlchemy**
   - Write a script to fetch all `State` objects using SQLAlchemy.
   - Sort results by state id in ascending order.

8. **First state**
   - Write a script to fetch the first `State` object using SQLAlchemy.
   - Print the state in the format `<state id>: <state name>`.
   - Handle cases where the table is empty by printing "Nothing".

9. **Contains `a`**
   - Write a script to list all `State` objects containing the letter 'a' using SQLAlchemy.
   - Sort results by state id in ascending order.

10. **Get a state**
    - Write a script to fetch a specific `State` object by name using SQLAlchemy.
    - Print the state's id.

11. **Add a new state**
    - Write a script to add a new `State` object "Louisiana" using SQLAlchemy.
    - Print the new state's id after creation.

12. **Update a state**
    - Write a script to update the name of a `State` object where id=2 to "New Mexico" using SQLAlchemy.

13. **Delete states**
    - Write a script to delete all `State` objects with names containing the letter 'a' using SQLAlchemy.

14. **Cities in state**
    - Define a Python class `City` mapped to a MySQL table `cities` using SQLAlchemy.
    - Include attributes for `id`, `name`, and `state_id` (foreign key to `states.id`).
    - Write a script to fetch and print all `City` objects with their corresponding `State` name.

15. **City relationship**
    - Extend `State` class with a relationship to `City` class using SQLAlchemy.
    - Write a script to create a new `State` "California" with a linked `City` "San Francisco".

16. **List relationship**
    - Write a script to list all `State` objects and their linked `City` objects using SQLAlchemy.
    - Display results with proper formatting.

#### Project Structure
- Directory: `0x0F-python-object_relational_mapping`
- Key Files:
  - `0-select_states.py`
  - `1-filter_states.py`
  - `2-my_filter_states.py`
  - `3-my_safe_filter_states.py`
  - `4-cities_by_state.py`
  - `5-filter_cities.py`
  - `6-model_state.py`
  - `7-model_state_fetch_all.py`
  - `8-model_state_fetch_first.py`
  - `9-model_state_filter_a.py`
  - `10-model_state_my_get.py`
  - `11-model_state_insert.py`
  - `12-model_state_update_id_2.py`
  - `13-model_state_delete_a.py`
  - `model_state.py`
  - `model_city.py`
  - `14-model_city_fetch_by_state.py`
  - `relationship_state.py`
  - `relationship_city.py`
  - `100-relationship_states_cities.py`
  - `101-relationship_states_cities_list.py`

#### Repository
- GitHub repository: [alx-higher_level_programming](https://github.com/martinnyemba/alx-higher_level_programming)

This project will enhance your understanding of Python's capabilities in database management and deepen your knowledge of SQLAlchemy's ORM for efficient database operations.
