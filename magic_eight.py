
def my_function():
    question = input("What is your question?")
    return question
    
while True:
    quest = my_function()
    if quest[-1] == "?":
        print("I’msorry, I can only answer questions.")
        break
    elif quest == "quit":
        break
    else:
        print("I'm sorry, I can only answer questions.")
