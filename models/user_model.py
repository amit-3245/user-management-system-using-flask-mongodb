from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from database.mongodb import get_users_collection
from bson.objectid import ObjectId


users = get_users_collection()


def create_user(name, email, password, role="user"):
    """
    Create a new user
    """
    # Check if user already exists
    if users.find_one({"email": email}):
        return {"status": False, "message": "User already exists"}

    hashed_password = generate_password_hash(password)

    user = {
        "name": name,
        "email": email,
        "password": hashed_password,
        "role": role,
        "created_at": datetime.utcnow()
    }

    users.insert_one(user)
    return {"status": True, "message": "User created successfully"}


def authenticate_user(email, password):
    """
    Authenticate user during login
    """
    user = users.find_one({"email": email})
    if not user:
        return None

    if check_password_hash(user["password"], password):
        return user

    return None


def get_all_users():
    """
    Fetch all users
    """
    return list(users.find({}, {"password": 0}))  # hide password


def get_user_by_id(user_id):
    """
    Get single user by ID
    """
    return users.find_one(
        {"_id": ObjectId(user_id)},
        {"password": 0}
    )


def update_user(user_id, name, email, role):
    """
    Update user details
    """
    users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {
            "name": name,
            "email": email,
            "role": role
        }}
    )


def delete_user(user_id):
    """
    Delete user
    """
    users.delete_one({"_id": ObjectId(user_id)})
