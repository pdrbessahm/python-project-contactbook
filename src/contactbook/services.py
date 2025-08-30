from typing import Iterable
from .models import Contact
from . import storage


def list_contacts() -> Iterable[Contact]: 
    return sorted(storage.all_contacts(), key = lambda c: (c.name or "").lower())

def create_contact(name: str, email: str | None, phone: str | None) -> Contact:
    name = (name or "").strip()
    if not name:
        raise ValueError("Name is required")
    return storage.add_contact(Contact(id = 0, name = name, email = email or None, phone = phone or None))
    
def update_contact(contact_id: int, *, name: str | None = None, email: str | None = None, phone: str | None = None) -> Contact:
    c = storage.get_contact(contact_id)
    if not c:
        raise ValueError("Contact not found")
    if name is not None and name.strip():
        c.name = name.strip()
    if email is not None:
        c.email = email or None
    if phone is not None:
        c.phone = phone or None
    return storage.update_contact(c)
    
def delete_contact(contact_id: int) -> None:
    storage.delete_contact(contact_id)