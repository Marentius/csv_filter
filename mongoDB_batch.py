import csv
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client.readDB
collection = db.person


def insert_batch(data_batch):
    try:
        collection.insert_many(data_batch)
        print(f"Inserted {len(data_batch)} rows")
    except Exception as e:
        print(f"Error inserting batch: {e}")


with open('C:\\Users\\vetle\\OneDrive\\Dokumenter\\Skole\\BigData\\konverterDatasett\\psam_ca2.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    batch = []
    batch_size = 10000 

    for row in csv_reader:
        
        person_data = {
            "ID": int(row["ID"]),
            "sex": row["sex"],
            "age": int(row["age"]),
            "when_last_worked": row["when_last_worked"],
            "education": {
                "education_level": row["education_level"],
                "field_of_degree1": row["field_of_degree1"],
                "field_of_degree2": row["field_of_degree2"],
                "current_education": row["current_education"]
            },
            "economy": {
                "poverty_income_ratio": int(row["poverty_income_ratio"]),
                "salary_past_12_months": int(row["sallary_past_12_months"]),
                "total_persons_earnings": int(row["total_persons_earnings"])
            }
        }

       
        batch.append(person_data)

        
        if len(batch) >= batch_size:
            insert_batch(batch)
            batch = []  

    
    if batch:
        insert_batch(batch)

print("All data inserted successfully!")
