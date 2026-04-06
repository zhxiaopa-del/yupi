"""User request / response schemas."""

from __future__ import annotations

from pydantic import Field

from app.schemas.common import CamelBaseModel, LongIdModel, PageRequest, TimeModel


class UserRegisterRequest(CamelBaseModel):
    user_account: str = Field(alias="userAccount")
    user_password: str = Field(alias="userPassword")
    check_password: str = Field(alias="checkPassword")


class UserLoginRequest(CamelBaseModel):
    user_account: str = Field(alias="userAccount")
    user_password: str = Field(alias="userPassword")


class UserAddRequest(CamelBaseModel):
    user_account: str = Field(alias="userAccount")
    user_name: str | None = Field(default=None, alias="userName")
    user_avatar: str | None = Field(default=None, alias="userAvatar")
    user_profile: str | None = Field(default=None, alias="userProfile")
    user_role: str | None = Field(default=None, alias="userRole")


class UserUpdateRequest(CamelBaseModel):
    id: int
    user_name: str | None = Field(default=None, alias="userName")
    user_avatar: str | None = Field(default=None, alias="userAvatar")
    user_profile: str | None = Field(default=None, alias="userProfile")
    user_role: str | None = Field(default=None, alias="userRole")


class UserQueryRequest(PageRequest):
    id: int | None = None
    user_account: str | None = Field(default=None, alias="userAccount")
    user_name: str | None = Field(default=None, alias="userName")
    user_profile: str | None = Field(default=None, alias="userProfile")
    user_role: str | None = Field(default=None, alias="userRole")


class LoginUserVO(LongIdModel, TimeModel):
    user_account: str = Field(alias="userAccount")
    user_name: str | None = Field(default=None, alias="userName")
    user_avatar: str | None = Field(default=None, alias="userAvatar")
    user_profile: str | None = Field(default=None, alias="userProfile")
    user_role: str = Field(alias="userRole")


class UserVO(LongIdModel, TimeModel):
    user_account: str = Field(alias="userAccount")
    user_name: str | None = Field(default=None, alias="userName")
    user_avatar: str | None = Field(default=None, alias="userAvatar")
    user_profile: str | None = Field(default=None, alias="userProfile")
    user_role: str = Field(alias="userRole")


class UserRawVO(LongIdModel, TimeModel):
    user_account: str = Field(alias="userAccount")
    user_password: str = Field(alias="userPassword")
    user_name: str | None = Field(default=None, alias="userName")
    user_avatar: str | None = Field(default=None, alias="userAvatar")
    user_profile: str | None = Field(default=None, alias="userProfile")
    user_role: str = Field(alias="userRole")
    is_delete: int | None = Field(default=None, alias="isDelete")
