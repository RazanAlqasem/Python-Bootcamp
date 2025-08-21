fruits = [ "Orange","Apple", "Banana", "Kiwi", "Blueberry"]
print("Fruits List:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits[1] = "Mango"
fruits.insert(2, "Watermelon")

user = input("\insert a fruit name to check: ")
print(user, "exists in the list?", user in fruits)

fruits.sort()
print("\nSorted Fruits List:", fruits)



