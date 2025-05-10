This is a Flask application that takes as input a CSV containing a category listing
and transform the CSV to a nested JSON document which will form a tree structure.  
The CSV represents a typical listing of Department > Aisle > Shelf for a theoretical 
supermarket.  The JSON document could possibly be consumed by the supermarket's website
for displaying the hierarchy of categories for the products being sold at the supermarket.
Note that the category hierarchy is not limited to three levels.

Pre-requisites:

    python 3.8
    python3.8-venv (for Ubuntu 20.04)

The repository contains scripts for installing the application's files.  
First, navigate into the repository's directory.  Then,

- On Windows 10, you can do: `installation_scripts\install.bat`
- On Ubuntu 20.04, you can do: `source installation_scripts/install.sh`

The code coverage report is automatically generated and can be found in `tests/cov_html/index.html`.

The Flask application is automatically started.  Open your web browser to http://localhost:5000.  
This will take you to a page where you can select a file as input to the file generator.

<img src="images/1 - start.jpg" width="70" height="40"/>

After clicking "Choose File" a file dialog will appear to enable you to select the input CSV.

<img src="images/2 - file selection.jpg" width="150" height="100"/>

After selecting the input file, click "Process".

<img src="images/3 - process.jpg" width="70" height="40"/>

After clicking "Process" the JSON document will be displayed on the next page.

<img src="images/4 - results.jpg" width="150" height="100"/>

Click "Back to file generator" to return to http://localhost:5000.


