import sqlite3


def init_db():
    conn = sqlite3.connect("money_exchange.db")
    cursor = conn.cursor()

    # users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # currencies table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS currencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            symbol TEXT
        )
    ''')

    # wallets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wallets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            currency_id INTEGER NOT NULL,
            balance REAL DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                   
            UNIQUE(user_id, currency_id),

            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (currency_id) REFERENCES currencies(id)
        )
    ''')

    # transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            from_currency_id INTEGER NOT NULL,
            to_currency_id INTEGER NOT NULL,

            from_amount REAL NOT NULL,
            to_amount REAL NOT NULL,

            exchange_rate REAL NOT NULL,

            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (from_currency_id) REFERENCES currencies(id),
            FOREIGN KEY (to_currency_id) REFERENCES currencies(id)
        )
    ''')

    # exchange_rates table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            from_currency_id INTEGER NOT NULL,
            to_currency_id INTEGER NOT NULL,

            rate REAL NOT NULL,

            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (from_currency_id) REFERENCES currencies(id),
            FOREIGN KEY (to_currency_id) REFERENCES currencies(id),

            UNIQUE(from_currency_id, to_currency_id)
        )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()