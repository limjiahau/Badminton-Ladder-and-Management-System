# Badminton-Ladder-and-Management-System

### Main Selection Screen:
![image](https://github.com/limjiahau/Badminton-Ladder-and-Management-System/blob/9da36f24710f89986d4a7a04e788de79e5bcf52a/badminton.JPG)

### Introduction of Project:

Developed a data management program for managing a badminton ladder. Players are placed in an ordered list and can challenge others who are ranked higher. 

### How to Run the Program:

Running the "main.py" file will lead you to the Main Selection Screen as shown. The helper files, "load.py", "actions.py", "queries.py" are additional code for the program to run as intended. 

### Rules:
1) A player on the ladder may only challenge another player up to three ranks above. 
2) If the challenger wins, he/she may move into the position of the challenged. The challenged moves down the ladder by one place.
3) If the challenger loses, the ladder remains unchanged.
4) A new player joins the bottom of the ladder.
5) When a player leaves, everyone below moves up by one place to occupy the vacated spot.

### Features of Program:
1) Issue a challenge (stating opponent and play-by date)
2) Record the result of the challenge
3) Join the ladder 
4) Withdraw from the ladder
5) Make a query

### Data Files
1) ladder.txt
  - Contains current order of the ladder
2) data.txt
  - Contains data on every challenge, and 
  - The coming and going of players. 
  - Chronological order, with the latest data inserted at the end of the file.
  
