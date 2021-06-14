from classes import A, B, C

classes_list = []
while True:
    data = {}
    print("Options:")
    print("1. Create an object of a class")
    print("2. Delete an object with a given name")
    print("3. Run execute method")
    print("4. Quit")
    choice = int(input('Your choice: '))

    if choice==1:
        name = input("Enter name of object: ")
        class_type = input("Enter type of class: ")
        if class_type=='A':
            new_class = A(name)
        elif class_type=='B':
            new_class = B(name)
        elif class_type=='C':
            new_class = C(name)
        classes_list.append(new_class)
    elif choice==2:
        name = input("Enter name of object: ")
        for i in range(len(classes_list)):
            if classes_list[i].name==name:
                del classes_list[i]
                break
    elif choice==3:
        name = input("Enter name of object: ")
        args = input("Enter space separated arguments: ")
        args = args.split()
        for i in range(len(args)):
            data[i+1] = args[i]
        for i in range(len(classes_list)):
            if classes_list[i].name==name:
                classes_list[i].execute(data)
                break
    else:
        exit()
    print()
