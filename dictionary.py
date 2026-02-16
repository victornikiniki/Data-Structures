user = { 
    "language" : "English", 
    "fontSize" : "10px", 
    "font" : "Sans-serif", 
    "time" : "AEST", 
    "job" : "Student"
}

# print(user["language"])

user["time"] = "AEDT"

user["relationship status"] = "dating"

remove_item = user.pop("time")

# print(user)
