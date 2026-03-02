from pyscript import document, display


def signup(event):
    document.getElementById("message").innerHTML = ""

    fullname = document.getElementById("fullname").value
    username = document.getElementById("username").value
    password = document.getElementById("password").value
   
    # Check input
    if fullname == "" or username == "" or password == "":
        display("Input is blank.", target="message")
        return
    
    # Validate name
    if fullname != fullname.title():
        display("Error: Please use Title Case (e.g., 'Ramos, Queeny Haraj').", target="message")
        return

    # Validate username
    if len(username) < 7:
        display(f"Please add {7 - len(username)} more characters to username.", target="message")
        return

    if len(password) < 10:
        display(f"Please add {10 - len(password)} more characters to password.", target="message")
        return
    
    # Check is password has at least one letter
    if not any(char.isalpha() for char in password):
        display("Password must contain at least one letter.", target="message")
        return

    # Check is password has at least one number
    if not any(char.isdigit() for char in password):
        display("Password must contain at least one number.", target="message")
        return
    
    # Display message
    display("You have successfully made an account! ♡", target="message")


    ## display(target="message") else:
    # if fullname.istitle():