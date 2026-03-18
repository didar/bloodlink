# Bloodlink: Blood Donation Management System
*A terminal-based Command Line Interface (CLI) application developed for an Introduction to Programming course.*

Bloodlink serves as a lightweight, in-memory database with persistent file storage, designed to efficiently manage and connect blood donors with patients in need.

## Features
* **Donor & Patient Management:** Easily register, view, and organize blood donors and active patient requests.
* **Smart Matching Algorithm:** Automatically pairs patients with compatible donors based on an exact blood group match and a geographic proximity match.
* **Fuzzy Searching:** Features a custom, fault-tolerant search engine that finds correct records even if the user makes a minor typo or enters a partial location.
* **Data Persistence:** Automatically serializes and saves all records locally to `donors.txt` and `requests.txt` to ensure data is retained between sessions.
* **Strict Input Validation:** Enforces data integrity by rejecting invalid blood types and ensuring all phone numbers meet the standard 11-digit Bangladeshi format.

## Prerequisites
* Python 3.x
* No external libraries or installations are required (the application relies entirely on Python's built-in standard libraries like `difflib` and `pathlib`).

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the directory containing the project.
3. Execute the script using Python:
   ```bash
   python bloodlink.py
