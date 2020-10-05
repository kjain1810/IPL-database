#!/usr/bin/env python3

def searchPlayer(cur, con):
    try:
        toSearch = input("Enter name: ")
        query = "SELECT * FROM Players WHERE Name='%s'" % (toSearch)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("No player with such name :(")
        else:
            print("Here is a list of players with this name: ")
            for i in range(len(res)):
                print(res[i])
        tmp = input("Press any key to continue> ")
    except Exception as e:
        print("Couldn't search :(")
        print("Error: ", e)
        tmp = input("Press any key to continue> ")


def searchTeam(cur, con):
    try:
        toSearch = input("Enter name: ")
        query = "SELECT * FROM Teams WHERE Name='%s'" % (toSearch)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("No team with such name :(")
        else:
            print("Here is a list of teams with this name: ")
            for i in range(len(res)):
                print(res[i])
        tmp = input("Press any key to continue> ")
    except Exception as e:
        print("Couldn't search :(")
        print("Error: ", e)
        tmp = input("Press any key to continue> ")


def searchStadium(cur, con):
    try:
        toSearch = input("Enter name: ")
        query = "SELECT * FROM Stadium WHERE Stadium_Name='%s'" % (toSearch)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("No stadium with such name :(")
        else:
            print("Here is a list of stadiums with this name: ")
            for i in range(len(res)):
                print(res[i])
        tmp = input("Press any key to continue> ")
    except Exception as e:
        print("Couldn't search :(")
        print("Error: ", e)
        tmp = input("Press any key to continue> ")
