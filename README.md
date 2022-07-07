# Uncrop Scripts
 The DaVinci Resolve scripts, setting, and Macro for uncropping/panning/whatever you want to do.

initial setup:
1. download DaVinci Resolve 8 Beta.
2. in github click Code then Download ZIP. unzip the file.
3. run install_python.bat as NOT administrator. Allow access to Python.exe in tool bar. (if it doesnt work, as in closes shortly after it runs, re-run script a couple times).
3. create new project.
4. go to fusion in the menu bar then Fusion Settings.
5. click path map then open up the Macros folder and add macros from macro folder.
6. open the Scripts folder and add the comp folder.


setup for padding:
1. drag buffer.drp into DaVinci Resolve Projects.
2. open buffer and go to the fusion tab (wand at bottom middle).
3. set the export path for both OriginalSaver and ExportSaver (have OriginalSaver end with Original.png and ExportSaver end with Export.png).
4. if canvas isn't the right size go to File > Project Settings then change timeline resolution to 1024 x 1024.
5. go back to the edit tab and make the Fusion Composition a handful amount of frames wide for performance.


add padding to an image:
1. add image to media pool.
2. select Image node.
3. drag image from media pool to the Clip Name property at the top of Tools.
4. select Pan node and set the Center and Size.
5. go to menu bar and click Workspace > Scripts > Export.
6. go to export folder (path of saver nodes) and add Export0001.png to image generating software (keep other image for later).
7. repeat for every image.


combine images:
0. create a project and set frame rate and resolution under File > Project Settings.
1. go to media pool root folder and right click > New Bin and name it ToConvert (case sensitive).
2. drag all images with the formatted names into the folder.
3. add last image and name it the image number (if it is the 8th image name it "8.png") all files must be named in file explorer.
4. drag first clip onto timeline.
5. hover over it and open fusion.
6. select MediaIn1.
7. go to menu bar and click Workspace > Scripts > VariablePan.
8. dont click anything.

to zoom out:
1. select last image in time line.
2. hit shift + space and add the zoom tool.
3. set the Start Frame and Size and the End Frame and Size.

If you have any questions or make anything don't be scared to msg or email me. My discord is pig3253#2053 and my email is maxrort@gmail.com
