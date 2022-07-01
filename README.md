# Uncrop Scripts
 The DaVinci Resolve scripts, setting, and Macro for uncropping/panning/whatever you want to do.

initial setup:
1. download DaVinci Resolve.
2. download files from github.
3. create new project for adding buffer to your images
4. go to fusion in the menu bar then Fusion Settings
5. click path map then open up the Macros folder and add Fade.settings (In Uncrop-Scripts Macro folder).
6. open the Scripts folder and add the comp folder
7. download python https://www.python.org/downloads/ AT THE BOTTOM SELECT "Add Python to PATH" click install. after that click the extend environment variable length button if there
8. reset computer
9. open a command prompt as administrator 
10. run the following commands
pip install wheel
pip install pipwin

pipwin install numpy
pipwin install pandas
pipwin install shapely
pipwin install gdal
pipwin install fiona
pipwin install pyproj
pipwin install six
pipwin install rtree
pipwin install geopandas


setup for padding:
1. open buffer project
2. click on the fusion tab at the bottom (the wand)
3. drag the ImageBuffer.setting file under the Settings folder into the nodes space (if there are 2 media outs then delite the second one)
4. set the export path for both OriginalSaver and ExportSaver (have OriginalSaver end with Original.png and ExportSaver end with Export.png)
5. if canvas isn't the right size go to File > Project Settings then change timeline resolution to 1024 x 1024
6. go back to the edit tab and make the Fusion Composition a handful amount of frames wide for performance


add padding to an image:
1. add image to media pool
2. select Image node
3. drag image from media pool to the Clip Name property at the top of Tools
4. select Pan node and set the Center and Size
5. go to menu bar and click Workspace > Scripts > Export
6. go to export folder (path of saver nodes) and add Export0001.png to image generating software (keep other image for later)
7. repeat for every image


combine images:
1. go to media pool root folder and right click > New Bin and name it ToConvert (case sensitive)
2. drag all images with the formatted names into the folder
3. add last image and name it the image number (if it is the 8th image name it "8.png") all files must be named in file explorer
4. drag first clip onto timeline
5. hover over it and open fusion
6. select MediaIn1
7. go to menu bar and click Workspace > Scripts > VariablePan
8. dont click anything


If you have any questions or make anything don't be scared to msg or email me. My email is maxrort@gmail.com