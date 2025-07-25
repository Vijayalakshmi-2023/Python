import functools
import datetime

# Logger decorator
def api_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            result = func(*args, **kwargs)
            status = "Success"
        except Exception as e:
            result = None
            status = f"Fail: {e}"
        
        # Logging details
        print(f"[{time}] Function: {func.__name__}")
        print(f"  Args: {args}")
        print(f"  Kwargs: {kwargs}")
        print(f"  Status: {status}")
        print("-" * 50)
        return result
    return wrapper
@api_logger
def fetch_user_data(user_id):
    if user_id <= 0:
        raise ValueError("Invalid user ID")
    return {"user_id": user_id, "name": "John Doe"}

@api_logger
def update_user_profile(user_id, **profile_data):
    if not profile_data:
        raise ValueError("No data to update")
    return {"user_id": user_id, "updated": profile_data}
# Successful API calls
fetch_user_data(101)
update_user_profile(101, name="Alice", email="alice@example.com")

# Failing API calls
fetch_user_data(-1)
update_user_profile(102)
