import sqlite3
from utils import hash_password  # Import from utils instead of auth

DB_FILE = "database.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # Users table: username, password, membership
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        membership TEXT NOT NULL
    )
    """)

    # Payment information table
    c.execute("""
    CREATE TABLE IF NOT EXISTS payment_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        card_number TEXT NOT NULL,
        cardholder_name TEXT NOT NULL,
        expiry_month TEXT NOT NULL,
        expiry_year TEXT NOT NULL,
        cvv TEXT NOT NULL,
        street_address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        zip_code TEXT NOT NULL,
        payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    )
    """)

    # Create index for faster lookups
    c.execute("""
    CREATE INDEX IF NOT EXISTS idx_payment_info_user_id 
    ON payment_info (user_id)
    """)

    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def save_user_with_payment(username, password, membership, payment_data):
    """
    Save user and their payment information to the database
    Uses hashed password for security
    """
    conn = get_db()
    try:
        cursor = conn.cursor()

        # Hash the password before storing
        hashed_password = hash_password(password)

        # Insert user with hashed password
        cursor.execute("""
        INSERT INTO users (username, password, membership)
        VALUES (?, ?, ?)
        """, (username, hashed_password, membership))

        # Get the user_id of the newly created user
        user_id = cursor.lastrowid

        # Insert payment information
        cursor.execute("""
        INSERT INTO payment_info (
            user_id, card_number, cardholder_name, 
            expiry_month, expiry_year, cvv,
            street_address, city, state, zip_code
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            payment_data['card_number'],
            payment_data['cardholder_name'],
            payment_data['expiry_month'],
            payment_data['expiry_year'],
            payment_data['cvv'],
            payment_data['street_address'],
            payment_data['city'],
            payment_data['state'],
            payment_data['zip_code']
        ))

        conn.commit()
        print(f"✅ User {username} saved with payment info, ID: {user_id}")
        return user_id, None  # Success
    except sqlite3.IntegrityError as e:
        conn.rollback()
        print(f"❌ Integrity error: {e}")
        return None, f"Username already exists: {str(e)}"
    except Exception as e:
        conn.rollback()
        print(f"❌ Database error: {e}")
        return None, f"Database error: {str(e)}"
    finally:
        conn.close()


def get_user_payment_info(username):
    """
    Retrieve payment information for a specific user
    """
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT pi.* 
        FROM payment_info pi
        JOIN users u ON u.id = pi.user_id
        WHERE u.username = ?
        ORDER BY pi.payment_date DESC
        LIMIT 1
        """, (username,))

        result = cursor.fetchone()
        return dict(result) if result else None
    except Exception as e:
        print(f"Error retrieving payment info: {e}")
        return None
    finally:
        conn.close()


def get_all_users_with_payment():
    """
    Get all users with their most recent payment information
    (Useful for admin purposes)
    """
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT 
            u.id,
            u.username,
            u.membership,
            pi.card_number,
            pi.cardholder_name,
            pi.expiry_month,
            pi.expiry_year,
            pi.street_address,
            pi.city,
            pi.state,
            pi.zip_code,
            pi.payment_date
        FROM users u
        LEFT JOIN payment_info pi ON u.id = pi.user_id
        WHERE pi.id IN (
            SELECT MAX(id)
            FROM payment_info
            GROUP BY user_id
        ) OR pi.id IS NULL
        ORDER BY u.id DESC
        """)

        results = cursor.fetchall()
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error retrieving users with payment: {e}")
        return []
    finally:
        conn.close()


# Initialize DB on startup
init_db()