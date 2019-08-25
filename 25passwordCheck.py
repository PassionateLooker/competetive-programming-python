def password(passwd):
    special=["%","!","@","*"]
    val=True
    if len(passwd)<6:
        print("Password must be atleast 6 characters")
        val=False
    if len(passwd)>20:
        print("Password shouldn't be more than 20 characters")
        val = False
    if not any(char.isupper() for char in passwd):
        print("Password should have a uppercase")
        val = False
    if not any(char.islower() for char in passwd):
        print("Password should have a lowercase")
        val = False
    if not any(char in special for char in passwd):
        print("Password should have a specialcase")
        val = False
    if val:
        return val
password1=input("Enter password")

if (password(password1)):
    print("Valid password")
else:
    print("Invalid password")

