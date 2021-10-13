#Create Dictionary
user_pass={"Shaden":"shaden123",
          "Eyad":"123",
          "sara":"12345678",
          "farah":"farah$@1"}

#Print Dictionaries value
print(user_pass["Shaden"])
print(user_pass["sara"])


#Change Dictionaries values
user_pass["Eyad"]="3456"
#Add new Dictionary values 
user_pass["Aleen"]="AleenPassword"
#Delete dictionary element
del(user_pass["Eyad"])
#print all Dictionary values
print(user_pass.values())
#print all Dictionary keys
print(user_pass.keys())
