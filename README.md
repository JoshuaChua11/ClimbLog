# ClimbLog
ClimbLog is a user-controlled tracker, offering climbers with a universal method to log both standardised and local completed climbs. It boasts several key features: 
* Seemless connection to standardised boards.
* Progress tracking and progression estimation.
* Easy access to videos and articles based on progression, climbing grade and style of climb.

> [!NOTE]
> The project currently only contains the backend code, ensure that all elements are accessed on console through __main__.py.

> [!WARNING]
> ClimbLog currently only logs bouldering and does not support sport climbing grades as of currently.
  
## :wave: Installation 
This guide will discuss the necessary modules and steps to access ClimbLog as intended: 
### Step - 1:
Install Boardlib.
```
python3 -m pip install boardlib
```
### Step - 2:
As BoardLib requires a sqlite database file containing all publicaly available data to each board. ClimbLog utilises the CSV outputs of BoardLib and requires the databases to be downloaded for each given board desired. 
> [!NOTE]
> It is recommended to download all available databases.
__Recommended Boards:__ Kilter, Tension, Decoy, Aurora, Touchstone.
```
boardlib database <board_name> <database_path>
```

## 	:card_file_box: Features
Users are given access to 4 main operations: 

### :date: Fetch Logbook 
Allows users to login into an account held for any of the recommended boards, and retrieves all saved and completed climbs in the users' logbook. Details of the logbook are currently returned through the terminal providing information on the board, angle, name of climb, date completed, logged and displayed grade, diffuculty and number of attempts. 

### :pen: Manual Log 
Operation allows users to log climbs onto ClimbLog that aren't completed on set boards. Allowing users to keep track of all climbs completed at local gyms for a full comprehensive record of completed climbs. 

### :climbing: Improvement Tracking 
ClimbLog helps users quantify their improvement through displaying their current and next target grades. Although it is important to soley focus on grades when climbing, ClimbLog provides users a prediction based on their current rate of climbing to when they should expect to reach their next goal!

### AI Recommended training videos
ClimbLog provides users with the option of utilising their current data to help find content better suited to their current needs. The program utilises current grade data, the duration spent at each grade, the rate of improvement and the desired outcome to generate users with easily accessable content to aid in their progression. 

## :telescope: Future Features
- [ ] Construct the front-end web site for ClimbLog
- [ ] Expand ClimbLog to include sportclimbing grades alongside an interactable map
- [ ] Improve the tracking calculations through fixed data

## :newspaper: Credits
This program was built with BoardLib produced by [Luke Emery-Fertitta](https://github.com/lemeryfertitta).
