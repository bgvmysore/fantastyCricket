# Fantasy Cricket Application

This is an app that lets you to build cricket teams from available list of 
players and evalutate their performance from available match data.

<img src="https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/start_ui.png" alt="startscreen" width="500">

## How it Works?

Run the Run.py and in menu barchoose "Manage Teams" and select "New Team".
<img src="https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/menubar.png" alt="menubar" width="500">

Choose the players from the list in left hand side.They are organised by their
roles.Double click to choose.
<img src="https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/newteam.png" alt="newteamwindow" width="500">

Once the team is selected goto "Manage Teams" menu and select "Evaluate"
In Evaluate Window you have a drop down of available matches.Select one from 
the list and click evaluate button. A list of players scores will appear after
that you can close the Evaluate window.
<img src="https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/eval.png" alt="EvaluateWindow" width="500">

Also, once players for you team is selected you can save the team by going to 
"Manage teams" and selecting "Save Team".
<img src="https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/save.png" alt="saveWindow" width="500">

Once a team is saved you can open it next time by selecting "Open Team" instead of "New Team" from "Manage Team" 
menu.
<img src="https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/open.png" alt="openWindow" width="500">

If you want to clone this repo and use this project make sure you have the following:

### Dependencies

  1. python3
  2. SQLite
  3. pyqt5
  4. pyqt5-tools
  

## Project Organisation

1.Run Run.py to open application.

2.Databases is found in db folder.

3.DB are split into 3 cricket.db contains players,teams.db contains teams saved,matches.db contains match details.

4.UI Files folder contains pyqt5 designer files.


**Note**: You can add your own Match data or Player Data in the respected SQLite 
Databases present in 'db' directory. Make sure you populate all the required
columns.
