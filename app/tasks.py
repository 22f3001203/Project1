import subprocess
import os
import datetime
import json
import glob
import requests
from app.utils import read_file



DATA_DIR = "/data/"

def install_uv():
    
    try:
        subprocess.run(["uv", "--version"], check=True)
    except FileNotFoundError:
        subprocess.run(["pip", "install", "uv"], check=True)

def run_datagen(email):
    install_uv()
    subprocess.run(["python", "-m", "pip", "install", "requests"], check=True)

    datagen_path = os.path.join(DATA_DIR, "datagen.py")
    
    try:
        response = requests.get("https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py")
        response.raise_for_status()
        with open(datagen_path, "w") as f:
            f.write(response.text)
        
        subprocess.run(["python", datagen_path, email], check=True)
        return "Datagen script executed successfully."
    except requests.RequestException as e:
        return f"Error fetching datagen.py: {str(e)}"

def ensure_prettier():
    try:
        subprocess.run(["npx", "prettier", "--version"], check=True)
    except FileNotFoundError:
        subprocess.run(["npm", "install", "-g", "prettier"], check=True)

def format_markdown():
    ensure_prettier()
    md_file = os.path.join(DATA_DIR, "format.md")
    
    if not os.path.exists(md_file):
        return "Markdown file not found."
    
    subprocess.run(["npx", "prettier", "--write", md_file], check=True)
    return "Markdown file formatted."

def count_wednesdays():
    file_path = os.path.join(DATA_DIR, "dates.txt")
    output_path = os.path.join(DATA_DIR, "dates-wednesdays.txt")

    if not os.path.exists(file_path):
        return "Dates file not found."

    with open(file_path, "r") as f:
        dates = f.readlines()

    try:
        wednesday_count = sum(1 for date in dates if datetime.datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == 2)
        
        with open(output_path, "w") as f:
            f.write(str(wednesday_count))
        
        return f"Wednesdays counted: {wednesday_count}"
    except ValueError:
        return "Invalid date format in file."

def sort_contacts():
    file_path = os.path.join(DATA_DIR, "contacts.json")
    output_path = os.path.join(DATA_DIR, "contacts-sorted.json")

    if not os.path.exists(file_path):
        return "Contacts file not found."

    try:
        with open(file_path, "r") as f:
            contacts = json.load(f)

        contacts.sort(key=lambda x: (x.get("last_name", ""), x.get("first_name", "")))

        with open(output_path, "w") as f:
            json.dump(contacts, f, indent=2)

        return "Contacts sorted successfully."
    except (json.JSONDecodeError, KeyError):
        return "Invalid contacts file format."

def recent_logs():
    log_files = sorted(glob.glob(os.path.join(DATA_DIR, "logs", "*.log")), key=os.path.getmtime, reverse=True)[:10]
    output_path = os.path.join(DATA_DIR, "logs-recent.txt")

    if not log_files:
        return "No log files found."

    with open(output_path, "w") as f:
        for log in log_files:
            try:
                with open(log, "r") as lf:
                    first_line = lf.readline().strip()
                    f.write(first_line + "\n")
            except Exception:
                continue

    return "Recent logs extracted successfully."

def execute_task(task):
    task_map = {
        "run datagen.py": lambda arg: run_datagen(arg),
        "format markdown": format_markdown,
        "count wednesdays": count_wednesdays,
        "sort contacts": sort_contacts,
        "recent logs": recent_logs
    }

    for key, func in task_map.items():
        if key in task.lower():
            if "run datagen.py" in key:
                email = task.split()[-1]  # Extract email
                return func(email)
            return func()

    raise ValueError("Unknown task")
