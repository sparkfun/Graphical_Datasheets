Graphical Datasheets
========================================

Code, final versions, and information on the Sparkfun Graphical Datasheets.

This repo includes the Python script used to help generate the graphical datasheets.  It also includes the final .svg, and .pdf files as well as the .csv files use for development boards.  The .csv files were used as a starting point and some text did change between the file and the final version.  There is also a User Submitted folder for external contributions.

Software Setup Notes
-------------------

We recommend using **Notepad++** to run the script. From **Notepad++**'s **Plugins** > **Plugins Admin...** menu, search for **PyNPP** plug-in and install. Then [download and unzip the **svgwrite** module](https://pypi.python.org/pypi/svgwrite/). In a command line, change the path to where **...\svgwrite** folder is located and use the "`C:\Python27\python setup.py install`" command to install.

Once you have created a CSV of the pinout for your development board (you can also edit the CSV from any of the examples), run the **tagscript.py** in the same path using Notepad++. A window will pop up requesting for the CSV file name. After entering the file name, it will output the SVG with the same name.

After running the script, open the SVG file in Inkscape (or your Illustrator) with an image of your development board to align or adjust the pinouts! Have fun!

Required Software
-------------------

Some software used to create graphical datasheets.

* **[Notepad++](https://notepad-plus-plus.org/download/v7.7.1.html)**
* **[Inkscape](https://inkscape.org/release/inkscape-0.92.4/)**

Repository Contents
-------------------

* **/Datasheets** - CSV of pinouts and graphical datasheets for development boards
* **tagscript.py** - Script to generate cells for graphical datasheets
* **tagscript_original-mshorter.py** - Originally script to individually modify each column attribute if necessary

Documentation
--------------

* [Enginursday: Graphical Datasheets](https://www.sparkfun.com/news/1947) - For more information on the graphical datasheets check out our blog post on them.
