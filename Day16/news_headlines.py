class PaginatedNewsIterator:
    def __init__(self, headlines, page_size=3):
        self.headlines = headlines
        self.page_size = page_size
        self.current_page = 0
        self.total_pages = (len(headlines) + page_size - 1) // page_size

    def display_page(self):
        start = self.current_page * self.page_size
        end = start + self.page_size
        page_data = self.headlines[start:end]
        print(f"\nPage {self.current_page + 1}/{self.total_pages}")
        for i, headline in enumerate(page_data, start=1):
            print(f"{start + i}. {headline}")

    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
        else:
            print("👉 You are on the last page.")

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        else:
            print("👈 You are on the first page.")
def run_news_pagination():
    headlines = [
        "Economy shows signs of recovery",
        "New species of bird discovered",
        "Tech stocks hit record highs",
        "Sports league resumes after break",
        "Local elections conclude peacefully",
        "Heavy rains expected tomorrow",
        "Travel restrictions ease up",
        "Health officials issue warning",
        "Historic summit scheduled",
        "Breakthrough in cancer research"
    ]

    paginator = PaginatedNewsIterator(headlines)

    while True:
        paginator.display_page()
        command = input("\nEnter command (n = next, p = previous, q = quit): ").lower()

        if command == 'n':
            paginator.next_page()
        elif command == 'p':
            paginator.previous_page()
        elif command == 'q':
            print("Exiting pagination.")
            break
        else:
            print("Invalid input. Use 'n', 'p', or 'q'.")

# Run it
run_news_pagination()
