# Welcome to our SC3020 Course Project 2
## About

This is a project for SC3020 (Database System Principles) where we:
1. Developed a PostgreSQL-based application to analyze and visualize query execution plans and block access patterns in a TPC-H dataset.

2. Designed and implemented a user-friendly graphical user interface using Python, Flask, and Tkinter to display natural language explanations of input queries and graphical representations such as QEP trees and heat maps.

3. Displayed query performance metrics such as execution time, planning time, total cost, node counts, average actual time for each node type, and shared buffer statistics.


## Conclusion
Our software enables users to better understand what is happening “inside the box” of a database system when they pose a SQL query. It has an easy to use interface and is
feature-rich. Users will know various behind the scenes processes of their query, such as time taken and most/least costly steps. Users can also better understand the set of physical
operators that takes one or more data streams as input and produces an output data stream through our QEP output in natural language and our QEP tree diagram. Last but not least, users
can gain a better understanding of blocks in their database. As such, users will gain more insights into the inner workings of databases.

## Refer to the below for Installation Instructions

Please ensure that you are using Python 3.11 to run our application code. We recommend creating a virtual environment to install our package dependencies.

1. Install GraphViz 9.0.0 from https://graphviz.org/download/ for the operating system you are running the source code from. This software is used to render our QEP. No further action is needed after it is installed on your computer.
    a) It is available via Windows Package Manager with command - winget install graphviz
    b) It is available via Homebrew with command - brew install graphviz.
    c)Please restart the terminal / IDE after installing this package and before running our code to allow the path variable to be updated.
2. Open PyCharm
3. Click ‘Open…’ under ‘File’ tab:
4. Select our folder
5. Press ‘Alt+F12’ to go to PyCharm terminal:
6. Type ‘python -m venv project2’ to create virtual environment:
7. Type ‘project2\Scripts\activate’ to activate virtual environment:
8. Type ‘pip install -r requirements.txt’ to install all dependencies:
9. Type ‘python project.py’ to run our software:
10. On the login screen, please enter the following information:
    a) Port - corresponds to the port number that your PostgreSQL server is running on. This can be obtained through inspecting server properties on applications like pgAdmin4.
    b) Host - localhost if you are running the PostgreSQL server on the same machine as the code is being run on.
    c) Database - name of the database on your PostgreSQL server that you wish to make queries to.
    d) Username - postgres username
    e) Password - postgres password
11. It is advised to close the application every time from the terminal via <Control + C> keyboard shortcut and not the window directly to ensure the flask app is terminated and the port 5000 is cleared. In the case that the port is occupied, the following commands can help you clear the 5000 port to ensure a smooth connection to the flask app.

```bash
sudo lsof -i :5000  # take note of the Process ID
sudo kill -9 <Process ID of the python app>
```


These commands should help you clear the port.

## Run this command for Mac to get Tkinter working
brew install python-tk
brew install graphviz

