echo Execuite Build to EXE
echo **********************************************
echo **********************************************
echo BUILDING THE UI FILES
pyuic5 -x dave_widget.ui -o dave_widget.py
echo pyinstaller Running...
pyinstaller --onefile daveApp.py
cd ./dist/
ren daveApp DAVE_GUI
cd ./../
echo **********************************************
echo **********************************************
echo EXE BUILD COMPLETE!
echo The end file is saved in the dist Folder
