#!/usr/bin/env python3

import subprocess as sp
import pymysql as sql
import pymysql.cursors as sqlcursor

from libs.addqueries import addPlayer, addTeam, addSeason, addMatch, addTeammanagement, addStadium
from libs.removequeries import removePlayer, removeTeam, removeSeason, removeMatch, removeStadium
from libs.updatequeries import updatePlayer, updateTeam, updateSeason, updateMatch, updateStadium
from libs.viewall import viewPlayers, viewMatches, viewTeams, viewStadiums, viewSeasons, viewPlayersAndTeamManagement
from libs.markFinished import markFinished
from libs.retrievequeries import *
from libs.searchname import searchPlayer, searchStadium, searchTeam


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
        print("6. View players and team management of a team")
        print("7. Exit")
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
            viewPlayersAndTeamManagement(cur, con)
        elif choice == 7:
            return
        else:
            print("Invalid choice")


def statsMenu(cur, con):
    while True:
        tmp = sp.call("clear", shell=True)
        print("1. Retrieve topscorers of current season")
        print("2. Retrieve overall top scorers")
        print("3. Retrieve positions of a team in previous seasons")
        print("4. Retrieve points of a team in previous seasons")
        print("5. Retrieve current season standings")
        print("6. Retrieve average scores of a player")
        print("7. Retrieve average scores of a player in current season")
        print("8. Retrieve matches played in a stadium")
        print("9. Exit")
        choice = int(input("Enter choice> "))
        if choice == 1:
            topScorerCurrentSeason(cur, con)
        elif choice == 2:
            topScorerOverall(cur, con)
        elif choice == 3:
            positionInPrevious(cur, con)
        elif choice == 4:
            pointsInPrevious(cur, con)
        elif choice == 5:
            currentStandings(cur, con)
        elif choice == 6:
            reportAverageOverall(cur, con)
        elif choice == 7:
            reportAverageCurrent(cur, con)
        elif choice == 8:
            reportMatchesPlayed(cur, con)
        elif choice == 9:
            return
        else:
            print("Invalid choice")


def searchMenu(cur, con):
    while True:
        tmp = sp.call("clear", shell=True)
        print("1. Seach for player")
        print("2. Search for team")
        print("3. Search for stadium")
        print("4. Exit")
        choice = int(input("Enter choice> "))
        if choice == 1:
            searchPlayer(cur, con)
        elif choice == 2:
            searchTeam(cur, con)
        elif choice == 3:
            searchStadium(cur, con)
        elif choice == 4:
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
                    print("5. To mark currently running season as finished")
                    print("6. Retrieve statistic")
                    print("7. Search by name")
                    print("8. Exit")
                    choice = int(input("Enter choice> "))
                    if choice == 1:
                        addMenu(cur, con)
                    elif choice == 2:
                        deleteMenu(cur, con)
                    elif choice == 3:
                        updateMenu(cur, con)
                    elif choice == 4:
                        viewMenu(cur, con)
                    elif choice == 5:
                        markFinished(cur, con)
                    elif choice == 6:
                        statsMenu(cur, con)
                    elif choice == 7:
                        searchMenu(cur, con)
                    elif choice == 8:
                        return
                    else:
                        print("Invalid choice")

        except Exception as e:
            tmp = sp.call("clear", shell=True)
            print("Connection failed!")
            print("Error: ", e)
            tmp = input("Enter any key to continue> ")


if __name__ == '__main__':
    main()
