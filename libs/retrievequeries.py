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
            query = "SELECT * FROM Players NATURAL JOIN Batsman WHERE TotalRuns = %d" % (maxbatsmanruns)
            cur.execute(query)
            data = cur.fetchall()
            print("Maximum Runs")
            print(data[0])
        else:
            query = "SELECT * FROM Players NATURAL JOIN AllRounder WHERE TotalRuns = %d" % (maxallrounderruns)
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
            query = "SELECT * FROM Players NATURAL JOIN Bowler WHERE TotalWickets = %d" % (maxbowlerwickets)
            cur.execute(query)
            data = cur.fetchall()
            print("Maximum Wickets")
            print(data[0])
        else:
            query = "SELECT * FROM Players NATURAL JOIN AllRounder WHERE TotalWickets = %d" % (maxallrounderwickets)
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
    pass


def pointsInPrevious(cur, con):
    pass


def currentStandings(cur, con):
    pass


def reportAverageCurrent(cur, con):
    pass


def reportAverageOverall(cur, con):
    # try:
    #     query = "SELECT * FROM Players"
    #     cur.execute(query)
    #     playerList = cur.fetchall()
    #     print("Player list: ")
    #     for i in range(len(playerList)):
    #         print(playerList[i])
    #     playerID = input("Enter ID of player> ")
    #     idx = -1
    #     for in range(len(playerList)):
    #         if playerList[i]["PlayerID"] == playerID:
    #             idx = i
    #             break
    #     if idx == -1:
    #         print("Invalid player ID!")
    #         tmp = input("Print any key to continue> ")
    #         return

    # except Exception as e:
    #     print("Unable to retrieve :(")
    #     tmp = input("Print any key to continue> ")
    pass


def reportMatchesPlayed(cur, con):
    pass
