from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    print("Starting ETL Pipeline...")

    data = extract_data()
    print("Extracted:", len(data))

    cleaned_data = transform_data(data)
    print("Transformed:", len(cleaned_data))

    load_data(cleaned_data)
    print("ETL Pipeline Completed")

if __name__ == "__main__":
    run_pipeline()
