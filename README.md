# Badminton-Ladder-and-Management-System
## MA1008 Introduction to Computational Thinking (Mini-Project)

### Main Selection Screen:
![image](https://user-images.githubusercontent.com/65124287/206387679-6a4920d6-2b1a-4b13-ba66-11a72adb1b87.png)

### Introduction of Project:

Develop a data management program for managing a badminton ladder. Players are placed in an ordered list and can challenge others who are ranked higher. 

### How to Run the Program:

Running the "main.py" file will lead you to the Main Selection Screen as shown. The helper files, "load.py", "actions.py", "queries.py" are additional code for the program to run as intended. 
Please view the docx. file for the full set of instructions. 

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
  
