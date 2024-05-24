## Potato Data Analytics App

### Overview

This project is a simple data analytics application for tracking and analyzing potato plant data. It includes functionality for logging plant data, testing for diseases, and visualizing the data in an admin area.

### Features

- **Add Entries**: Log data for potato plants, including plant ID, disease type, test results, field location, and date logged.
- **Admin Area**: View and manage logged data in a tabular format with sorting, searching, and pagination features.

### Technologies Used

- **Flask**: Web framework for Python.
- **SQLite**: Lightweight database.
- **HTML/CSS/JavaScript**: Frontend technologies.
- **DataTables**: jQuery plugin for advanced table features.

### Project Structure

potato_data_app/
│
├── app.py
├── potato_data.db
├── templates/
│ ├── index.html
│ └── admin.html
├── static/
│ └── styles.css
└── README.md


### Installation

1. **Clone the Repository**:
   ```bash
   git clone %link%
   cd potato_data_app
   
2. **Create and Activate a Virtual Environment (optional but recommended**):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install Dependencies**:
    ```bash
    pip install Flask
    pip install Flask-SQLAlchemy
