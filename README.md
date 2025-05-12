# Overview
This is a Flask application that takes as input a CSV containing a category listing
and transform the CSV to a nested JSON document which will form a tree structure.  
The CSV represents a typical listing of Department > Aisle > Shelf for a theoretical 
supermarket.  The JSON document could possibly be consumed by the supermarket's website
for displaying the hierarchy of categories for the products being sold at the supermarket.
Note that the category hierarchy is not limited to three levels.

# Installation
### Using Docker
The repository contains a Dockerfile that you can use to build a docker image of the 
application.  Open your terminal and navigate to the repository's directory.  Then, execute

    docker build -t fuzzy-enigma .

Run the application using:

    docker run --publish 5000:5000 --volume fs:/app/out --detach --name fuzzy-enigma --rm fuzzy-enigma

To see the coverage report, do:

    docker volume inspect fs

The coverage report will be in <"Mountpoint">/cov_html.

### Using installation scripts
The repository contains scripts for installing the application's files.  
Open your terminal and navigate to the repository's directory.  Then,

On Windows, you can execute:

    installation_scripts\install.bat

On Linux, you can execute:

    source installation_scripts/install.sh

The code coverage report will be automatically generated and can be found in

    tests/cov_html/index.html

The Flask application will be automatically started.  

# Usage
Open your web browser to http://localhost:5000.  
This will take you to a page where you can select a file as input to the file generator.

<img src="images/1 - start.jpg" width="70" height="40"/>

After clicking "Choose File" a file dialog will appear to enable you to select the input CSV.

<img src="images/2 - file selection.jpg" width="150" height="100"/>

After selecting the input file, click "Process".

<img src="images/3 - process.jpg" width="70" height="40"/>

After clicking "Process" the JSON document will be displayed on the next page.

<img src="images/4 - results.jpg" width="150" height="100"/>

Click "Back to file generator" to return to http://localhost:5000.
