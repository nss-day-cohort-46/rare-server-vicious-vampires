from models import Comment
import sqlite3
import json

def get_all_comments():

    with sqlite3.connect(".rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id
            c.post_id
            c.author_id
            c.content
            c.created_on
        FROM Comments c
        """)

        comments = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            comment = Comment(row['id'],
                        row['post_id'],
                        row['author_id'],
                        row['content'],
                        row['created_on'])
            
            comments.append(comment.__dict__)

    return json.dumps(comments)

def create_comment(new_comment):
    with sqlite3.connect(".rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.exectue("""
        INSERT INTO Comments
            (post_id, author_id, content, created_on)
        VALUES
            ( ?, ?, ?, ?);
        """, (new_comment['post_id'],
             new_comment['author_id'],
             new_comment['content'],
             new_comment['created_on'] ))

        id = db_cursor.lastrowid
        new_comment['id'] = id

    return json.dumps(new_comment)

def delete_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE from Comment
        WHERE id = ?
        """, ( id, ))

def update_comment(id, updated_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comment
            SET
                post_id = ?,
                author_id = ?,
                content = ?,
                created_on = ?,
        WHERE id = ?
        """, (updated_comment['post_id'],
            updated_comment['author_id'],
            updated_comment['content'],
            updated_comment['created_on'] ))
                        
        rows_affected = db_cursor.rowcount
    
    if rows_affected == 0:
        return False
    else:
        return True

def get_comment_by_post(post_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id
            c.post_id
            c.author_id
            c.content
            c.created_on
        FROM Comments c
        WHERE c.post_id = ?
        """, (post_id,))

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'],
                    row['post_id'],
                    row['author_id'],
                    row['content'],
                    row['created_on'],)

            comments.append(comment.__dict__)

    return json.dumps(comments)