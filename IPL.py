#!/usr/bin/env python3

import subprocess as sp
import pymysql as sql
import pymysql.cursors as sqlcursor

from libs.addqueries import addPlayer, addTeam, addSeason, addMatch, addTeammanagement
from libs.removequeries import removePlayer, removeTeam, removeSeason, removeMatch, removeStadium
from libs.updatequeries import updatePlayer, updateTeam, updateSeason, updateMatch, updateStadium
from libs.viewall import viewPlayers, viewMatches, viewTeams, viewStadiums, viewSeasons


def addMenu(cur, con):
    while True:
        tmp = sp.call("clear", shell=True)
        print("1. Add player")
        print("2. Add team")
        print("3. Add match")
        print("4. Add season")
        print("5. Add stadium")
        print("6. Add Team Management")
        print("7. Exit")
        choice = int(input("Enter choice> "))
        if choice == 1:
            addPlayer(cur, con)
        elif choice == 2:
            addTeam(cur, con)
        elif choice == 3:
            addMatch(cur, con)
        elif choice == 4:
            addSeason(cur, con)
        elif choice == 5:
            addStadium(cur, con)
        elif choice == 6:
            addTeammanagement(cur, con)
        elif choice == 7:
            return
        else:
            print("Invalid choice")


def deleteMenu(cur, con):
    while True:
        tmp = sp.call("clear", shell=True)
        print("1. Delete player")
        print("2. Delete team")
        print("3. Exit")
        choice = int(input("Enter choice> "))
        if choice == 1:
            removePlayer(cur, con)
        elif choice == 2:
            removeTeam(cur, con)
        elif choice == 3:
            return
        else:
            print("Invalid choice")


def updateMenu(cur, con):
    while True:
        tmp = sp.call("clear", shell=True)
        print("1. Update player")
        print("2. Update Team")
        print("3. Update Stadium")
        print("4. Update Season")
        print("5. Exit")
        choice = int(input("Enter choice> "))
        if choice == 1:
            updatePlayer(cur, con)
        elif choice == 2:
            updateTeam(cur, con)
        elif choice == 3:
            updateStadium(cur, con)
        elif choice == 4:
            updateSeason(cur, con)
        elif choice == 5:
            return
        else:
            print("Invalid choice")


def viewMenu(cur, con):
    while True:
        tmp = sp.call("clear", shell=True)
        print("1. View all players")
        print("2. View all teams")
        print("3. View all seasons")
        print("4. View all matches")
        print("5. View all stadiums")
        print("6. Exit")
        choice = int(input("Enter choice> "))
        if choice == 1:
            viewPlayers(cur, con)
        elif choice == 2:
            viewTeams(cur, con)
        elif choice == 3:
            viewSeasons(cur, con)
        elif choice == 4:
            viewMatches(cur, con)
        elif choice == 5:
            viewStadiums(cur, con)
        elif choice == 6:
            return
        else:
            print("Invalid choice")


def main():
    while(1):
        tmp = sp.call("clear", shell=True)

        username = input("Username: ")
        password = input("Password: ")

        try:
            con = sql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='IPL',
                              cursorclass=sqlcursor.DictCursor)
            tmp = sp.call("clear", shell=True)

            if(con.open):
                print("Connected")
            else:
                print("Connection failed")

            tmp = input("Enter any key to continue>")

            with con.cursor() as cur:
                while(1):
                    tmp = sp.call("clear", shell=True)
                    print("1. To go to add menu")
                    print("2. To go to delete menu")
                    print("3. To go to update menu")
                    print("4. To go to view menu")
                    choice = int(input("Enter choice> "))
                    if choice == 1:
                        addMenu(cur, con)
                    elif choice == 2:
                        deleteMenu(cur, con)
                    elif choice == 3:
                        updateMenu(cur, con)
                    elif choice == 4:
                        viewMenu(cur, con)
                    else:
                        print("Invalid choice")

        except Exception as e:
            tmp = sp.call("clear", shell=True)
            print("Connection failed!")
            print("Error: ", e)
            tmp = input("Enter any key to continue> ")


if __name__ == '__main__':
    main()
