from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = "Rimon"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float =Field(gt=0,lt=4, default=5, description='A decimal value representing the cgpa of the student')

new_student={'age':'24', 'email':'abc@gmail.com'}

student=Student(**new_student)

print(student)

student_dict = dict(student)

print(student_dict['age'])