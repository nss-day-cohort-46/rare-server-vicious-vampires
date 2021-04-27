from models import Tag
import sqlite3
import json


def get_all_tags():

    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tag t
        """)

        tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            tag = Tag(row['id'],
                    row['label'],
                    )

            tags.append(tag.__dict__)

    return json.dumps(tags)

def delete_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE from Tag
        WHERE id = ?
        """, ( id, ))

def update_tag(id, updated_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Tag
            SET
                label = ?,
        WHERE id = ?
        """, (updated_tag['label'], ))

        rows_affected = db_cursor.rowcount
    
    if rows_affected == 0:
        return False
    else: 
        return True

def create_tag(new_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tag
            ( label )
        VALUES
            ( ?,);
        """, (new_tag['label'],
            ))

        id = db_cursor.lastrowid
        new_tag['id'] = id

    return json.dumps(new_tag)

def get_single_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tag t
        WHERE t.id = ?
        """, ( id, ))

        # Load the single result into memory
        row = db_cursor.fetchone()

        # Create an animal instance from the current row
        tag = Tag(row['id'], row['label']
        )

        return json.dumps(tag.__dict__)