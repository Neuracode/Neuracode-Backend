from typing import List,Optional
from pydantic import BaseModel

class UserInfoRegister(BaseModel):
    name: str
    password: str
    email: str

class UserInfoLogin(BaseModel):
    name: str
    password: str
   
class Authorization(BaseModel):
    token: str
 
class CreateCourseAuthorization(BaseModel):
    token: str
    courseName: str
    courseDescription: Optional[str] = ""
    courseTags: Optional[List[str]] = []
    lecturer: Optional[List[str]] = []
    lectureHours: Optional[List[str]] = []
    courseLength: Optional[str] = ""
    courseStart: Optional[str] = ""
    courseEnd: Optional[str] = ""
    
class CourseAuthorization(BaseModel):
    token: str
    courseName: str
    parameter: str
    newValueOfParameter: str
    
class CredentialChangeAuthorization(BaseModel):
    name: str
    parameter: str
    newValueOfParameter: str
    token: str

class VolunteeringHoursAppend(BaseModel):
    token: str
    title: str
    description: str
    hours: int
    
class VolunteeringAuthorization(BaseModel):
    token: str
    taksId: str
    decision: bool