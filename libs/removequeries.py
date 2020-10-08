#!/usr/bin/env python3
from tabulate import tabulate

def removePlayer(cur, con):
    try:
        query = "SELECT * FROM Players"
        cur.execute(query)
        rows = cur.fetchall()
        headers = rows[0].keys()
        rows = [x.values() for x in rows]
        print(tabulate(rows, headers, tablefmt="pretty"))
        deleteplayer = int(input("Enter the ID of the player that you want to delete: "))
        query = "SELECT * FROM Teams WHERE CaptainID = %d" % (deleteplayer)
        cur.execute(query)
        rows = cur.fetchall()
        if(len(rows)>0):
            print("Player to be deleted should not be captain of any team, change the captain from update teams!")
            tmp = input("Enter any key to continue> ")
            return
        query = "UPDATE Matches SET Mom = NULL WHERE Mom = %d" % (deleteplayer)
        cur.execute(query)
        cascade = ["Batsman", "AllRounder", "Bowler", "PlayerScorecard", "Players"]
        for i in cascade:
            query = "DELETE FROM %s WHERE PlayerID = %d" % (i, deleteplayer)
            cur.execute(query)
        con.commit()
        print("Player deleted!")
    except Exception as e:
        con.rollback()
        print('Deletion failed :(')
        print('Error', e)
    tmp = input("Enter any key to continue> ")
    return        

def removeTeam(cur, con):
    pass

def removeMatch(cur, con):
    pass

def removeSeason(cur, con):
    pass

def removeStadium(cur, con):
    pass

def removeTeamManagement(cur, con):
    try:
        query = "SELECT * FROM TeamManagement"
        cur.execute(query)
        rows = cur.fetchall()
        headers = rows[0].keys()
        rows = [x.values() for x in rows]
        print(tabulate(rows, headers, tablefmt="pretty"))
        name = input("Type the name of the team management that you want to delete: ")
        query = "DELETE FROM TeamManagement WHERE Name = '%s'" % (name)
        cur.execute(query)
        con.commit()
        print("Team Management deleted")
    except Exception as e:
        con.rollback()
        print('Deletion failed :(')
        print('Error', e)
    tmp = input("Enter any key to continue> ")
    return   





