import asyncio
import os
import csv
import logging
from .logger import setup_logger
from .file_processor import process_file

setup_logger()

# path to input files
input_folder = "data/input_files"
output_file = "data/output_files/results.csv"

# main asynchronous function to process all files
async def main():
    # creating an empty list to store async tasks
    tasks=[]
    # looping through each file in input folder
    for filename in os.listdir(input_folder):
        # processing files that ends with .txt
        if filename.endswith(".txt"):
            # generating full path of the file
            input_files=os.path.join(input_folder,filename)
            # adding to tasks list 
            tasks.append(process_file(input_files))
    # running all async tasks concurrently
    results=await asyncio.gather(*tasks)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['filename', 'word_count'])
        writer.writeheader()
        writer.writerows(results)
    
    logging.info(f"All results saved to {output_file}")
    
if __name__=="__main__":
    asyncio.run(main())
