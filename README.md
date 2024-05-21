# Terminal Application: LITESPEED CRM for Sales

This application is a Customer Relationship Management (CRM) system that helps businesses efficiently manage and store customer data. Developed from my experience in software sales, this application solves a problem I encountered in my previous role.

It allows sales development representatives to quickly identify if a lead has already been assigned to a different team member by entering the company URL. The application includes essential CRM functionality to add new leads, edit existing leads, remove leads, and search/display lead information.

## Link to GitHub Repository

[GitHub](https://github.com/Kasun1Don/terminal_app)


Link Address: https://github.com/Kasun1Don/terminal_app

## Style Guide

The terminal application has been written in Python following the [PEP 8](https://peps.python.org/pep-0008/) style guide and conventions.

## Key Features

## Implementation Plan
Kanban board 

### Feature Implementation Checklists:

### Kanban Progress Tracking Screenshots:

## Installation Instructions
To run the program, open the GitHub repository and click the green " < > Code " button. Select 'Download ZIP'

Save the ZIP file to a directory which can be navigate to using the terminal. Unzip the file.

In the Terminal:

Navigate to the foldeer containing the unzipped file. Open or cd into the terminal_app directory.

```bash
chmod +x run_crm.sh
```
Run the script by entering the following command:
```bash
./run_crm.sh
```

3. The script will install all required dependencies listed in the Dependencies section.

*if an error message says "This program runs on Python3, but it looks like Python3 is not installed." refer to System Requirements below:

## System Requirements

The application requires Python version 3.10 or above to run. Check your machine's Python version or if it has python installed by trying the following terminal commands:

```
python --version

python3 --version
```
If both return an error message or the version requires updating, follow the Python installation guide to install or upgrade to the latest version of Python.


## Dependencies and Packages
The Python application requires the following packages:

* colorama: for colored text in the terminal
* pandas: for reading and manipulating CSV files
* tabulate: for formatting tables in the terminal
* uuid: for generating unique identifiers
* datetime: for handling date and time

The package dependencies installed when running the program are as follows:
```
colorama==0.4.6
numpy==1.26.4
pandas==2.2.2
python-dateutil==2.9.0.post0
pytz==2024.1
six==1.16.0
tabulate==0.9.0
tzdata==2024.1
```

## References

