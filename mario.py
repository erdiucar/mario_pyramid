from sys import argv

# You must add a number as an input when you try to run the program
if len(argv) == 2:
    try:
        # Try to convert second argv to integer
        height = int(argv[1])

        # Minimum height is 1, maximum height is 20
        if height > 0 and height <= 20:
            space = height - 1

            for i in range(height):
                for j in range(space):
                    print(" ", end="")

                for j in range(i + 1):
                    print("#", end="")

                print("  ", end="")

                for j in range(i + 1):
                    print("#", end="")

                print()

                space -= 1
        else:
            print("Write a number between 1-20")
    except:
        print("Second argv must be an integer")
else:
    print("Argv must have two inputs")
