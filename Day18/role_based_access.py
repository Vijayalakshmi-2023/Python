import functools
import datetime

# Simulated current user (can be replaced with actual session/user context)
current_user = {"username": "vijayalakshmi", "role": "user"}

# Access control decorator
def access_control(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_role = current_user.get("role", None)
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if user_role != required_role:
                # Log denied access
                print(f"[{time}] ACCESS DENIED to '{func.__name__}'")
                print(f"  User: {current_user['username']} (Role: {user_role})")
                print(f"  Required Role: {required_role}")
                print("-" * 50)
                return f"Access Denied: '{required_role}' role required"
            # If allowed
            return func(*args, **kwargs)
        return wrapper
    return decorator
@access_control("admin")
def delete_user(user_id):
    return f"User {user_id} deleted."

@access_control("user")
def view_profile():
    return f"Profile of {current_user['username']}"
# 1. Current user is 'user'
print(view_profile())        # ✅ Allowed
print(delete_user(123))      # ❌ Denied

# 2. Switch to admin role
current_user["role"] = "admin"
print(delete_user(456))      # ✅ Allowed
