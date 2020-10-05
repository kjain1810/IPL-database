#!/usr/bin/env python3

def topScorerCurrentSeason(cur, con):
    try:
        query = "SELECT OrangeCap, PurpleCap FROM Seasons where (Finished = 0)"
        cur.execute(query)
        data = cur.fetchall()
        maxrunsID = data[0]["OrangeCap"]
        maxwicketsID = data[0]["PurpleCap"]
        print("Maxruns scorer:")
        query = "SELECT * FROM Players where (PlayerID = %d)" % (maxrunsID)
        cur.execute(query)
        data = cur.fetchall()
        print(data[0])
        print("Maxwickets taker:")
        query = "SELECT * FROM Players where (PlayerID = %d)" % (maxwicketsID)
        cur.execute(query)
        data = cur.fetchall()
        print(data[0])

    except Exception as e:
        print("Couldn't fetch list :(")
        print("Error: ", e)
    tmp = input("Press any key to continue> ")
    return


def topScorerOverall(cur, con):
    try:
        query = "SELECT MAX(TotalRuns) AS Maxruns FROM Batsman"
        cur.execute(query)
        res = cur.fetchall()
        maxbatsmanruns = res[0]["Maxruns"]
        query = "SELECT MAX(TotalRuns) AS Maxruns FROM AllRounder"
        cur.execute(query)
        res = cur.fetchall()
        maxallrounderruns = res[0]["Maxruns"]
        if(maxbatsmanruns > maxallrounderruns):
            query = "SELECT * FROM Players NATURAL JOIN Batsman WHERE TotalRuns = %d" % (
                maxbatsmanruns)
            cur.execute(query)
            data = cur.fetchall()
            print("Maximum Runs")
            print(data[0])
        else:
            query = "SELECT * FROM Players NATURAL JOIN AllRounder WHERE TotalRuns = %d" % (
                maxallrounderruns)
            cur.execute(query)
            data = cur.fetchall()
            print("Maximum Runs")
            print(data[0])
        query = "SELECT MAX(TotalWickets) AS Maxwickets FROM Bowler"
        cur.execute(query)
        res = cur.fetchall()
        maxbowlerwickets = res[0]["Maxwickets"]
        query = "SELECT MAX(TotalWickets) AS Maxwickets FROM AllRounder"
        cur.execute(query)
        res = cur.fetchall()
        maxallrounderwickets = res[0]["Maxwickets"]
        if(maxallrounderwickets < maxbowlerwickets):
            query = "SELECT * FROM Players NATURAL JOIN Bowler WHERE TotalWickets = %d" % (
                maxbowlerwickets)
            cur.execute(query)
            data = cur.fetchall()
            print("Maximum Wickets")
            print(data[0])
        else:
            query = "SELECT * FROM Players NATURAL JOIN AllRounder WHERE TotalWickets = %d" % (
                maxallrounderwickets)
            cur.execute(query)
            data = cur.fetchall()
            print("Maximum Wickets")
            print(data[0])
    except Exception as e:
        print("Couldn't fetch list :(")
        print("Error: ", e)
    tmp = input("Press any key to continue> ")
    return


def positionInPrevious(cur, con):
    try:
        teamID = int(input("Enter team ID: "))
        season = int(input("Enter season year: "))
        query = "SELECT * FROM TeamStandings WHERE TeamID=%d AND SeasonYear=%d" % (
            teamID, season)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("Team %d didn't participate in year %d" % (teamID, season))
        else:
            print("Team %d was at position %d in year %d" %
                  (teamID, res[0]["Standing"], season))
        tmp = input("Press any key to continue> ")
    except Exception as e:
        print("Couldn't retrieve :(")
        print("Error: ", e)
        tmp = input("Press any key to continue> ")


def pointsInPrevious(cur, con):
    pass


def currentStandings(cur, con):
    try:
        query = "SELECT * FROM Seasons WHERE Finished=0"
        cur.execute(query)
        seasonList = cur.fetchall()
        if len(seasonList) == 0:
            print("No season ongoing!")
            tmp = input("Press any key to continue> ")
            return
        season = seasonList[0]["Year"]
        query = "SELECT * FROM TeamResults WHERE SeasonYear=%d" % (season)
        cur.execute(query)
        teamResults = cur.fetchall()
        sortedTeamResults = sorted(teamResults, key=lambda i: i["Points"])
        for i in range(len(sortedTeamResults)):
            query = "SELECT Name FROM Teams WHERE TeamID=%d" % (
                sortedTeamResults[i]["TeamID"])
            cur.execute(query)
            teamNameList = cur.fetchall()
            teamName = teamNameList[0]["Name"]
            print("Position %d: %s(Team ID: %d) with %d points" % (
                len(sortedTeamResults) - i, teamName, sortedTeamResults[i]["TeamID"], sortedTeamResults[i]["Points"]))
        tmp = input("Press any key to continue> ")
    except Exception as e:
        print("Couldn't get standings :(")
        print("Error: ", e)
        tmp = input("Press any key to continue> ")


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
