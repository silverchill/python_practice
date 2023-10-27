name = input("What's your name? ")

match name:
    case "Stephen" | "Solo" | "Clara":
        print("Odiase")
    case "Oby" | "Ugo" | "Dara":
        print("Egede")
    case _:
        print("which family")