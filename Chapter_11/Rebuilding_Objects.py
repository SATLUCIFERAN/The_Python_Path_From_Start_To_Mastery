
import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

def dict_to_book(d):
    """
    A custom hook that checks if a dictionary represents a Book and rebuilds it.
    """
    # Look for specific keys to identify a "Book" dictionary
    if 'title' in d and 'author' in d:
        return Book(d['title'], d['author'])
    # If it's not a book, just return the dictionary as is
    return d

json_string = '{"book_data": {"title": "The Hitchhiker\'s Guide", "author": "Douglas Adams"}}'

# The hook is called on the inner dictionary, converting it to a Book object
data = json.loads(json_string, object_hook=dict_to_book)

# The result is a dictionary with a Book object inside
print(data)
print(f"Type of book_data: {type(data['book_data'])}")
