# Contact Book 🧧 Project

## About This Project

This is a simple terminal-based CRUD system built with python in order to remember what I did while playing with Java and to practice what I have learned after finishing the 4 hour MySQL beginner course from FreeCodeCamp.

## Features
- Add New Contacts
- List All Contacts
- Update Contact Information
- Delete Contacts

## Files Explanations

- data/
    - contacts.json -> Is holding my database which later will be swapped out for MySQL.

- src/contactbook/
    - cli.py -> input and output, basically the terminal input
    - models.py -> defines what a contact look like
    - services.py -> create/read/update/delete functions
    - storage.py -> deals with reading/writing json or csv

- tests/
    - test_services.py -> just to look more professional, yknow?

