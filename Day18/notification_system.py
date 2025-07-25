import functools

def notify_with(header="", footer=""):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(header)
            result = func(*args, **kwargs)
            print(footer)
            return result
        return wrapper
    return decorator
@notify_with(
    header="🔔 Notification Start: New Message",
    footer="✅ Notification End"
)
def display_message(msg):
    print(f"📨 {msg}")
    return "Displayed successfully"
result = display_message("You have 3 new updates.")
print("Return Value:", result)
