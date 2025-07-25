import functools

# Simulated user session
user = {"username": "guest", "is_logged_in": False}

def require_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not user.get("is_logged_in"):
            raise PermissionError(f"Access denied: '{func.__name__}' requires user login.")
        return func(*args, **kwargs)
    return wrapper
@require_login
def view_dashboard():
    return f"Welcome to the dashboard, {user['username']}."

@require_login
def perform_sensitive_action():
    return "Sensitive action performed successfully!"
# Not logged in
try:
    print(view_dashboard())
except PermissionError as e:
    print(e)

# Log the user in
user["username"] = "admin"
user["is_logged_in"] = True

# Try again
print(view_dashboard())
print(perform_sensitive_action())
