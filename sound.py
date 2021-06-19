from datetime import datetime, timedelta


entry = input("Please enter ID: ")
age = datetime.today()
year = int(age.strftime("%y"))
for entry in range(int(id_input.get())):
    age = id_input.get()[2] - year
        if age >= 18:
            print("You may try your luck.")
        elif age != 18:
            print("Sorry, you are not there yet.")
        elif id_input != 13:
            print("ID number invalid, please try again.")
    except ValueError:
        if id_input != int
            print("Please only use numbers")
