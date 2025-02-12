# Given data
apple_varieties = {
    "Golden Delicious": {"color": "yellow", "taste": "sweet"},
    "Granny Smith": {"color": "green", "taste": "sour"},
    "Fuji": {"color": "red", "taste": "sweet"}
}

# Get user preferences
print("What apple characteristics do you prefer?")
color_preference = input("What color do you prefer? yellow / green / red / leave empty for any: ").lower()
taste_preference = input("What taste do you prefer? sweet / sour / leave empty for any: ").lower()

print(f"Your preferences are: color {color_preference}, taste {taste_preference}.")

matching_apples = [apple for apple, properties in apple_varieties.items() \
                   if (color_preference == properties["color"] or color_preference == "")and \
                    (taste_preference == properties["taste"] or taste_preference == "")]

# for apple, properties in apple_varieties.items():
#     if (color_preference == properties["color"] or color_preference == "") and \
#         (taste_preference == properties["taste"] or taste_preference == ""):
#         matching_apples.append(apple)

print("You should buy these apples: ")
print(matching_apples)
