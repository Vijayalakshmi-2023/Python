import functools

def validate_token(required_token):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            token = kwargs.pop("token", None)  # extract token from kwargs
            if token != required_token:
                print(f"Access denied: Invalid or missing API token for '{func.__name__}'")
                return "403 Forbidden: Invalid or missing token"
            return func(*args, **kwargs)
        return wrapper
    return decorator
@validate_token("secret_token")
def get_user_data(user_id):
    return {"user_id": user_id, "name": "John Doe"}

@validate_token("admin_token")
def delete_account(user_id):
    return f"Account {user_id} has been deleted."
print(get_user_data(101, token="secret_token"))      # ✅ Allowed
print(get_user_data(101))                            # ❌ Missing token
print(get_user_data(101, token="wrong_token"))       # ❌ Invalid token

print(delete_account(202, token="admin_token"))      # ✅ Allowed
print(delete_account(202, token="secret_token"))     # ❌ Invalid token
