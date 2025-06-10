#Challenge 1
# 1.  Create two dictionaries, Jane and John, to store contact information for Jane and John, respectively.
# 2.  Each contact dictionary contains keys for 'name,' 'phone,' and 'email' with corresponding values.
# 3.  Create a contacts dictionary and use the names 'Jane' and 'John' as keys, associating them with their respective contact dictionaries.
# 4.  Print Jane's contact information.
# 5.  Update Jane's phone number.
# 6.  Print Jane's updated contact information
jane = {
    "name": "Jane",
    "phone": "555-555-5555",
    "email": "jane",
}

john = {
    "name": "John",
    "phone": "555-123-1234",
    "email": "john",
}

contacts = {
    "Jane": jane,
    "John": john
}


contacts={"Jane":jane, "John":john}
print(jane)
jane["phone"] = "555-22222225"
print(jane)

#Challenge 2
# ● Create the dictionary: Begin with creating a dictionary where the keys are tuples of book titles and authors, and the values are genres.
# ● Add a New Book: Add a new entry to the dictionary with a tuple containing the title and author of the new book, and set its genre.
# ● Retrieve and Print Book Information: Retrieve and print the genre of a book given its title and author.
# Step 1: Create the dictionary
library = {
    ("To Kill a Mockingbird", "Harper Lee"): "Fiction",
    ("1984", "George Orwell"): "Dystopian",
    ("Pride and Prejudice", "Jane Austen"): "Romance"
}

# Step 2: Add a new book
new_book = ("The Hobbit", "J.R.R. Tolkien")
library[new_book] = "Fantasy"

# Step 3: Retrieve and print the genre of a specific book
search_book = ("1984", "George Orwell")
genre = library.get(search_book)

if genre:
    print(f"The genre of '{search_book[0]}' by {search_book[1]} is {genre}.")
else:
    print(f"Book '{search_book[0]}' by {search_book[1]} not found in the library.")
