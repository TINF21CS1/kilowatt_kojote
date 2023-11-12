import os
import sqlite3

con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))

def close_db(e=None):
    db = None#g.pop('db', None)

    if db is not None:
        db.close()

def init_db():

    with open(os.path.join(os.path.dirname(__file__), "schema.sql")) as schema:
        con.executescript(schema.read())
        con.commit()


def init_db_command():
    """Clear the existing data and create new tables."""
    #init_db()
    #click.echo('Initialized the database.')

if __name__ == "__main__":
    init_db()
