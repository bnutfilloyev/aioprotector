from sqlalchemy import BigInteger, Column

from bot.db.base import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, unique=True)

    def __repr__(self):
        return f"User #{self.id} {self.user_id}"
