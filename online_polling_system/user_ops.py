# user_ops.py

def has_voted(user_set, user_id, question):
    return (user_id, question) in user_set

def mark_voted(user_set, user_id, question):
    user_set.add((user_id, question))
