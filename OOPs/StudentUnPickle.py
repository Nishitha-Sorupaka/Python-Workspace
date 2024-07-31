#Program for reading the student records from file(studpick.data)
#StudentUnPickle.py-----File Name and Module Name
import pickle
class StudentUnPickle:
    def readStudRecords(self):
        try:
            with open("studpick.data","rb") as fp:
                print("-"*50)
                while(True):
                    try:
                        obj=pickle.load(fp)
                        obj.disStudData()
                    except EOFError:
                        print("-"*50)
                        break
        except FileNotFoundError:
            print("File Does Not Exist")