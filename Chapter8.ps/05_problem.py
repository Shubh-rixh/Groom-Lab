def inch_to_cms(inch):
    return inch*2.54
inch = int(input("Enter value in inch: "))
a = inch_to_cms(inch)
print(f"{a} cms")