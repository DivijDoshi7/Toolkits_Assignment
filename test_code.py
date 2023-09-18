import csv
import pandas as pd

job_titles = ["Data Architect", "Senior Business Analyst", "Data Scientist", "Machine Learning Engineer"]
csv_file_path = "/Users/divijdoshi/Desktop/COMP219_Git_sample/job_data.csv"

try:
    job_data = pd.read_csv(csv_file_path)
    filtered_data = job_data[job_data['job_title'].isin(job_titles)]
    grouped_data = filtered_data.groupby('job_title')['num_of_salaries']

    for title in job_titles:
        if title in grouped_data.groups:
            average_salary = grouped_data.get_group(title).mean()
            print(f"Average num_of_salaries for {title}: {average_salary:.2f}")
        else:
            print(f"No data found for {title}")

except FileNotFoundError:
    print(f"File '{csv_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

