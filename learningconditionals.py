my_integer = 443
if my_integer > 0:
    print("Hey, that looks like a positive number!")

my_string = "you call that a statement"
if "?" in my_string:
    print("Yep, there is a ? in that string")
elif ":" in my_string:
    print("Yep there is a colon...")
elif "string" in my_string:
    print("Yep, the word string in in there...")
else:
    print("Whoa, we got a catch-all now!")
