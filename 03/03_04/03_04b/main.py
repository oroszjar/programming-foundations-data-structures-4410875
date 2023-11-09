user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    updated_preferences = {}
    for key, value in user_pref.items():
        if value is not None:
            updated_preferences[key] = value
    return updated_preferences

# create new dict removing the elements with empty values

print(update_preferences(user_preferences))
