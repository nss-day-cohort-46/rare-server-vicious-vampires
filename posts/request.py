from models import Category
from models import Post
from models import User
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
            p.approved,
            c.label,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.created_on,
            u.active
        FROM Post p
        JOIN Category c
            ON c.id = p.category_id
        JOIN User u
            ON u.id = p.user_id
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

            category = Category(row['id'], row['label'])
            post.category = category.__dict__
            
            user = User(row['id'],
                        row['first_name'],
                        row['last_name'],
                        row['email'],
                        row['bio'],
                        row['username'],
                        row['password'],
                        row['created_on'],
                        row['active'], )
            post.user = user.__dict__

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
            p.approved,
            c.label,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.created_on,
            u.active
        FROM Post p
        JOIN Category c
            ON c.id = p.category_id
        JOIN User u
            ON u.id = p.user_id
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

        category = Category(data['id'], data['label'])
        post.category = category.__dict__

        user = User(data['id'],
                    data['first_name'],
                    data['last_name'],
                    data['email'],
                    data['bio'],
                    data['username'],
                    data['password'],
                    data['created_on'],
                    data['active'], )
        post.user = user.__dict__

        return json.dumps(post.__dict__) 

def create_post(new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Post
            ( user_id, category_id, title, publication_date, content, approved )
        VALUES
            ( ?, ?, ?, ?, ?, ? );
        """, (new_post['user_id'], new_post['category_id'], new_post['title'], new_post['publication_date'], new_post['content'], new_post['approved']))

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

