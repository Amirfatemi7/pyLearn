


mm = 




def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Download")
    print("7- Exit")




print(MEDIAS)

while True:
    show_menu()
    choice = int(input("Enter your choice "))

    match choice:
        case 1:
            Product.add()
        case 2:
            id = int(input("enter product id: "))
            for product in PRODUCT:
                if product.id == id:
                    product.edit()

        case 3:
            id = int(input("enter product id: "))
            for product in PRODUCT:
                if product.id == id:
                    product.remove()
        case 4:
            Product.search()
        case 5:
            Product.show_list()
        case 6:
            buy()
        case 7:
            db.write()
        case _:
            print("mese adam vared kon :) ")
        