import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "usersCase.json"

try:
    with open(FILE_PATH, 'r') as file:
        users = json.load(file)
except FileNotFoundError: 
        users = []
                
                
class UserManger: 
        def __init__(self):
            self.users= users        
        def save_changes(self):
            with open(FILE_PATH,'w') as file:
                        json.dump(self.users,file,indent=4)    
        def add_user(self,name, age):
                if self.users:
                        for x in self.users:
                                    if x['Name']==name and x['Age']==age :
                                        return {"❌ User already exists!"}   
                #ID for first time                
                if not self.users:
                    new_id = 1
                else:
                    new_id = max(user['id'] for user in self.users) + 1
                    
                self.users.append({'Name': name,'Age': age,'id': new_id})
                self.save_changes()
                print("-===================After adding a new user===================")  
                self.show_all_users()                
        def search_UserName(self,name):

                    for x in self.users:
                        if x['Name']==name :
                            return{(f"""User Found:
                                    ID: {x["id"]}
                                    Name: {x["Name"]} 
                                    Age: {x["Age"]}""")}
                                        
                    return { "NOT found."}                   
        def search_userID(self,id):
                    for x in self.users:
                        if x['id']==id :
                            return(f"""User Found:
                            ID: {x["id"]}
                            Name: {x["Name"]}
                            Age: {x["Age"]}""")
                    
                            
                    return(f'{id} is NOT found.')                 
        def delete_user(self, name, age):

            for x in self.users:
                if x['Name'] == name and x['Age'] == age:
                    self.users.remove(x)
                    self.save_changes()
                    return(f'User {name} deleted successfully.')
                    

            return(f'{name} with the age of {age} is NOT found.')                                    
        def update_user(self, name, age, new_name, new_age):
            for x in self.users:
                if x['Name'] == name and x['Age'] == age:
                    x['Name'] = new_name
                    x['Age'] = new_age

                    self.save_changes()

                    return {
                        "message": "User updated successfully",
                        "user": x
                    }

            return f'{name} with the age of {age} is NOT found.'
        def show_all_users(self):
            return self.users
