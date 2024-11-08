

def save_names(names):
    with open("usernames.txt", "w") as file:
        for name in names:
            file.write(name + "\n")

def load_names():
    try:
        with open("usernames.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def main(name):
    saved_names = load_names()
    entered_name = name

    if entered_name in saved_names:
        print("Welcome back!")
    else:
        print("Welcome, newbie!")
        saved_names.append(entered_name)
        save_names(saved_names)

