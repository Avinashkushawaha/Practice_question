#wap to check given collection homogenious or not
collection = eval(input("Enter collection here :"))
homogeneous = True

if len(collection) > 0:
    ref_type = type(collection[0])
    for item in collection:
        if type (item) != ref_type:
           homogeneous = False
           break

print("Collection is homogeneous" if homogeneous else "Collection is not homogeneous")


