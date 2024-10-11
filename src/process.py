import os
import re

def clean_report(input_folder, output_folder):
    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        
        # Check if it's a file (ignore subdirectories)
        if os.path.isfile(input_file):
            with open(input_file, 'r') as file:
                data = file.read()

            # Regular expression to match comma-separated table data
            table_data = re.findall(r'[\w\s]+,\s?[\d\w\s\.\%\(\)]+', data)

            # Define the output file path in the clean_report_data folder
            output_file = os.path.join(output_folder, filename)

            # Write the cleaned data to the output file
            with open(output_file, 'w') as cleaned_file:
                for line in table_data:
                    cleaned_file.write(line + '\n')

# Folder paths
input_folder = r'C:\Users\Close\libMutual\report_data_raw'
output_folder = r'C:\Users\Close\libMutual\clean_report_data'

# Clean all files in the input folder and save to the output folder
clean_report(input_folder, output_folder)

print(f'Cleaned data has been written to {output_folder}')
