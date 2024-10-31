def predict_grade(score):
    if score > 90:
        print("grade A")
    elif score > 80:
        print("grade B")
    elif score >= 60:
        print("grade C")
    else:
        print("grade D")


predict_grade(99)
