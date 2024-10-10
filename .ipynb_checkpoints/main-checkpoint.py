name = input("Please give me your name.")

movie = input("What is your favorite movie?")

    while True:
        rating = input(f"How would you rate '{movie}' on a scale of 1-10? ")
        try:
            rating = int(rating)
            if 1 <= rating <= 10:
                break
            else:
                print("Please enter a rating between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

print(f"{name} rated {movie} a {rating}/10")