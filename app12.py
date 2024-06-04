
options={
    "1":"Go home",
    "2":"Go To World",
    "3":"Go to School"
}

while True:
    username = input("Enter username:")
    print("Username is: " + username)
    option=input("Enter Options /n 1 to 3 \n")
    print(option)
    print(options[option])
    with open("one.txt","w") as file:
        file.write(f"username: {username} \n")
        file.write(f"option: {option} \n")
        