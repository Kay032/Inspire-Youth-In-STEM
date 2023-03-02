f = open("C:\Users\USER\OneDrive\Documents\Inspire-Youth-In-STEM\Week-4\text.txt","r+w")

print(f,readline())
file_name = open()'C:\Users\USER\OneDrive\Documents\Inspire-Youth-In-STEM\Week-4\text.txt'
try:
    with open(filename) as f_obj:
        contents= f_obj.read()
        print(contents)
except FileNotFoundError:
