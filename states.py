from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
class Mailing(StatesGroup):
    Text = State()


storage = MemoryStorage()