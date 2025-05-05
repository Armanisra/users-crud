from sqlalchemy import Column, Integer, String 

class Users():
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable = False) 
    last_name = Column(String, nullable = False) 
    age = Column(Integer, nullable = False)
#sqknjbwkjwq