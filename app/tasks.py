import subprocess
import os
from app.utils import read_file

def install_uv():
    """Install uv package if not already installed"""
    try:
        subprocess.run(["uv", "--version"], check=True)
    except FileNotFoundError:
        subprocess.run(["pip", "install", "uv"], check=True)

def run_datagen(email):
    """Run datagen.py script with the user's email"""
    install_uv()  # Ensure uv is installed
    subprocess.run(["python", "-m", "pip", "install", "requests"])  # Install requests
    subprocess.run(["python", "-c", f"import requests; exec(requests.get('https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py').text)", email])

def format_markdown():
    """Format markdown file using Prettier"""
    subprocess.run(["npx", "prettier@3.4.2", "--write", "/data/format.md"], check=True)

import datetime

def count_wednesdays():
    """Count the number of Wednesdays in /data/dates.txt"""
    with open("/data/dates.txt", "r") as f:
        dates = f.readlines()

    wednesday_count = sum(1 for date in dates if datetime.datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == 2)

    with open("/data/dates-wednesdays.txt", "w") as f:
        f.write(str(wednesday_count))

import json

def sort_contacts():
    """Sort contacts by last_name and first_name"""
    with open("/data/contacts.json", "r") as f:
        contacts = json.load(f)

    contacts.sort(key=lambda x: (x["last_name"], x["first_name"]))

    with open("/data/contacts-sorted.json", "w") as f:
        json.dump(contacts, f, indent=2)

import glob

def recent_logs():
    """Extract the first line of the 10 most recent log files"""
    log_files = sorted(glob.glob("/data/logs/*.log"), key=os.path.getmtime, reverse=True)[:10]

    with open("/data/logs-recent.txt", "w") as f:
        for log in log_files:
            with open(log, "r") as lf:
                first_line = lf.readline().strip()
                f.write(first_line + "\n")

def execute_task(task):
    """Identify the task and execute the corresponding function"""
    if "install uv" in task and "run datagen.py" in task:
        return run_datagen(task.split()[-1])  # Extract email from task
    elif "format markdown" in task or "format /data/format.md" in task:
        return format_markdown()
    elif "count Wednesdays" in task:
        return count_wednesdays()
    elif "sort contacts" in task:
        return sort_contacts()
    elif "recent log files" in task:
        return recent_logs()
    else:
        raise ValueError("Unknown task")
