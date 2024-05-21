# Terminal Application: LITESPEED CRM for Sales

This application is a Customer Relationship Management (CRM) system that helps businesses efficiently manage and store customer data. Developed from my experience in software sales, this application solves a problem I encountered in my previous role.

It allows sales development representatives to quickly identify if a lead has already been assigned to a different team member by entering the company URL. The application includes essential CRM functionality to add new leads, edit existing leads, remove leads, and search/display lead information.

## Link to GitHub Repository

[GitHub](https://github.com/Kasun1Don/terminal_app)


Link Address: `https://github.com/Kasun1Don/terminal_app`

## Style Guide

The terminal application has been written in Python following the [PEP 8](https://peps.python.org/pep-0008/) style guide and conventions.

## Key Features

## Implementation Plan

The implementation plan was tracked using a Trello Kanban board.

The implementation plan included cards for each Key Feature, with a due date and a checklist of tasks in order of priority.

### Feature Implementation Checklists:

In order of the terminal application's main menu options:


### Kanban Progress Tracking Screenshots:

The following screenshots were taken over the course of the application development period:

<img src="/docs/Trello_1.png" width="500" height="auto">

<img src="/docs/Trello_2.png" width="500" height="auto">

<img src="/docs/Trello_3.png" width="500" height="auto">

<img src="/docs/Trello_4.png" width="500" height="auto">

## Installation Instructions

1. To run the program, open the GitHub repository and click the green [ < > Code ] button. Select 'Download ZIP'

2. Save the ZIP file to a directory which can be navigated to using the terminal. Unzip the file.

In the Terminal:

3. Navigate to the directory where the file was unzipped. Change directory (cd) to the `terminal_app-main` folder.

4. Change permissions to make the script executable by entering:

```bash
chmod +x run_crm.sh
```

5. Run the script by entering the following command:

```bash
./run_crm.sh
```

6. The script will install all required dependencies listed in the Dependencies section below.

7. The terminal application will prompt for input.

8. On MacOS: for the best user experience, drag the corner of the terminal window to set width & height to at least `100 x 40`.

9. To exit the application at any time use `Ctrl + C`.

Note: 

* This application primarily requires company URLs to interact with the lead database.

    A list of Company URLs to test the application :

    ```
    https://www.vercel.com
    https://www.miro.com
    https://www.salesforce.com
    https://www.zoom.us

    (the application uses this URL format)
    ```

* if an error message says "This program runs on Python3, but it looks like Python3 is not installed.", refer to System Requirements below:

## System Requirements

The application requires Python version 3.10 or above to run. 

Check your machine's Python version or if it has python installed by trying the following terminal commands:

```bash
python --version

python3 --version
```
If both return an error message or the version requires updating, follow this [Python installation guide](https://wiki.python.org/moin/BeginnersGuide/Download) to install or upgrade to the latest version of Python.


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

