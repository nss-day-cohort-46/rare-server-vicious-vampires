from models import User
import sqlite3
import json


def get_all_users():

    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.created_on,
            u.active
        FROM User u
        """)

        users = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post = User(row['id'],
                    row['first_name'],
                    row['last_name'],
                    row['email'],
                    row['bio'],
                    row['username'],
                    row['password'],
                    row['created_on'],
                    row['active'])

            users.append(post.__dict__)

    return json.dumps(users)

def get_single_user(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.created_on,
            u.active
        FROM User u
        WHERE u.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        post = User(data['id'],
                    data['first_name'],
                    data['last_name'],
                    data['email'],
                    data['bio'],
                    data['username'],
                    data['password'],
                    data['created_on'],
                    data['active'])

        return json.dumps(post.__dict__)

def create_user(new_user):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO User
            ( first_name, last_name, email, bio, username, password, created_on, active )
        VALUES
            ( ?, ?, ?, ?, ?, ?);
        """, (new_post['first_name'],
            new_post['last_name'],
            new_post['email'],
            new_post['bio'],
            new_post['username'],
            new_post['password'],
            new_post['created_on'],
            new_post['active'], ))

        id = db_cursor.lastrowid
        new_user['id'] = id

    return json.dumps(new_user)