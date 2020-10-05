#!/usr/bin/env python3

def topScorerCurrentSeason(cur, con):
    pass


def topScorerOverall(cur, con):
    pass


def positionInPrevious(cur, con):
    pass


def pointsInPrevious(cur, con):
    pass


def currentStandings(cur, con):
    pass


def reportAverageCurrent(cur, con):
    pass


def reportAverageOverall(cur, con):
    try:
        query = "SELECT * FROM Players"
        cur.execute(query)
        playerList = cur.fetchall()
        print("Player list: ")
        for i in range(len(playerList)):
            print(playerList[i])
        playerID = input("Enter ID of player> ")
        idx = -1
        for in range(len(playerList)):
            if playerList[i]["PlayerID"] == playerID:
                idx = i
                break
        if idx == -1:
            print("Invalid player ID!")
            tmp = input("Print any key to continue> ")
            return

    except Exception as e:
        print("Unable to retrieve :(")
        tmp = input("Print any key to continue> ")


def reportMatchesPlayed(cur, con):
    pass
