import sqlite3

DATABASE = "users.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def insert_user(email, password_hash, full_name, dob):
    conn = get_connection()

    conn.execute(
        """
        INSERT INTO users(email,password_hash,full_name,date_of_birth)
        VALUES(?,?,?,?)
        """,
        (email, password_hash, full_name, dob)
    )

    conn.commit()
    conn.close()


def get_user_by_email(email):
    conn = get_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    ).fetchone()

    conn.close()

    return user


def update_profile(email, full_name, dob):
    conn = get_connection()

    conn.execute(
        """
        UPDATE users
        SET full_name=?, date_of_birth=?
        WHERE email=?
        """,
        (full_name, dob, email)
    )

    conn.commit()
    conn.close()


def save_reset_token(email, token, expires):
    conn = get_connection()

    conn.execute(
        """
        UPDATE users
        SET reset_token=?, reset_expires=?
        WHERE email=?
        """,
        (token, expires, email)
    )

    conn.commit()
    conn.close()


def get_user_by_token(token):
    conn = get_connection()

    user = conn.execute(
        """
        SELECT * FROM users
        WHERE reset_token=?
        """,
        (token,)
    ).fetchone()

    conn.close()

    return user


def update_password(email, password_hash):
    conn = get_connection()

    conn.execute(
        """
        UPDATE users
        SET password_hash=?,
            reset_token=NULL,
            reset_expires=NULL
        WHERE email=?
        """,
        (password_hash, email)
    )

    conn.commit()
    conn.close()