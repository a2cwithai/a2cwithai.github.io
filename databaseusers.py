dataBase = {
    
}

def check_user(username , password):
    if(username not in dataBase):
        return False
    elif(dataBase[username] != password):
        return False
    else:
        return True    
    
def create_user(username , password):
    if(dataBase[username] == password):
        return False
    else:
        dataBase[username] = password
        return True

