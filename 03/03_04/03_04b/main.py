user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    return{
        key:value for key, value in user_pref.items() if value is not None
    }
    
    #del user_preferences["notifications"]
    #del user_preferences["theme"]
    #return user_preferences


print(update_preferences(user_preferences))
