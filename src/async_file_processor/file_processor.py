import aiofiles
import os 
import logging

# Async function to process a file and count the number of words
async def process_file(input_path):
    result={}
    try:
        async with aiofiles.open(input_path,mode='r') as file:
            text=await file.read()
            word_count=len(text.split())
            result['filename'] = os.path.basename(input_path)
            result['word_count'] = word_count
            logging.info(f"{os.path.basename(input_path)} processed successfully ")
            logging.info(f"{os.path.basename(input_path)}: {word_count} words")
    except Exception as e:
        result['filename'] = os.path.basename(input_path)
        result['word_count'] = 0
        logging.error(f"{os.path.basename(input_path)} Error: {e}")
    return result
                   
    