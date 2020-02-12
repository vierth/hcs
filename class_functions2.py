# funcitons are defined with the def keyword

def my_function():
    # all of the code in this block will run as part of the function
    print("hello! Nice function!")

def hello_function(name):
    # say hello!
    print("Hi, " + name + "! Nice function!")

def hello_function_2(person_one, person_two):
    print(f"Hi, {person_two}, my name is {person_one}")

def greeting_or_parting(yourname, myname, interaction="greeting"):
    if interaction == "greeting":
        print(f"Hi, {yourname}, my name is {myname}!")
    elif interaction == 'parting':
        print(f"Goodbye, {yourname}. {myname} out")
    else:
        print(f"{interaction} not understood")

greeting_or_parting("Paul", "Erin", interaction="chumbawumba")