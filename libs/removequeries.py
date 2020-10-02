#!/usr/bin/env python3

def removePlayer(cur, con):
    try:
        deleteplayer = input("Enter name of player to be deleted: ")
        query = "DELETE FROM Players WHERE Name = %s" %(deleteplayer)
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
    try:
        teamName = input("Name: ")
        query = "DELETE FROM Teams WHERE Name = '%s'" % (teamName)
        cur.execute(query)
        con.commit()
        print("Team deleted!")
    except Exception as e:
        con.rollback()
        print("Deletion failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue> ")
    return

def removeMatch(cur, con):
    pass

def removeSeason(cur, con):
    pass

def removeStadium(cur, con):
    pass



