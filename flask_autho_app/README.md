# Flask Login Page Project 

**If table has not been created in the database, remove and create the database again:**
```bash
rm project/db.sqlite
```

**Run python**
```bash
python3
```

**Import instantiated object of SQLAlchemy and function to create table in** `__init__.py`
```bash
>>> from project import db, create_app
>>> db.create_all(app=create_app())
>>> exit()
```

**Run sqlite3**
```bash
sqlite3 project/db.sqlite
sqlite> .tables
user
sqlite> .exit
```