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


with open('C:\\Users\\vetle\\OneDrive\\Dokumenter\\Skole\\BigData\\noder\\psam_ca2_converted.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    batch = []
    batch_size = 10000 

    for row in csv_reader:
        
        person_data = {
            "person_id": row["ID"],
            "sex": row["sex_id"],
            "age": row["age"],
            "when_last_worked": row["when_last_worked_id"],
            "education": {
                "education_level": row["education_level_id"],
                "field_of_degree1": row["field_of_degree1_id"],
                "field_of_degree2": row["field_of_degree2_id"],
                "current_education": row["current_education_id"]
            },
            "economy": {
                "poverty_income_ratio": row["poverty_income_ratio"],
                "salary_past_12_months": row["sallary_past_12_months"],
                "total_persons_earnings": row["total_persons_earnings"]
            }
        }

       
        batch.append(person_data)

        
        if len(batch) >= batch_size:
            insert_batch(batch)
            batch = []  

    
    if batch:
        insert_batch(batch)

print("All data inserted successfully!")
