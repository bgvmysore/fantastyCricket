## Fantasy Cricket Application

This is an app that lets you to build cricket teams from available list of 
players and evalutate their performance from available match data.

![startscreen](https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/start_ui.png)

## How it Works?

Run the Run.py and in menu bar choose "Manage Teams" and select "New Team".

![Menubar](https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/menubar.png)

Choose the players from the list in left hand side.They are organised by their
roles.DOuble click to choose.

![newteam_window](https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/newteam.png)

Once the team is selected goto "Manage Teams" menu and select "Evaluate"

In Evaluate Window you have a drop down of available matches.Select one from 
the list and click evaluate button. A list of players scores will appear after
that you can close the Evaluate window.

![EvaluateWindow](https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/eval.png)

Also, once players for you team is selected you can save the team by going to 
"Manage teams" and selecting "Save Team".Once a team is saved you can open it 
next time by selecting "Open Team" instead of "New Team" from "Manage Team" 
menu.

![savewindow](https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/save.png)
![openwindow](https://github.com/bgvmysore/fantastyCricket/blob/master/screenhots/open.png)

## Project Organisation

1.Run Run.py to open application.

2.Databases is found in db folder.

3.DB are split into 3 cricket.db contains players,teams.db contains teams saved
,matches.db contains match details.

4.UI Files folder contains pyqt5 designer files.


Note: You can add your own Match data or Player Data in the respected SQLite 
Databases present in 'db' directory. Make sure you populate all the required
columns.
