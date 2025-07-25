import functools
import json
import datetime
import os

def log_cli_parameters(log_file="cli_params_log.json"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            entry = {
                "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "function": func.__name__,
                "args": args,
                "kwargs": kwargs
            }

            # Load existing log
            if os.path.exists(log_file):
                with open(log_file, "r") as file:
                    log_data = json.load(file)
            else:
                log_data = []

            log_data.append(entry)

            # Write updated log
            with open(log_file, "w") as file:
                json.dump(log_data, file, indent=2)

            return func(*args, **kwargs)
        return wrapper
    return decorator
@log_cli_parameters()
def create_user(username, email, admin=False):
    print(f"User '{username}' with email '{email}' created. Admin: {admin}")
create_user("anu", "anu@example.com")
create_user("banu", "banu@example.com", admin=True)
