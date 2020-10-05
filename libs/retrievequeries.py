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
    try:
        query = "SELECT * FROM Seasons WHERE Finished=0"
        cur.execute(query)
        seasonList = cur.fetchall()
        if len(seasonList) == 0:
            print("No season ongoing!")
            tmp = input("Press any key to continue> ")
            return
        season = seasonList[0]["Year"]
        query = "SELECT PlayerID, Name, MatchesPlayed, MoM FROM Players"
        cur.execute(query)
        playerList = cur.fetchall()
        print("Player list: ")
        for i in range(len(playerList)):
            print(playerList[i])
        playerID = int(input("Enter ID of player: "))
        idx = -1
        for i in range(len(playerList)):
            if playerList[i]["PlayerID"] == playerID:
                idx = i
                break
        if idx == -1:
            print("Invalid player ID!")
            tmp = input("Print any key to continue> ")
            return
        query = "CREATE TEMPORARY TABLE IF NOT EXISTS temptable1 AS (SELECT MatchID FROM PlayerScorecard WHERE PlayerID=%d)" % (
            playerID)
        cur.execute(query)
        query = "CREATE TEMPORARY TABLE IF NOT EXISTS temptable2 AS (SELECT ID, Season FROM temptable1, Matches WHERE temptable1.MatchID=Matches.ID)"
        cur.execute(query)
        query = "SELECT * FROM temptable2 WHERE Season=%d" % (season)
        cur.execute(query)
        curMatchList = cur.fetchall()
        for i in curMatchList:
            print(i)
        curMatches = len(curMatchList)
        if curMatches == 0:
            print("Player hasn't played a match this season")
            tmp = input("Press any key to continue> ")
            return
        query = "SELECT * FROM Batsman WHERE PlayerID=%d" % (playerID)
        cur.execute(query)
        statList = cur.fetchall()
        if len(statList) != 0:
            print("Player %s is a batsman" % (playerList[idx]["Name"]))
            print("Matches Player: ", playerList[idx]["MatchesPlayed"])
            print("Man of the matches: ", playerList[idx]["MoM"])
            print("Total runs scored: ", statList[0]["CurrentRuns"])
            print("Batting average: ",
                  statList[0]["CurrentRuns"]/curMatches)
            tmp = input("Print any key to continue> ")
            return
        query = "SELECT * FROM Bowler WHERE PlayerID=%d" % (playerID)
        cur.execute(query)
        statList = cur.fetchall()
        if len(statList) != 0:
            print("Player %s is a bowler" % (playerList[idx]["Name"]))
            print("Matches Player: ", playerList[idx]["MatchesPlayed"])
            print("Man of the matches: ", playerList[idx]["MoM"])
            print("Total wickets taken: ", statList[0]["CurrentWickets"])
            print("Average wickets per match: ",
                  statList[0]["CurrentWickets"]/curMatches)
            tmp = input("Print any key to continue> ")
            return
        query = "SELECT * FROM AllRounder WHERE PlayerID=%d" % (playerID)
        cur.execute(query)
        statList = cur.fetchall()
        if len(statList) != 0:
            print("Player %s is an all-rounder" % (playerList[idx]["Name"]))
            print("Matches Player: ", playerList[idx]["MatchesPlayed"])
            print("Man of the matches: ", playerList[idx]["MoM"])
            print("Total runs scored: ", statList[0]["CurrentRuns"])
            print("Total wickets taken: ", statList[0]["CurrentWickets"])
            print("Average wickets per match: ",
                  statList[0]["CurrentRuns"]/curMatches)
            print("Average wickets per match: ",
                  statList[0]["CurrentWickets"]/curMatches)
            tmp = input("Print any key to continue> ")
            return
        print("Incomplete infomation about player :(")
        tmp = input("Print any key to continue> ")
    except Exception as e:
        print("Unable to retrieve :(")
        print("Error: ", e)
        tmp = input("Print any key to continue> ")


def reportAverageOverall(cur, con):
    try:
        query = "SELECT PlayerID, Name, MatchesPlayed, MoM FROM Players"
        cur.execute(query)
        playerList = cur.fetchall()
        print("Player list: ")
        for i in range(len(playerList)):
            print(playerList[i])
        playerID = int(input("Enter ID of player: "))
        idx = -1
        for i in range(len(playerList)):
            if playerList[i]["PlayerID"] == playerID:
                idx = i
                break
        if idx == -1:
            print("Invalid player ID!")
            tmp = input("Print any key to continue> ")
            return
        if playerList[idx]["MatchesPlayed"] == 0:
            print("Player hasn't played a match this season")
            tmp = input("Press any key to continue> ")
            return
        query = "SELECT * FROM Batsman WHERE PlayerID=%d" % (playerID)
        cur.execute(query)
        statList = cur.fetchall()
        if len(statList) != 0:
            print("Player %s is a batsman" % (playerList[idx]["Name"]))
            print("Matches Player: ", playerList[idx]["MatchesPlayed"])
            print("Man of the matches: ", playerList[idx]["MoM"])
            print("Total runs scored: ", statList[0]["TotalRuns"])
            print("Batting average: ",
                  statList[0]["TotalRuns"]/playerList[idx]["MatchesPlayed"])
            tmp = input("Print any key to continue> ")
            return
        query = "SELECT * FROM Bowler WHERE PlayerID=%d" % (playerID)
        cur.execute(query)
        statList = cur.fetchall()
        if len(statList) != 0:
            print("Player %s is a bowler" % (playerList[idx]["Name"]))
            print("Matches Player: ", playerList[idx]["MatchesPlayed"])
            print("Man of the matches: ", playerList[idx]["MoM"])
            print("Total wickets taken: ", statList[0]["TotalWickets"])
            print("Average wickets per match: ",
                  statList[0]["TotalWickets"]/playerList[idx]["MatchesPlayed"])
            tmp = input("Print any key to continue> ")
            return
        query = "SELECT * FROM AllRounder WHERE PlayerID=%d" % (playerID)
        cur.execute(query)
        statList = cur.fetchall()
        if len(statList) != 0:
            print("Player %s is an all-rounder" % (playerList[idx]["Name"]))
            print("Matches Player: ", playerList[idx]["MatchesPlayed"])
            print("Man of the matches: ", playerList[idx]["MoM"])
            print("Total runs scored: ", statList[0]["TotalRuns"])
            print("Total wickets taken: ", statList[0]["TotalWickets"])
            print("Average wickets per match: ",
                  statList[0]["TotalRuns"]/playerList[idx]["MatchesPlayed"])
            print("Average wickets per match: ",
                  statList[0]["TotalWickets"]/playerList[idx]["MatchesPlayed"])
            tmp = input("Print any key to continue> ")
            return
        print("Incomplete infomation about player :(")
        tmp = input("Print any key to continue> ")
    except Exception as e:
        print("Unable to retrieve :(")
        print("Error: ", e)
        tmp = input("Print any key to continue> ")


def reportMatchesPlayed(cur, con):
    pass
