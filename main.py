
if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    # TODO: Print the Animal instance
    # TODO: Call the method to make a generic animal sound

    # TODO: Create an instance of the Dog class
    # TODO: Print the Dog instance
    # TODO: Call the method to make the dog-specific sound

    # TODO print out all the animals

    from animal import Animal
    from dog import Dog

    black_animal = Animal("Brian", "Bear")
    white_dog = Dog("Jimmy", "Canine", "Husky")

    print(black_animal)
    black_animal.speak()
    print(white_dog)
    white_dog.speak()

    all_animals = Animal.get_all_animals()
    print("All Animals:")
    for animal in all_animals:
        print(animal)

