from pymongo import MongoClient
from config import MoNGO_DB,MONGO_LINK
mdb = MongoClient(MONGO_LINK)[MoNGO_DB]

def search_or_save(mdb,effective_user,nessage):
    user = mdb.users.find_one({'user_id':effective_user.id})
    if not user:
        user={
            "user_id":effective_user.id
    }
        mdb.users.insert_one(user)
    return user