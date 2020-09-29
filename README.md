# IPL-database
Major project for Data and Application course during Monsoon'20 semester

# Loading the database
1. ```mysql -u username -p IPL < database.sql```

# Tables

<b>To Samay and teja: tables ka naam exactly yahi rakhna taaki panga na ho</b>

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

# Useful MySQL commands
Adding so I dont have to google these again and again :P
1. ```SHOW CREATE TABLE Players;``` : Shows all the details of the table
2. ```SHOW columns FROM table_name```: Show details of columns
2. ```ALTER TABLE table_name ADD column_name datatype values```: Add column to table. Values can be things like ```NOT NULL```, ```PRIMARY KEY```, etc
3. ```ALTER TABLE table_name ADD CONSTRAINT constraint_name CHECK constraint```: Add constraints
4. ```ALTER TABLE table_name DROP CONSTRAINT constraint_name```: Remove constraint
