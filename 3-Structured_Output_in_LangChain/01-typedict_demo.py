from typing import TypedDict

class Students(TypedDict):
    name: str
    id: int
    section: str

student01: Students = {
    'name':"Rimon",
    'id': 12345678,
    'section':'59A'
}

print(student01)