import pet

def main():
    name = input("Name your pet: ")
    pet = Pet(name)

    print(f"Welcome, {name} has been born!")

    while pet.is_alive():
        pet.status()
        print("Available actions: feed / play / sleep / exit")
        action = input("What would you like to do? ").strip().lower()

        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "sleep":
            pet.sleep()
        elif action == "exit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command. Please try again.")

        pet.update()

    if not pet.is_alive():
        print(f"\nSadly, {pet.name} has passed away. Take better care next time.")

if __name__ == "__main__":
    main()
