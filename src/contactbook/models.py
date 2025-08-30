from dataclasses import dataclass

# importing the dataclass decorator
# a decorator is a tool that adds functionality to a class automatically
# this is saving me from writing constructors like __init__, __repr__ and __eq__.

@dataclass

# this is telling python that the class below is holding actual data and I need the system to auto-generate the methods

class Contact:
    id: int
    name: str
    email: str | None = None
    phone: str | None = None

# I am setting up how a contact should look like in my program so i can determine a pattern for all contact 
# every contact must have a name and an id but there is no need to fill the email and phone columns at first, so i've settled up this condition with "| None = None "
