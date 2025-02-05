import json
import time
from datetime import datetime, timedelta
from termcolor import cprint
import random
import sqlite3
import os

DATABASE_PATH = 'tasks_schedule.db'

def initialize_db():
    conn = sqlite3.connect('C:\Users\productivity app')  # Persistent database file
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS schedule (
                          task TEXT,
                          start_time TEXT,
                          end_time TEXT
                      )''')
    return conn

def clear_schedule_from_db(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM schedule")
    conn.commit()

def save_schedule_to_db(schedule, conn):
    cursor = conn.cursor()
    for task, start_time, end_time in schedule:
        cursor.execute("INSERT INTO schedule (task, start_time, end_time) VALUES (?, ?, ?)",
                       (task, start_time.strftime("%Y-%m-%d %H:%M:%S"), end_time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

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

def main():
    conn = initialize_db()
    clear_schedule_from_db(conn)  # Clear any existing schedule in the database
    tasks = load_tasks()
    schedule = get_tasks_schedule(tasks)
    save_schedule_to_db(schedule, conn)
    current_index = 0
    while True:
        now = datetime.now()
        current_task, start_time, end_time = schedule[current_index]
        remaining_time = end_time - now
        remaining_minutes = int(remaining_time.total_seconds() // 60)
        print('')
        for index, (task, s_time, e_time) in enumerate(schedule):
            if index < current_index:
                # Task is completed
                print(f'{task} done: {e_time.strftime("%H:%M")}')
            elif index == current_index:
                # Current task
                if remaining_minutes < 2:
                    cprint(f'{task} < 2m left!', 'white', 'on_red', attrs=['blink'])
                elif remaining_minutes < 5:
                    cprint(f'{task} < 5m left!', 'white', 'on_red')
                else:
                    cprint(f'{task} - {remaining_minutes}m remaining', 'white', 'on_blue')
            else:
                print(f'{task} @ {s_time.strftime("%H:%M")}')
        list_of_reminders = [
            "I am getting better every day",
            "Jobs not finished",
            "Rest at the end",
            "I am the best algo trader in the world",
        ]
        random_reminder = random.choice(list_of_reminders)
        print(random_reminder)
        if now >= end_time:
            current_index += 1
        if current_index >= len(schedule):
            cprint("All tasks are completed", 'white', 'on_green')
            break
        time.sleep(15)
    conn.close()

if __name__ == "__main__":
    main()
