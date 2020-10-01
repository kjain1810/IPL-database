#!/usr/bin/env python3

def addPlayer(cur, con):
    try:
        newPlayer = {}
        newPlayer["Name"] = input("Name: ")
        newPlayer["Age"] = int(input("Age: "))
        query = "INSERT INTO Players(Name, Age) VALUES ('%s', %d)" % (
            newPlayer["Name"], newPlayer["Age"])
        cur.execute(query)
        con.commit()
        print("Player added!")

    except Exception as e:
        con.rollback()
        print("Addition failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue> ")
    return


def addTeam(cur, con):
    try:
        teamName = input("Name: ")
        query = "INSERT INTO Teams(Name) VALUES ('%s')" % (teamName)
        cur.execute(query)
        con.commit()
        print("Team added!")
    except Exception as e:
        con.rollback()
        print("Addition failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue> ")
    return


def addMatch():
    pass


def addSeason(cur, con):
    try: 
        SeasonYear = int(input("Season Year: "))
        query = "INSERT INTO Seasons(Year) VALUES (%d)" % (SeasonYear)
        cur.execute(query)
        con.commit()
        print("Season Added!")
    except Exception as e:
        con.rollback()
        print("Addition failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue> ")
    pass


def addStadium():
    pass
