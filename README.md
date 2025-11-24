Simple CLI Pregnancy Tracker
# Project Description

This is a straightforward Command-Line Interface (CLI) application developed in Python to help expectant parents track their pregnancy week by week. The application calculates the Expected Delivery Date (EDD), identifies the current trimester, and provides relevant, pre-defined information based on the current week, including:
* Baby's comparative size.
* Key safety tips and nutrition advice.
* Average expected weight gain range.
* Upcoming medical milestones.
* A log for tracking weekly symptoms and weight.

# Setup and How to Run

Since this application uses only standard Python libraries (datetime and json), no external dependencies are required
1. Save the Code: Save the provided Python script as a file (e.g., pregnancy_tracker.py).
2.Execute: Run the script from your terminal:

python pregnancy_tracker.py

3.Input: The application will prompt you for four pieces of information:
*Current pregnancy week (1-40).
*First day of last menstrual period (LMP) in YYYY-MM-DD format (e.g., 2025-01-01).
*Current weight in kilograms (kg).
*Any symptoms experienced this week, separated by commas.

# Core Features and Functions

Data Dictionaries (The Knowledge Base)

*b (Weekly Content): Stores core information (size, tip, nutrition, weight gain) mapped to specific week numbers (1, 12, 20, 28, 36, 40).

*m (Milestones): Stores descriptions for major medical checkups or events mapped to specific weeks (12, 16, 20, 28, 36).

*t (Trimesters): Stores the general advice notes for each of the three trimesters (keys 1, 2, and 3).

Calculation and Utility Functions

*a(s) (EDD Calculation): Calculates the Expected Delivery Date by adding a timedelta of 40 weeks to the Last Menstrual Period date (s).

*v(w) (Trimester Check): Returns the trimester number (1, 2, or 3) based on simple conditional checks against the current week (w).

*x(w) (Content Lookup): Crucial for content retrieval. This function finds the largest week key in dictionary b that is less than or equal to the current week. This ensures the user always gets the most recent, relevant weekly advice, even if data for the exact week is missing.

*y(ed) (Days Left): Calculates the number of days remaining by finding the difference between the EDD (ed) and the current system date.

*z(d, f) (Data Persistence): Handles saving the current weekly progress (d) to the specified JSON file (f). It reads existing data, Data 

# Persistence (Progress Log)

The application saves a history of weekly records to a file named pp.json.

*Format: The data is saved as a JSON array of objects.

*Data Saved: Each entry includes the week, the date of entry, current weight, and reported symptoms.

*Mechanism: The z function uses a try/except block to gracefully handle the initial creation of the file and ensures that new data is appended to the existing log.appends the new record, and overwrites the file with the complete, updated history.
Mechanism: The z function uses a try/except block to gracefully handle the initial creation of the file and ensures that new data is appended to the existing log.
