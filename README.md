# Clarity AI challenge - Álvaro de Prada  

## Description  
This project is a simple Flask application that parses log files to filter connections based on host and time range, using Unix timestamps.

## Installation
To run this project, you will need Python 3.8 or later. You can set up the project environment with the following steps:

1. Clone the repository:
```
   git clone https://github.com/yourusername/your-project-name.git
```
2. Navigate to the project directory:
```
   cd your-project-name
```
3. Install the required dependencies:
```
   pip install -r requirements.txt
```

## Usage
To run the application, execute:
```
python app.py
```
Then, open a browser and go to http://127.0.0.1:5000/ to access the application.

## What it does?
Given a .txt log file like the one provided in the homework description, you need to include as input an init_datetime , an
end_datetime, and a Hostname, and the program will return:
- A list of hostnames connected to the given host during the given period.
