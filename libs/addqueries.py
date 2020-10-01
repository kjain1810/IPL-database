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


def addSeason():
    pass


def addStadium(cur, con):
    try:
        stadiumName = input("Enter name: ")
        stadiumCity = input("Enter city: ")
        maxCap = int(input("Enter max capacity: "))
        homeTeamID = int(input("Enter home team ID: "))
        query = "INSERT INTO Stadium(Stadium_Name, Stadium_City, Max_capacity, Home_Team) VALUES ('%s', '%s', %d, %d)" % (
            stadiumName, stadiumCity, maxCap, homeTeamID)
        cur.execute(query)
        con.commit()
        print("Stadium added!")
    except Exception as e:
        con.rollback()
        print("Addition failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue")
    return
