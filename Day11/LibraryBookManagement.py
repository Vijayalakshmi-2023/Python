# Library Book Management

# Books available in different branches
branch_a_books = {"The Great Gatsby", "1984", "To Kill a Mockingbird", "Moby Dick"}
branch_b_books = {"1984", "To Kill a Mockingbird", "The Catcher in the Rye", "War and Peace"}
branch_c_books = {"Moby Dick", "War and Peace", "The Odyssey", "1984"}

# All unique books available across all branches (union)
all_books = branch_a_books.union(branch_b_books, branch_c_books)
print("All available books across branches:", all_books)

# Books common to all branches (intersection)
common_books = branch_a_books.intersection(branch_b_books, branch_c_books)
print("Books available in all branches:", common_books)

# Books only in Branch A (difference)
only_branch_a = branch_a_books.difference(branch_b_books, branch_c_books)
print("Books only in Branch A:", only_branch_a)

# Books only in Branch B (difference)
only_branch_b = branch_b_books.difference(branch_a_books, branch_c_books)
print("Books only in Branch B:", only_branch_b)

# Books only in Branch C (difference)
only_branch_c = branch_c_books.difference(branch_a_books, branch_b_books)
print("Books only in Branch C:", only_branch_c)
