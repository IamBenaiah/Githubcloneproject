import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_django_project.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
author1 = Author.objects.create(name="Chinua Achebe")
author2 = Author.objects.create(name="Wole Soyinka")

book1 = Book.objects.create(title="Things Fall Apart", author=author1)
book2 = Book.objects.create(title="The Lion and the Jewel", author=author2)

library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)  # ManyToMany relationship

librarian = Librarian.objects.create(name="Mr. John", library=library)

# Queries
print("Books by Chinua Achebe:", Book.objects.filter(author=author1))
print("Books in Central Library:", library.books.all())
print("Librarian of Central Library:", library.librarian.name)
