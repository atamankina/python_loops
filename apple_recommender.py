# Given data
apple_varieties = {
    "Golden Delicious": {"color": "yellow", "taste": "sweet"},
    "Granny Smith": {"color": "green", "taste": "sour"},
    "Fuji": {"color": "red", "taste": "sweet"}
}

# Get user preferences
print("What apple characteristics do you prefer?")
color_preference = input("What color do you prefer? yellow / green / red : ")
taste_preference = input("What taste do you prefer? sweet / sour : ")

print(f"Your preferences are: color {color_preference}, taste {taste_preference}.")

matching_apples = []

for apple, properties in apple_varieties.items():
    print(apple)
    print(properties)

