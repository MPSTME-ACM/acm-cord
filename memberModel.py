from sqlmodel import SQLModel, Field

class Member(SQLModel, table=True):
    __tablename__ = "muncord_members"
    email: str = Field(nullable=False, max_length=150)
    name: str = Field(nullable=False, max_length=75)
    department_id: int = Field(nullable=False)
    role: int = Field(nullable=False, default=0)
    invite_link: str = Field(index=True, primary_key=True, nullable=False)