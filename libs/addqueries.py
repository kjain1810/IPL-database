#!/usr/bin/env python3

def addPlayer(cur, con):
    try:
        newPlayer = {}
        newPlayer["Name"] = input("Name: ")
        newPlayer["Age"] = int(input("Age: "))
        newPlayer["TeamID"] = int(input("TeamID: "))
        newPlayer["Role"] = input("Role(Batsman, Bowler, AllRounder): ")
        query = "INSERT INTO Players(Name, Age, TeamID) VALUES ('%s', %d, %d)" % (
            newPlayer["Name"], newPlayer["Age"], newPlayer["TeamID"])
        cur.execute(query)
        query = "SELECT last_insert_id()"
        cur.execute(query)
        rows = cur.fetchall()
        query = "INSERT INTO %s(PlayerID) VALUES (%d)" % (newPlayer["Role"], rows[0]["last_insert_id()"])
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


def addMatch(cur, con):
    try:
        teamID1 = int(input("Enter ID of first team: "))
        teamID2 = int(input("Enter ID of second team: "))
        query = "SELECT * FROM Teams WHERE TeamID in (%d, %d)" % (
            teamID1, teamID2)
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows) != 2:
            print("Invalid teams!")
            tmp = input("Enter any key to continue> ")
            return
        playerScorecard = []
        for i in range(len(rows)):
            query = "SELECT * FROM Players WHERE TeamID=%d" % (
                rows[i]["TeamID"])
            cur.execute(query)
            teamPlayers = cur.fetchall()
            if len(teamPlayers) != 11:
                print("Team %s does not have exactly 11 players!" %
                      (rows[i]["Name"]))
                tmp = input("Enter any key to continue> ")
                return
            print("Enter player performances of team %s" % (rows[i]["Name"]))
            for j in range(len(teamPlayers)):
                print(teamPlayers[j]["Name"] + "(ID %d)" %
                      (teamPlayers[j]["PlayerID"]))
                runs = int(input("Runs: "))
                wickets = int(input("Wickets: "))
                playerScorecard.append(
                    {"PlayerID": teamPlayers[j]["PlayerID"], "Runs": runs, "Wickets": wickets})
        roles = ["Batsman", "Bowler", "AllRounder"]
        previousinfo = {}
        for i in roles:
            query = "SELECT * FROM Players natural join %s where (TeamID = %d or TeamID = %d)" % (i,teamID1, teamID2)
            cur.execute(query)
            templist = cur.fetchall()
            for j in templist:
                previousinfo[j["PlayerID"]] = j
        for i in playerScorecard:
            if("CurrentRuns" in previousinfo[i["PlayerID"]].keys()) and ("CurrentWickets" in previousinfo[i["PlayerID"]].keys()):
                runs = i["Runs"] + previousinfo[i["PlayerID"]]["CurrentRuns"]
                totalruns = i["Runs"] + previousinfo[i["PlayerID"]]["TotalRuns"]
                wickets = i["Wickets"] + previousinfo[i["PlayerID"]]["CurrentWickets"]
                totalwickets = i["Wickets"] + previousinfo[i["PlayerID"]]["TotalWickets"]
                query = "UPDATE AllRounder SET CurrentRuns = %d, TotalRuns = %d, CurrentWickets = %d, TotalWickets = %d WHERE PlayerID = %d" % (runs, totalruns, wickets, totalwickets, i["PlayerID"])
            elif ("CurrentRuns" in previousinfo[i["PlayerID"]].keys()):
                runs = i["Runs"] + previousinfo[i["PlayerID"]]["CurrentRuns"]
                totalruns = i["Runs"] + previousinfo[i["PlayerID"]]["TotalRuns"]
                query = "UPDATE Batsman SET CurrentRuns = %d, TotalRuns = %d WHERE PlayerID = %d" % (runs, totalruns, i["PlayerID"])
            elif ("CurrentWickets" in previousinfo[i["PlayerID"]].keys()):
                wickets = i["Wickets"] + previousinfo[i["PlayerID"]]["CurrentWickets"]
                totalwickets = i["Wickets"] + previousinfo[i["PlayerID"]]["TotalWickets"]
                query = "UPDATE Bowler SET CurrentWickets = %d, TotalWickets = %d WHERE PlayerID = %d" % (wickets, totalwickets, i["PlayerID"])
            cur.execute(query)
            con.commit()
    except Exception as e:
        con.rollback()
        print("Addition failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue> ")
    return


def addSeason(cur, con):
    try:
        SeasonYear = int(input("Season Year: "))
        query = "INSERT INTO Seasons(Year) VALUES (%d)" % (SeasonYear)
        cur.execute(query)
        con.commit()
        print("Season Added!")
    except Exception as e:
        con.rollback()
        print("Addition failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue> ")
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
