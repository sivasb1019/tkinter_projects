# Complaint Management
* This code is for a graphical user interface (GUI) application built using the Tkinter library in Python.
* It allows users to register and manage complaints. Here's a description of the code:

### 1. The code begins by importing the necessary modules:
* **Tkinter:** This is the GUI library used to create the graphical interface.
* **messagebox:** It provides a way to display messages or alerts to the user.
* **ttk:** The Tkinter themed widget set for enhanced GUI components.
* **sqlite3:** Used for creating and managing a SQLite database.
* 
### 2. A class named Database is defined to handle database operations:
* The constructor (__init__) initializes a SQLite database connection and creates a table named complaintList if it doesn't already exist.
* This table is used to store complaints.
  
### 3. Several functions are defined:

* **insert:** Inserts complaint details into the database.
* **fetch:** Retrieves all data from the complaintList table.
* **displayAll:** Clears the current display and populates the GUI table with all complaints.
* **addComplaint:** Validates and adds a new complaint to the database.
* **clearAll:** Clears input fields in the GUI.
* **getData:** Retrieves and displays complaint data when a row in the GUI table is selected.
  
**4. An instance of the Database class is created with the database file "Complaints.db".**

###  5. The main GUI window is created using Tkinter (Tk class) and configured with properties such as the title, geometry, background color, and maximized state.

###  6. Labels and input fields for the complaint details (Name, Age, Email, Contact No, Complaints) are created and positioned within the GUI.

### 7. Buttons are added to the GUI for submitting complaints, clearing input fields, and displaying the list of complaints.

### 8. A section for displaying the list of complaints is created using a ttk.Treeview widget.

### 9. The Treeview is configured with columns to display complaint data, and a function is defined to handle row selection to view complaint details.

### 10. The main event loop (window.mainloop()) is started to run the GUI application.

### 11.Thi s code creates a simple GUI application for registering and managing complaints, allowing users to add, view, and clear complaint entries. It stores the complaint data in a SQLite database.
