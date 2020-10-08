#!/usr/bin/env python3

from tabulate import tabulate

def searchPlayer(cur, con):
    try:
        toSearch = input("Enter name: ")
        query = "SELECT * FROM Players WHERE Name LIKE '%%%s%%'" % (toSearch)
        # print(query)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("No player with such name :(")
        else:
            headers = res[0].keys()
            res = [x.values() for x in res]
            print(tabulate(res, headers, tablefmt="pretty"))
            # print("Here is a list of players with this name: ")
            # for i in range(len(res)):
            #     print(res[i])
        tmp = input("Press any key to continue> ")
    except Exception as e:
        print("Couldn't search :(")
        print("Error: ", e)
        tmp = input("Press any key to continue> ")


def searchTeam(cur, con):
    try:
        toSearch = input("Enter name: ")
        query = "SELECT * FROM Teams WHERE Name LIKE '%%%s%%'" % (toSearch)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("No team with such name :(")
        else:
            headers = res[0].keys()
            res = [x.values() for x in res]
            print(tabulate(res, headers, tablefmt="pretty"))
            # print("Here is a list of teams with this name: ")
            # for i in range(len(res)):
            #     print(res[i])
        tmp = input("Press any key to continue> ")
    except Exception as e:
        print("Couldn't search :(")
        print("Error: ", e)
        tmp = input("Press any key to continue> ")


def searchStadium(cur, con):
    try:
        toSearch = input("Enter name: ")
        query = "SELECT * FROM Stadium WHERE Stadium_Name LIKE '%%%s%%'" % (toSearch)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("No stadium with such name :(")
        else:
            headers = res[0].keys()
            res = [x.values() for x in res]
            print(tabulate(res, headers, tablefmt="pretty"))
            # print("Here is a list of stadiums with this name: ")
            # for i in range(len(res)):
            #     print(res[i])
        tmp = input("Press any key to continue> ")
    except Exception as e:
        print("Couldn't search :(")
        print("Error: ", e)
        tmp = input("Press any key to continue> ")
