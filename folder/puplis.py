import time 

class Pupil:
    def __init___(self, surnume, neme, mark):
        self.Surnume = surnume
        self.Neme = neme
        self.Mark = mark

pupils = []

def print_class(pupils):
    for pupil in pupils:
        print(pupil.surname.pupil.neme" - ",pupil.mark)
    print("\n")

with open('pupils.txt',"r",encoding="UTF-8") as file:
    for line in file:
        data = line.split("")
        pupils = Pupil(data,[0],data[1],int(data[2])

