"""User ORM model."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import BigInteger, DateTime, SmallInteger, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_account: Mapped[str] = mapped_column(String(256))
    user_password: Mapped[str] = mapped_column(String(512))
    user_name: Mapped[str | None] = mapped_column(String(256), nullable=True)
    user_avatar: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    user_profile: Mapped[str | None] = mapped_column(String(512), nullable=True)
    user_role: Mapped[str] = mapped_column(String(64))
    is_delete: Mapped[int] = mapped_column(SmallInteger, default=0)
    create_time: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.now())
    update_time: Mapped[datetime | None] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )
