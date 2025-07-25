import functools

def html_wrapper(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            return f"<{tag}>{content}</{tag}>"
        return wrapper
    return decorator
@html_wrapper("div")
@html_wrapper("h2")
@html_wrapper("p")
def get_welcome_message():
    return "Welcome to the Decorator-Powered Site!"
print(get_welcome_message())
@html_wrapper("section")
@html_wrapper("article")
@html_wrapper("h1")
def show_title():
    return "Python Decorators Rock!"
print(show_title())
