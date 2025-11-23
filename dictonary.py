country_capitals = {
    "United States": "Washington D.C.",
    "England": "London",
    "Germany": "Berlin",
    "Canada": "Ottawa"
}
print(len(country_capitals))                 # Number of items
print(country_capitals)                      # Display all key-value pairs
country_capitals["Italy"] = "Rome"           # Add new item
print(country_capitals)
del country_capitals["Germany"]              # Delete an item
print(country_capitals)
country_capitals.clear()                     # Clear all entries
print(country_capitals)
