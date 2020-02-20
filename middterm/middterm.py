db = { "vaso1990": {"email": "vaso@gmail.com", "password": "test123" , "credit": 0  } }

def first_question():
  ques = input("do you want to Register: ")
  ques = ques.lower()
  if ques == "yes":
    return True
  else:
    return False

while True:
    if first_question():
        use = input("username: ")
        email = input("email: ")
        passw = input("password: ")
        db[use] = {"email": email , "password" : passw , "credit": 0 }

        print(db)
    else:
        break


def second_question():
  ques = input("do you want to logIn: ")
  ques = ques.lower()
  if ques == "yes":
    return True
  else:
    return False

while True:
    if second_question():
        user = input("insert current username: ")
        if user in db:
            print("you are logged in")
        else:
            print("try again")
    else:
        break


def third_question():
  ques = input("add to deposit: ")
  ques = ques.lower()
  if ques == "yes":
    return True
  else:
    return False


while True:
    if third_question():
        user = input("insert current username: ")
        if user in db:
            x = int(input("Add amount: "))
            db[user]["credit"]+=x
        else:
            print("try again")
    else:
        print(db)