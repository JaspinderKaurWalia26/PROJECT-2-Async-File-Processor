# Async File Processor

## Project Overview
Async File Processor is a Python-based system that reads and processes multiple **text files** concurrently using asynchronous programming.  
The project demonstrates how real-world applications handle multiple file operations efficiently without blocking execution.

---

## What does this project do?
- Reads **multiple `.txt` files at the same time**  
- Counts the **number of words** in each file  
- Stores all results in a **single CSV file** (`results.csv`)  
- Logs:
  - Timestamped messages for each file processed
  - File-level success (e.g., "file1.txt processed successfully")
  - Word count for each file (e.g., "file1.txt: 72 words")
  - Errors if any file fails to process
  - Summary message when all files are processed (e.g., "All results saved to results.csv")  

---

## Why Async Programming is Used
Async programming allows the program to start reading one file and move on to other files while waiting for I/O.  
Reading files sequentially can be slow, but asynchronous programming improves efficiency and reduces waiting time.

### Benefits of Async
- Faster execution  
- Better performance for I/O-bound tasks  
- Efficient use of system resources  
- Scalable file processing  

---

## Technologies Used
- Python 3  
- asyncio  
- aiofiles  
- logging module  
- csv module  

---

## 📁 Project Structure
```
ASYNC_FILE_PROCESSOR/
│
├── data/
│   ├── input_files/      #input .txt files here
│   │   ├── file1.txt
│   │   ├── file2.txt
│   │   └── file3.txt
│   └── output_files/
│       └── results.csv   # All processed results saved here
│
├── logs/
│   └── app.log           # Logs for program execution
│
├── src/
│   └── async_file_processor/
│       ├── __init__.py      # Allows importing files from this folder as a package
│       ├── main.py          # Program entry point
│       ├── file_processor.py # Async function to process each file
│       └── logger.py        # Logging setup
│
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies
```
---
## How to Run
Follow these steps to run the Async File Processor:
### 1. Clone the repository
```
git clone https://github.com/JaspinderKaurWalia26/PROJECT-2-Async-File-Processor.git
cd PROJECT-2-Async-File-Processor
```
### 2. Create a virtual environment (optional)
```
python -m venv venv
```
### 3. Activate the virtual environment
- Windows:
```
venv\Scripts\activate
```
- Linux/Mac:
```
source venv/bin/activate
```
### 4. Install dependencies
```
pip install -r requirements.txt
```
### 5. Run the program
```
python -m src.async_file_processor.main
```
### 6. Check outputs

- Processed results:data/output_files/results.csv
- Logs: logs/app.log




