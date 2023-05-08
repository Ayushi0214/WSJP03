#country_capitals

db = {}

while True:
    print("""
    press 1 to insert
    press 2 to display countries
    press 3 to display capitals
    press 4 to delete
    press 5 to display db
    press 6 to display capital""")

    choice = int(input('enter your choice between 1-6: '))
    if choice == 1:
        country = input("enter country name: ").upper()
        capital = input('enter capital name: ').upper()
        db[country] = capital

    elif choice == 2:
        if len(db) == 0:
            print("data not available")
        else:
            print("Countries: ")
            for i in db.keys():
                print(i)
            
    elif choice == 3:
        if len(db) == 0:
            print("data not available")
        else:
            print("Capitals: ")
            for i in db.values():
                print(i)
    
    elif choice == 4:
        country = input('enter country name: ').upper()
        del db[country]
    
    elif choice == 5: 
        print("Details are as follows: ")
        for i,j in db.items:
            print(i,j)
            
    elif choice == 6:
        country = input("enter country: ").upper()
        print(db[country])
        
    else:
        print("invalid input")
        
    repeat = input('do you want to repeat again? ').upper()
    if repeat == "NO":
        break
