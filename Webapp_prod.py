from flask import Flask, render_template, jsonify
import json
import time
from datetime import datetime, timedelta
import random

app = Flask(__name__)

def load_tasks():
    with open(r'C:\Users\bbrowne\Desktop\DEV\productivity app\tasks.json', 'r') as f:
        tasks = json.load(f)
    return tasks

def get_tasks_schedule(tasks):
    task_start_time = datetime.now()
    schedule = []
    for task, minutes in tasks.items():
        end_time = task_start_time + timedelta(minutes=minutes)
        schedule.append((task, task_start_time, end_time))
        task_start_time = end_time
    return schedule

@app.route('/')
def index():
    tasks = load_tasks()
    schedule = get_tasks_schedule(tasks)
    current_index = 0
    now = datetime.now()

    # Find the current task
    for i, (task, start_time, end_time) in enumerate(schedule):
        if now < end_time:
            current_index = i
            break

    current_task, start_time, end_time = schedule[current_index]
    remaining_time = end_time - now
    remaining_minutes = int(remaining_time.total_seconds() // 60)

    # Prepare data for the template
    task_data = []
    for index, (task, s_time, e_time) in enumerate(schedule):
        if index < current_index:
            status = 'done'
            time_str = e_time.strftime("%H:%M")
        elif index == current_index:
            status = 'current'
            time_str = f'{remaining_minutes}m remaining'
        else:
            status = 'upcoming'
            time_str = s_time.strftime("%H:%M")
        
        task_data.append({
            'task': task,
            'status': status,
            'time': time_str
        })

    # Random reminder
    list_of_reminders = [
        "I am getting better every day",
        "Jobs not finished",
        "Rest at the end",
        "I am the best algo trader in the world",
    ]
    random_reminder = random.choice(list_of_reminders)

    return render_template('index.html', tasks=task_data, reminder=random_reminder)

@app.route('/update')
def update():
    tasks = load_tasks()
    schedule = get_tasks_schedule(tasks)
    current_index = 0
    now = datetime.now()

    # Find the current task
    for i, (task, start_time, end_time) in enumerate(schedule):
        if now < end_time:
            current_index = i
            break

    current_task, start_time, end_time = schedule[current_index]
    remaining_time = end_time - now
    remaining_minutes = int(remaining_time.total_seconds() // 60)

    # Prepare data for the JSON response
    task_data = []
    for index, (task, s_time, e_time) in enumerate(schedule):
        if index < current_index:
            status = 'done'
            time_str = e_time.strftime("%H:%M")
        elif index == current_index:
            status = 'current'
            time_str = f'{remaining_minutes}m remaining'
        else:
            status = 'upcoming'
            time_str = s_time.strftime("%H:%M")
        
        task_data.append({
            'task': task,
            'status': status,
            'time': time_str
        })

    # Random reminder
    list_of_reminders = [
        "I am getting better every day",
        "Jobs not finished",
        "Rest at the end",
        "I am the best algo trader in the world",
    ]
    random_reminder = random.choice(list_of_reminders)

    return jsonify(tasks=task_data, reminder=random_reminder)

if __name__ == "__main__":
    app.run(debug=True)