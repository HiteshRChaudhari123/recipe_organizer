import os

if os.path.exists("/mnt/data/recipes.txt"):
    with open("/mnt/data/recipes.txt", "r") as file:
        content = file.read()
        recipes = eval(content) if content else {}
else:
    recipes = {}

def add_recipe():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    instructions = input("Enter the instructions: ")
    recipes[name] = {'Ingredients': ingredients, 'Instructions': instructions}
    print(f"Recipe for {name} added successfully!")
    with open("/mnt/data/recipes.txt", "w") as file:
        file.write(str(recipes))

def view_recipe():
    print("\nAvailable Recipes:")
    for idx, name in enumerate(recipes.keys(), start=1):
        print(f"{idx}. {name}")
    recipe_num = int(input("\nEnter the number of the recipe you want to view: "))
    name = list(recipes.keys())[recipe_num - 1]
    print(f"\nRecipe: {name}")
    print(f"Ingredients: {', '.join(recipes[name]['Ingredients'])}")
    print(f"Instructions: {recipes[name]['Instructions']}")

def search_recipe():
    keyword = input("Enter a keyword to search for a recipe: ")
    found = False
    for name, recipe in recipes.items():
        if keyword in name or keyword in ' '.join(recipe['Ingredients']) or keyword in recipe['Instructions']:
            print(f"\nRecipe: {name}")
            print(f"Ingredients: {', '.join(recipe['Ingredients'])}")
            print(f"Instructions: {recipe['Instructions']}")
            found = True
    if not found:
        print("No recipes found for the given keyword.")

while True:
    print("\nRecipe Organizer Menu:")
    print("1. Add Recipe")
    print("2. View Recipe")
    print("3. Search for Recipe")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_recipe()
    elif choice == '2':
        view_recipe()
    elif choice == '3':
        search_recipe()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")

print("Thank you for using the Recipe Organizer!")
