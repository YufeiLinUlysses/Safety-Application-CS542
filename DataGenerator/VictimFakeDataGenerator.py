
import csv
from faker import Faker
import datetime

def datagenerate(records, headers):
    fake = Faker('en_US')
    with open("VICTIM_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        tools = ['knife', 'gun', 'poison', 'rope', 'wood', 'falcon']
        relation = ['foreign', 'friend', 'family']
        for i in range(records):

            writer.writerow({
                    "Name": fake.name(),
                    "Birth Date" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
                    "Address" : fake.address(),
                    "Tool" : fake.words(1, tools, True),
                    "Relation" : fake.words(1, relation, True),
                    "Job" : fake.job(),
                    "SSN" : fake.ssn(),
                    "Date_between" : fake.date_between(start_date='-4y', end_date='-2y')
                    })
    
if __name__ == '__main__':
    records = 250000
    headers = ["Name", "Birth Date", "Address", "Tool", "Relation", "Job", "SSN", "Date_between"]
    datagenerate(records, headers)
    print("CSV generation complete!")