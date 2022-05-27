class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name:str = name
        self.age:int = age
        self.tracks:list = tracks
        self.score:float = score
    #methods
    def change_name(self, change_name):
        self.change_name = change_name
        print("The student's name is: ", self.change_name)
    def change_age(self, change_age):
        self.change_age = change_age
        print("The student's age is: ", self.change_age)
    def add_track(self, add_track):
        self.add_track = add_track
        print("The student's track is: ", self.add_track)
    def get_score(self):
        return self.score
#object
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(f"Bob scored {Bob.get_score()} marks")