from sqlmodel import SQLModel, create_engine, Session, select
from memberModel import Member
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)

def add_member(email: str, name: str, department_id: int, role: int, invite_link: str = None) -> Member:
    with get_session() as session:
        member = Member(
            email=email,
            name=name,
            department_id=department_id,
            role=role,
            invite_link=invite_link
        )
        session.add(member)
        session.commit()
        session.refresh(member)
        return member


def get_member_by_invite(invite_link: str) -> Member | None:
    with get_session() as session:
        statement = select(Member).where(Member.invite_link == invite_link)
        result = session.exec(statement).first()
        return result
