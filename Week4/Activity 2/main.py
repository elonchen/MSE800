from rectangle import RectangleLand

if __name__ == "__main__":
    # User input
    length = float(input("Enter the length of the land: "))
    width = float(input("Enter the width of the land: "))

    # Create object
    land = RectangleLand(length, width)

    # Display results
    print("\nLand Information")
    land.display_info()