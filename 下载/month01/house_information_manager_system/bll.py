"""
    业务逻辑层
""" 
from dal import HouseDao

class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

