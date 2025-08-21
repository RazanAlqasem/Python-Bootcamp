fruits = [ "Orange","Apple", "Banana", "Kiwi", "Blueberry"]
print("Fruits List:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits[1] = "Mango"
fruits.insert(2, "Watermelon")

user_fruit = input("\insert a fruit name to check: ")
print(user_fruit, "exists in the list?", user_fruit in fruits)

fruits.sort()
print("\nSorted Fruits List:", fruits)


