#Program for Reading the data from CSV file by using File Pointer (Normal Files)
#Non-CsvEx1.py
try:
    with open("student.csv","r") as fp:
        print("-"*50)
        filedata=fp.read()
        print(filedata)
        print("-" * 50)
except FileNotFoundError:
    print("File Does not exist")