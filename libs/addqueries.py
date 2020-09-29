#!/usr/bin/env python3

def addPlayer(cur, con):
    try:
        newPlayer = {}
        newPlayer["Name"] = input("Name: ")
        newPlayer["Age"] = int(input("Age: "))
        query = "INSERT INTO Players(Name, Age) VALUES ('%s', %s)" % (
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


def addStadium():
    pass


if __name__ == '__main__':
    addPlayer()
