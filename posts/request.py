from models import Post
import sqlite3
import json


def get_all_posts():

    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content,
            p.approved
        FROM Post p
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post = Post(row['id'],
                    row['user_id'],
                    row['category_id'],
                    row['title'],
                    row['publication_date'],
                    row['content'],
                    row['approved'])

            posts.append(post.__dict__)

    return json.dumps(posts)

def get_single_post(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content,
            p.approved
        FROM Post p
        WHERE p.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        post = Post(data['id'],
                    data['user_id'],
                    data['category_id'],
                    data['title'],
                    data['publication_date'],
                    data['content'],
                    data['approved'])

        return json.dumps(post.__dict__) 

def create_post(new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Post
            ( label )
        VALUES
            ( ?);
        """, (new_post['label'], ))

        id = db_cursor.lastrowid
        new_post['id'] = id

    return json.dumps(new_post)

def delete_post(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE from Post
        WHERE id = ?
        """, ( id, ))

def update_post(id, updated_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Post
            SET
                user_id = ?,
                category_id = ?,
                title = ?,
                publication_date = ?,
                content = ?,
                approved = ?
        WHERE id = ?
        """, (updated_post['user_id'],
            updated_post['category_id'],
            updated_post['title'],
            updated_post['publication_date'],
            updated_post['content'],
            updated_post['approved'], id ))

        rows_affected = db_cursor.rowcount
    
    if rows_affected == 0:
        return False
    else: 
        return True

def get_posts_by_user(user_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content,
            p.approved
        FROM Post p
        WHERE p.user_id = ?
        """, (user_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'],
                    row['user_id'],
                    row['category_id'],
                    row['title'],
                    row['publication_date'],
                    row['content'],
                    row['approved'])

            posts.append(post.__dict__)

    return json.dumps(posts)

