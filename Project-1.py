@@ -0,0 +1,51 @@
# User Configuration Manager
# Test dictionary
test_settings = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled"
}
# Function to add a setting
def add_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
# Function to update a setting
def update_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
# Function to delete a setting
def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"
# Function to view settings
def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"

    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result
# Testing
print(add_setting(test_settings, ("Volume", "High")))
print(update_setting(test_settings, ("Theme", "Light")))
print(delete_setting(test_settings, "Language"))
print(view_settings(test_settings))
