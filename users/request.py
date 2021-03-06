from models import User, user
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

            user = User(row['id'],
                    row['first_name'],
                    row['last_name'],
                    row['email'],
                    row['bio'],
                    row['username'],
                    row['password'],
                    row['created_on'],
                    row['active'])

            users.append(user.__dict__)

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

        user = User(data['id'],
                    data['first_name'],
                    data['last_name'],
                    data['email'],
                    data['bio'],
                    data['username'],
                    data['password'],
                    data['created_on'],
                    data['active'])

        return json.dumps(user.__dict__)

def create_user(new_user):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO User
            ( username, first_name, last_name, email, password )
        VALUES
            ( ?, ?, ?, ?, ? );
        """, (new_user['username'],
            new_user['first_name'],
            new_user['last_name'],
            new_user['email'],
            new_user['password'], ))

        id = db_cursor.lastrowid
        new_user['id'] = id

        registered_user = {
            "valid": "valid",
            "token": id
        }

    return json.dumps(registered_user)

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