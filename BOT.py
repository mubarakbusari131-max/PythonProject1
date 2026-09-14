while True:
    user_input = input("you:")
    if user_input == "hello":
        print("bot: Hello!, welcome to bot")

    elif user_input == "name":
        print("bot: my name is python bot")

    elif user_input == "help":
        print("bot: you can say hello, name, or bye")

    elif user_input == "bye":
        print("bot: Goodbye!")
        break

    else:
        print("bot: i dont know your message")
