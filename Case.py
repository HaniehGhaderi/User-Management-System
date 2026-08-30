import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "usersCase.json"
print("File path:", FILE_PATH)
print("File exists:", FILE_PATH.exists())
try:
    with open(FILE_PATH, 'r') as file:
        users = json.load(file)
except FileNotFoundError: 
        users = []
                
                
class UserManger: 
        def __init__(self):
            self.users= users        
        def save_changes(self):
            with open('D:/Python/Tamrinha/usersCase.json','w') as file:
                        json.dump(self.users,file,indent=4)    
        def add_user(self,name, age):
                if self.users:
                        for x in self.users:
                                    if x['Name']==name and x['Age']==age :
                                        print("❌ User already exists!")  
                                        return    
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
                            print(f"""User Found:
                                                ID: {x["id"]}
                                                Name: {x["Name"]}
                                                Age: {x["Age"]}""")
                                        
                            return
                    print(f'{name} is NOT found.')    
                        
        def search_userID(self,id):
                    for x in self.users:
                        if x['id']==id :
                            print(f"""User Found:
                            ID: {x["id"]}
                            Name: {x["Name"]}
                            Age: {x["Age"]}""")
                    
                            return
                    print(f'{id} is NOT found.')                 
        def delete_user(self, name, age):

            for x in self.users:
                if x['Name'] == name and x['Age'] == age:
                    print(f'{name} with the age of {age} is found.')
                    self.users.remove(x)
                    self.save_changes()
                    print(f'User {name} deleted successfully.')
                    return

            print(f'{name} with the age of {age} is NOT found.') 
                                    
        def update_user(self,name,age):
                    for x in self.users:
                        if x['Name']==name and x['Age']==age:
                            print(f'{name} with the age of {age} is found.')
                            NewName=input('Enter the new name=')
                            NewAge=int(input('Enter the new age='))
                            x['Name']=NewName
                            x['Age']=NewAge
                            self.save_changes()
                            break

                    else:
                        print(f'{name} with the age of {age} is NOT found.')    

        def show_all_users(self):
            if not self.users:
                print("No users found.")
                return

            print(f"{'ID':<10}{'NAME':<20}{'AGE':<10}")
            print("-" * 40)

            for x in self.users:
                    print(f"{x['id']:<10}{x['Name']:<20}{x['Age']:<10}")     




#________________MAIN PROJECT_____________________                    
manager=UserManger()                
while True:                
    try:
            match_number=int(input("""========== USER MANAGEMENT ==========  

            1. Add User
            2. Search by UserName
            3. Search by ID
            4. Delete User
            5. Update User
            6. Show All Users
            7. Statistics
            8. Exit
            

            Choose:"""))
    except ValueError:
        print("Please enter a number.")  
        continue      

    match match_number:    
            #Add a new
            
            case 1:
                try:
                    name=str(input('Name='))
                except ValueError:
                    print('Invalid input for Name')
                    
                try:
                    age = int(input('Age='))
                except ValueError:
                    print("Age must be a number")
                manager.add_user(name,age)    
                
        #Search a user by username
            case 2:
                try:
                    name=input('Name=')
                except ValueError:
                    print("Invalid Name")
                manager.search_UserName(name)
        #Search a user id
            case 3:
                try:
                    id=int(input('ID=') )
                except ValueError:
                    print("Invalid ID")  
                manager.search_userID(id)                    
        #Delete a new user
            case 4:
                name=input('Name=')
                try:
                    age=int(input('Age='))                    
                except ValueError:
                    print("Invalid Age")
                massage=input(f"""Are you sure you want to delete {name}?Y/N:""")
                if massage.lower() == 'y':
                    manager.delete_user(name,age) 
                elif massage.lower() == 'n':
                    print('Delete cancelled.')
                    continue              
        #update a user
            case 5:
                print('Befor updating the list of user',users)
                name=input('Name=')
                age=int(input('Age='))
                manager.update_user(name,age)
                
        #Show all users
            case 6:
                manager.show_all_users()
            #Statistics    
            case 7: 
                if not users:
                    print("No users found.")
                    continue
                ages = [user["Age"] for user in users]
                print(f"Total Users: {len(users)}")
                print(f"Average Age: {sum(ages)/len(ages):.2f}")
                print(f"Max Age: {max(ages)}")
                print(f"Min Age: {min(ages)}")
                            
        #exite
            case 8:
                massage=input("""Are you sure you want to exit?
        Y/N:""")
                if massage.lower() == 'y':
                    break
                elif massage.lower() == 'n':
                    continue
            
            
            case _:
                print("Invalid option! Please choose 1-8.")    
                
                
