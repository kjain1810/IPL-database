# IPL-database

Major project for Data and Application course during Monsoon'20 semester

# Introduction

This miniworld is a scaled down replica of the Indian Premier League. We have tried to incorporate as many features which you would be able to access in the real world scenario. You have to ability to track statistics across multiple seasons. You can even find aggregate data from all the seasons put together. 

# Requirements

To run this mini-world on your system you need:
1. SQL Server
2. Python Modules - PyMySQL and Tabulate

# Installation

1. To install MySQL in Windows use this link <https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/windows-install-archive.html>   
    For Ubuntu use this link <https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04>   
    For MacOS use this link <https://database.guide/how-to-install-sql-server-on-a-mac/>
2. For Python Libraries run these commands on your terminal-    
   `pip install pymysql`     
   `pip install tabulate`

# Loading the database
1. ```mysql -u ***username*** -p IPL < populatedDatabase.sql```
2. ```mysql -u ***username*** -p IPL < database.sql```

Use the first command if you want to use a populated database and test the features only. 
Use the second command if you want to use a fresh database which is not populated. 

**NOTE** Make sure you create an empty database called IPL in your SQL server before running these commands.

# HOWTO

1. Use the command `python IPL.py` to start the CLI.
2. Enter your SQL username and password which you used to load the database. 
3. You will be shown a menu which shows the functions groups that can be executed.
4. Upon selecting a group, a submenu will show up on your screen from which you can select a funtion of the group.
5. For example pressing `1` will take you to the submenu for the add group. Upon pressing `1` again you will be able to add a new player to the database.
6. If you are using the fresh database follow these steps to populate the database:
  1. Add a season.
  2. Add teams(at least 2).
  3. Add players(ensure that at least 2 teams have 11 players)
  4. Add Home Stadiums for your teams. 
  5. Add Team Management for your teams.
  6. Now, you can add any number of matches between teams.
7. You also have the option to end the current season and start a new one. 
8. You can search for Players, Teams, and Stadiums by name.
9. You can also view statistics like the Orange Cap Winner(Most Runs) etc.
10. To add a Team Captain, update the team from the update menu. 
11. Play around to use all the remaining features :)

# Requirements

The exhaustive list of requirements is below:

## Functional Requirements [COMPLETED]
- [x] Retrieve Players, Teams, Matches,Seaons, Stadiums.
- [x] Retrieve all players and management of a particular Team.
- [x] Retrieve overall top scorers or top scorers of currently running season in terms of runs and wickets.
- [x] Retrieve position of a team in a particular season, position of a team across all seasons, and their points in the ongoing season.
- [x] Calculate average total wickets and/or average total runs of a player in a particular season or overall.
- [x] Search Players, Teams, Stadiums by name.
- [x]  
- [x] Retrieve number of matches played in a stadium.
- [x] Add matches, players, teams, seasons, stadiums, and Team management.
- [x] Remove players, and team management.
- [x] Update players, teams, and stadiums.

## Database Requirements [COMPLETED]
- [x] Players <br>
- [x] Teams <br>
- [x] Batsman<br>
- [x] Bowler<br>
- [x] AllRounder<br>
- [x] TeamManagement<br>
- [x] Seasons<br>
- [x] Matches<br>
- [x] Stadium<br>
- [x] TeamStandings<br>
- [x] Plays<br>
- [x] Scorecard<br>
- [x] TeamResults<br>
- [x] PlayerScorecard<br>
