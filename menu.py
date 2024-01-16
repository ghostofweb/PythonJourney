import pickle

directory = {}
a = open("marks.dat", "wb")
for i in range(5):
    name = input(f"enter the name of the student {i}")
    marks = int(input(f"enter marks of that student {i}"))
    directory[name] = marks

pickle.dump(directory, a)
a.close()
a = open("marks.dat", "rb")
data = pickle.load(a)
a.close()

e = (dict(sorted(data.items())))
for name , marks in e.items():
    print(f"{name} : {marks}")