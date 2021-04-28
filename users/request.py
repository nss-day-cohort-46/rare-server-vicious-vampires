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
            ( ?, ?, ?, ?, ?, ?, ?, ?);
        """, (new_user['first_name'],
            new_user['last_name'],
            new_user['email'],
            new_user['bio'],
            new_user['username'],
            new_user['password'],
            new_user['created_on'],
            new_user['active'], ))

        id = db_cursor.lastrowid
        new_user['id'] = id

    return json.dumps(new_user)

def get_user_by_email_and_password(email_and_password):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        email = email_and_password["username"]
        password = email_and_password["password"]

        db_cursor.execute("""
        SELECT u.id
        FROM User u
        WHERE u.email = ? AND u.password = ?
        """, (email, password))

        data = db_cursor.fetchone()

        user = {
            "valid": "valid",
            "token": data['id']
        }
    return json.dumps(user)