def lazy_contact_searcher(contacts, initial_letter):
    search_letter = initial_letter.lower()
    while True:
        for name, number in contacts.items():
            if name.lower().startswith(search_letter):
                new_letter = (yield f"{name}: {number}")
                if new_letter:
                    search_letter = new_letter.lower()
                    break  # Restart with new search key
        else:
            new_letter = (yield "No more contacts.")
            if new_letter:
                search_letter = new_letter.lower()
