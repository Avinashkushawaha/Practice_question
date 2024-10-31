def info_person(*args, **kwargs):
    for key, value in kwargs.items():
        print(key, value)
    

info_person(name ="Ram", age="30",dept="CSE") 
info_person(name="Shyam", dept="CSE")

