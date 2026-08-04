#File Handling
#txt
with open("journal.txt","w") as file:
    file.write("This is the first file created.\n")
    file.write("We'll be calling this line - Journal.\n")
    file.write("Welcome to Journal.\n")
with open("journal.txt","a") as file:
    file.write("Write Something.\n")
with open("journal.txt", "r") as file:
    for num, line in enumerate(file, start= 1):
        print(f"{num}: {line.strip()}")
#csv
import csv
with open("student.csv", "w", newline= "") as file:
    fieldnames = ["Name", "Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Eric", "Grade": "85"})
    writer.writerow({"Name": "Sally", "Grade": "90"})
    writer.writerow({"Name": "Finn", "Grade": "80"})
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} scored {row['Grade']}")
#json
import json
person = {
    "name": "Hill",
    "age": 30,
    "skills": ["coding", "writing"]
}
with open("person.json", "w") as file:
    json.dump(person, file, indent= 4)
with open("person.json", "r") as file:
    loaded = json.load(file)
    print(loaded["skills"])