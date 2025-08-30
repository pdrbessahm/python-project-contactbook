import json, os
from pathlib import Path
from typing import Optional, Iterable
from .models import Contact


DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "contacts.json"


# make sure the storage files exists and has a valid initial structure
def _ensure_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True) 
    # creates the data/ folder if its missing
    if not DATA_FILE.exists():
        DATA_FILE.write_text(json.dumps({"seq": 0, "items": []}, ensure_ascii=False, indent=2), encoding="utf-8") 
        # creates an auto-id counter and an empty list of contacts if the json file doesnt exist yet

def _load() -> dict:
    # reads the whole json file into a python dictionary
    _ensure_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
        # centralizes reading logic so other functions dont duplicate it

def _save(data: dict) -> None:
    # persists the given dictionary back to disk as json
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        # its responsible for writing only, keeping format consistent

def all_contacts() -> Iterable[Contact]:
    # returns all contacts as objects
    data = _load() # loads the dictionary
    return [Contact(**it) for it in data ["items"]] 
    # convert each stored item into a contact object via unpacking (contact(**it))

def get_contact(contact_id: int) -> Optional[Contact]:
    # find one contact by ID
    for c in all_contacts():
        # runs a counter throughout the object dict list previously defined
        if c.id == contact_id:
            return c
            # if there is the actual id in the list
    return None

def add_contact(c: Contact) -> Contact:
    # insert a new contact and assigns a new auto-incremented id
    data = _load()
    # loads json
    data["seq"] += 1
    # increment them by one
    c.id = data["seq"]
    # adds c.id to the value counted before
    data["items"].append(c.__dict__)
    _save(data)
    return c
    # save the file and return the enriched contact object

def update_contact(c: Contact) -> Contact:
    # updates an existing contact by matching ids
    data = _load()
    for i, it in enumerate(data["items"]):
        if it["id"] == c.id:
        # creating a counter to match it ID to c ID, in other words, find the index that we want to update
            data["items"][i] = c.__dict__
            # replace the previous dictionary with the new information
            _save(data)
            # saves the new information
            return c
            # return the new information
    raise KeyError(f"Contact {c.id} not found")
    # raise an error it the id doesnt exists

def delete_contact(contact_id: int) -> None:
    # remove a contact by id
    data = _load()
    # loads json
    data["items"] = [it for it in data["items"] if it["id"] != contact_id]
    # selecting everythin except the matching id
    _save(data)