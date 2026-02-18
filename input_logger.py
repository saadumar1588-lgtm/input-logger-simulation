import datetime

print("This is a simple key logging simulation.")
print("Type 'exit' to stop the program.\n")

while True:
    user_input = input("Type something: ")

    if user_input.lower() == "exit":
        print("Program stopped.")
        break

    time_now = datetime.datetime.now()

    with open("keylog.txt", "a") as file:
        file.write(str(time_now) + " - " + user_input + "\n")

print("Your data is saved in keylog.txt")
