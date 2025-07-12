# Social Media Post Scheduler

posts = []

def show_menu():
    print("\n📲 Social Media Post Scheduler")
    print("1. View scheduled posts")
    print("2. Add a new post")
    print("3. Add a priority post")
    print("4. Post (remove the next one)")
    print("5. Exit")

def view_posts():
    if not posts:
        print("🕳️ No posts scheduled yet.")
    else:
        print("\n🗓️ Scheduled Posts:")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post}")

def add_post():
    title = input("Enter post title: ").strip().capitalize()
    posts.append(title)
    print(f"✅ Post '{title}' scheduled.")

def add_priority_post():
    title = input("Enter PRIORITY post title: ").strip().capitalize()
    posts.insert(0, title)
    print(f"🚨 Priority post '{title}' added to the top.")

def remove_post():
    if not posts:
        print("⚠️ No posts to publish.")
    else:
        posted = posts.pop(0)
        print(f"📤 Posted: '{posted}'")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1–5): ")

    if choice == "1":
        view_posts()
    elif choice == "2":
        add_post()
    elif choice == "3":
        add_priority_post()
    elif choice == "4":
        remove_post()
    elif choice == "5":
        print("🛑 Exiting Post Scheduler. Happy posting! 📅")
        break
    else:
        print("❌ Invalid choice. Try again.")
