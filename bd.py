from aiogram import types,Bot
from gino import Gino
from sqlalchemy import (Column,Integer,BigInteger,String,Sequence,TIMESTAMP,Boolean,JSON)
from sqlalchemy import sql
from gino.schema import GinoSchemaVisitor
from config import dp_pass,dp_users,host

db = Gino()

class Users(db.Model):
    __tablename__ ="users"
    id = Column(Integer,Sequence("user_id_seq"),primary_key=True)
    user_id=Column(BigInteger)
    query:sql.Select



class DBCommands:
    async def get_user(self,user_id):
        user = await Users.query.where(Users.user_id==user_id).gino.first()
        return user
    async def add_new_user(self)->Users:
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = Users()
        new_user.user_id=user.id


        await new_user.create()
        return new_user

    async def count_users(self):
        total = await db.func.count(Users.id).gino.scalar()
        return total


