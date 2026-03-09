import sqlite3
from database import get_db
from utils import hash_password, verify_password  # Import from utils instead


def register_user(username: str, password: str, membership: str) -> bool:
    """
    Register a new user with hashed password
    """
    conn = get_db()
    try:
        cursor = conn.cursor()
        hashed = hash_password(password)
        cursor.execute(
            "INSERT INTO users (username, password, membership) VALUES (?, ?, ?)",
            (username, hashed, membership)
        )
        conn.commit()
        print(f"✅ User {username} registered successfully with hashed password")
        return True
    except sqlite3.IntegrityError as e:
        print(f"❌ Integrity error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error registering user: {e}")
        return False
    finally:
        conn.close()


def authenticate_user(username: str, password: str):
    """
    Authenticate a user by verifying password hash
    """
    conn = get_db()
    try:
        cursor = conn.cursor()
        # Get the user by username first
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            # Convert Row object to dictionary
            user_dict = dict(user)
            # Verify password hash
            if verify_password(password, user_dict["password"]):
                print(f"✅ User {username} authenticated successfully")
                return {
                    "id": user_dict["id"],
                    "username": user_dict["username"],
                    "membership": user_dict["membership"]
                }
            else:
                print(f"❌ Invalid password for {username}")
        else:
            print(f"❌ User {username} not found")

        return None
    except Exception as e:
        print(f"❌ Error authenticating user: {e}")
        return None
    finally:
        conn.close()


def authenticate_user_by_username(username: str):
    """
    Get user by username without password verification
    """
    conn = get_db()
    try:
        c = conn.cursor()
        c.execute("SELECT id, username, membership FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        if user:
            return dict(user)
        return None
    except Exception as e:
        print(f"❌ Error fetching user: {e}")
        return None
    finally:
        conn.close()