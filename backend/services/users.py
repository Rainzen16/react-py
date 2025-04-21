import json

class UserService:
    async def get_all_users(self):
        f = open("data/dummy1.json")
        
        users = json.load(f)
        
        return users