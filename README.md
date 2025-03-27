# Productivity App

This is a simple Flask web application designed to display a daily task schedule and provide random motivational reminders. The app helps you stay organized by tracking your tasks and their progress throughout the day.

---

## Features

- **Task Scheduling**: Loads tasks from a JSON file and calculates start and end times for each task.
- **Task Status**: Displays the list of tasks with their status: `done`, `current`, or `upcoming`.
- **Countdown Timer**: Provides a countdown for the current task's remaining time.
- **Motivational Reminders**: Displays random motivational reminders to keep you inspired.

---

## Requirements

- Python 3.x
- Flask
- JSON file (`tasks.json`) containing task names and their durations in minutes.

---

## Installation

1. **Clone or download the repository** to your local machine.
2. **Install Flask** using pip:
   ```bash
   pip install flask
   ```
3. **Prepare the JSON file**:
   - Ensure the `tasks.json` file is placed at the specified location:  
     `C:\Users\bbrowne\Desktop\DEV\productivity app\tasks.json`.
   - The `tasks.json` file should have the following structure:
     ```json
     {
         "Task 1": 30,
         "Task 2": 45,
         "Task 3": 60
     }
     ```
     - Each key represents a task name.
     - Each value represents the task duration in minutes.

---

## Running the Application

1. Navigate to the project directory.
2. Run the application using the command:
   ```bash
   python app.py
   ```
3. Open a web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see your task schedule.

---

## Endpoints

- **`/`**: Displays the task schedule with the status of each task.
- **`/update`**: Returns a JSON response with the updated task schedule and a random reminder.

---

## Code Explanation

### Functions

- **`load_tasks()`**: Loads tasks from the `tasks.json` file.
- **`get_tasks_schedule()`**: Generates a schedule by calculating the start and end time for each task.

### Flask Routes

- **Root Route (`/`)**:
  - Renders the schedule in an HTML template (`index.html`).
  - Displays the task list with their status (`done`, `current`, or `upcoming`).
  - Shows a countdown for the current task and a random motivational reminder.

- **`/update` Route**:
  - Provides a JSON response with the updated task schedule and a random reminder.

---

## Example Response from `/update` Endpoint

```json
{
  "tasks": [
    {"task": "Task 1", "status": "done", "time": "12:30"},
    {"task": "Task 2", "status": "current", "time": "20m remaining"},
    {"task": "Task 3", "status": "upcoming", "time": "14:00"}
  ],
  "reminder": "I am getting better every day"
}
```

---

## Customization

- **Tasks**: Modify the `tasks.json` file to add, remove, or update tasks and their durations.
- **Reminders**: Edit the `list_of_reminders` in the code to include your own motivational quotes or reminders.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Author

Bayo Browne  
(https://github.com/bbrowne1)
---

Enjoy staying productive with the Productivity App! 🚀
![Visitor Count](https://komarev.com/ghpvc/?username=bbrowne1&repo=productivity-app&color=blue)
