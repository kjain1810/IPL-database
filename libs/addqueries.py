#!/usr/bin/env python3

from tabulate import tabulate

def addPlayer(cur, con):
    try:
        query = "SELECT * FROM Teams"
        cur.execute(query)
        rows = cur.fetchall()
        headers = rows[0].keys()
        rows = [x.values() for x in rows]
        print(tabulate(rows, headers, tablefmt="pretty"))
        newPlayer = {}
        newPlayer["Name"] = input("Player Name: ")
        newPlayer["Age"] = int(input("PlayerAge: "))
        newPlayer["TeamID"] = int(input("TeamID(Select from above table): "))
        newPlayer["Role"] = input("Role(Batsman, Bowler, AllRounder): ")
        query = "INSERT INTO Players(Name, Age, TeamID) VALUES ('%s', %d, %d)" % (
            newPlayer["Name"], newPlayer["Age"], newPlayer["TeamID"])
        cur.execute(query)
        query = "SELECT last_insert_id()"
        cur.execute(query)
        rows = cur.fetchall()
        query = "INSERT INTO %s(PlayerID) VALUES (%d)" % (
            newPlayer["Role"], rows[0]["last_insert_id()"])
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
    """
    tables updating:
        1. Batsman/Bowler/All Rounder as appropriate
        2. Orange cap/purple cap of season
        3. Matches
        4. Scorecard
        5. PlayerScorecard
        6. Plays
        7. TeamStandings
    """
    try:
        # input teams and check existence
        query = "SELECT * FROM Teams"
        cur.execute(query)
        rows = cur.fetchall()
        headers = rows[0].keys()
        rows = [x.values() for x in rows]
        print(tabulate(rows, headers, tablefmt="pretty"))
        teamID1 = int(input("Enter ID of first team(use above table): "))
        teamID2 = int(input("Enter ID of second team(use above table): "))
        query = "SELECT * FROM Teams WHERE TeamID in (%d, %d)" % (
            teamID1, teamID2)
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows) != 2:
            print("Invalid teams!")
            tmp = input("Enter any key to continue> ")
            return

        # input season and check existence
        season = int(input("Enter season year: "))
        query = "SELECT * FROM Seasons WHERE Year = %d" % (season)
        cur.execute(query)
        sList = cur.fetchall()
        if len(sList) != 1:
            print("No such season")
            tmp = input("Enter any key to continue> ")
            return
        if sList[0]["Finished"]:
            print("Season finished")
            tmp = input("Enter any key to continue> ")
            return
        # fetch current runs of orangecap and purple cap
        orangeCapPlayerID = sList[0]["OrangeCap"]
        purpleCapPlayerID = sList[0]["PurpleCap"]
        orangeCapRuns = -1
        purpleCapWickets = -1
        if orangeCapPlayerID != None:
            query = "SELECT CurrentRuns FROM Batsman WHERE PlayerID=%d" % (
                orangeCapPlayerID)
            cur.execute(query)
            tmp = cur.fetchall()
            if len(tmp) == 0:
                query = "SELECT CurrentRuns FROM AllRounder WHERE PlayerID=%d" % (
                    orangeCapPlayerID)
                cur.execute(query)
                tmp = cur.fetchall()
            orangeCapRuns = tmp[0]["CurrentRuns"]
        if purpleCapPlayerID != None:
            query = "SELECT CurrentWickets FROM Bowler WHERE PlayerID=%d" % (
                purpleCapPlayerID)
            cur.execute(query)
            tmp = cur.fetchall()
            if len(tmp) == 0:
                query = "SELECT CurrentWickets FROM AllRounder WHERE PlayerID=%d" % (
                    purpleCapPlayerID)
                cur.execute(query)
                tmp = cur.fetchall()
            purpleCapWickets = tmp[0]["CurrentWickets"]
        # check number of players for both teams
        # input performance of every player
        playerScorecard = []
        totalScores = {}
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
            thisTeam = 0
            headers = teamPlayers[0].keys()
            teamPlayers = [x.values() for x in teamPlayers]
            print(tabulate(teamPlayers, headers, tablefmt="pretty"))
            for j in range(len(teamPlayers)):
                # print(teamPlayers[j]["Name"] + "(ID %d)" %
                #       (teamPlayers[j]["PlayerID"]))
                runs = int(input("Runs: "))
                wickets = int(input("Wickets: "))
                playerScorecard.append(
                    {"PlayerID": teamPlayers[j]["PlayerID"], "Runs": runs, "Wickets": wickets})
                thisTeam += runs
            totalScores[rows[i]["TeamID"]] = thisTeam

        # determining the winner
        winner = -1
        if totalScores[teamID1] > totalScores[teamID2]:
            winner = teamID1
        elif totalScores[teamID1] < totalScores[teamID2]:
            winner = teamID2
        if winner == -1:
            print("Match can't tie!")
            tmp = input("Enter any key to continue> ")
            return

        # input umpires
        umpireOne = input("Enter field umpire 1' name: ")
        umpireTwo = input("Enter field umpire 2' name: ")

        # input stadium and check
        query = "SELECT Stadium_Name, Stadium_City, Home_Team FROM Stadium where (Home_Team = %d or Home_Team = %d)" % (
            teamID1, teamID2)
        cur.execute(query)
        rows1 = cur.fetchall()
        print("Home Stadiums of teams")
        headers = rows1[0].keys()
        rows1 = [x.values() for x in rows1]
        print(tabulate(rows1, headers, tablefmt="pretty"))
        # for i in rows1:
        #     print(i)
        stadiumName = input("Enter stadium name: ")
        stadiumCity = input("Enter stadium city: ")

        # UPDATING EACH PLAYER'S RECORD OF BATSMAN/BOWLER/ALLROUNDER
        # taking prevoius records of the players involved in the match
        roles = ["Batsman", "Bowler", "AllRounder"]
        previousinfo = {}
        for i in roles:
            query = "SELECT * FROM Players natural join %s where (TeamID = %d or TeamID = %d)" % (
                i, teamID1, teamID2)
            cur.execute(query)
            templist = cur.fetchall()
            for j in templist:
                previousinfo[j["PlayerID"]] = j
        # Making the changes of the score card to the record of players
        for i in playerScorecard:
            runs = 0
            wickets = 0
            if("CurrentRuns" in previousinfo[i["PlayerID"]].keys()) and ("CurrentWickets" in previousinfo[i["PlayerID"]].keys()):
                runs = i["Runs"] + previousinfo[i["PlayerID"]]["CurrentRuns"]
                totalruns = i["Runs"] + \
                    previousinfo[i["PlayerID"]]["TotalRuns"]
                wickets = i["Wickets"] + \
                    previousinfo[i["PlayerID"]]["CurrentWickets"]
                totalwickets = i["Wickets"] + \
                    previousinfo[i["PlayerID"]]["TotalWickets"]
                query = "UPDATE AllRounder SET CurrentRuns = %d, TotalRuns = %d, CurrentWickets = %d, TotalWickets = %d WHERE PlayerID = %d" % (
                    runs, totalruns, wickets, totalwickets, i["PlayerID"])
            elif ("CurrentRuns" in previousinfo[i["PlayerID"]].keys()):
                runs = i["Runs"] + previousinfo[i["PlayerID"]]["CurrentRuns"]
                totalruns = i["Runs"] + \
                    previousinfo[i["PlayerID"]]["TotalRuns"]
                query = "UPDATE Batsman SET CurrentRuns = %d, TotalRuns = %d WHERE PlayerID = %d" % (
                    runs, totalruns, i["PlayerID"])
            elif ("CurrentWickets" in previousinfo[i["PlayerID"]].keys()):
                wickets = i["Wickets"] + \
                    previousinfo[i["PlayerID"]]["CurrentWickets"]
                totalwickets = i["Wickets"] + \
                    previousinfo[i["PlayerID"]]["TotalWickets"]
                query = "UPDATE Bowler SET CurrentWickets = %d, TotalWickets = %d WHERE PlayerID = %d" % (
                    wickets, totalwickets, i["PlayerID"])
            cur.execute(query)

            # check for updates in season orange and purple caps
            if orangeCapRuns < runs:
                query = "UPDATE Seasons SET OrangeCap=%d WHERE Year=%d" % (
                    i["PlayerID"], season)
                orangeCapRuns = runs
                cur.execute(query)
            if purpleCapWickets < wickets:
                query = "UPDATE Seasons SET PurpleCap=%d WHERE Year=%d" % (
                    i["PlayerID"], season)
                purpleCapWickets = wickets
                cur.execute(query)
            query = "SELECT * FROM Players WHERE PlayerID = %d" % (
                i["PlayerID"])
            cur.execute(query)
            playerdata = cur.fetchall()
            totalmathches = playerdata[0]["MatchesPlayed"] + 1
            query = "UPDATE Players set MatchesPlayed = %d where PlayerID = %d" % (
                totalmathches, i["PlayerID"])
            cur.execute(query)

        # input MoM and check correctness of it

        headers = playerScorecard[0].keys()
        playerScorecard = [x.values() for x in playerScorecard]
        print(tabulate(playerScorecard, headers, tablefmt="pretty"))
        # for i in playerScorecard:
        #     print(i)
        MoM = int(input("Enter man of the match from the performances: "))
        query = "SELECT * FROM Players WHERE PlayerID = %d" % (MoM)
        cur.execute(query)
        MoMList = cur.fetchall()
        if MoMList[0]["TeamID"] != teamID1 and MoMList[0]["TeamID"] != teamID2:
            print("Player was not part of the match!")
            tmp = input("Enter any key to continue> ")
            return
        update_no_of_mom = MoMList[0]["MoM"] + 1
        query = "UPDATE Players set MoM=%d where PlayerID=%d" % (
            update_no_of_mom, MoM)
        cur.execute(query)
        # insert Matches and get matchid
        query = "INSERT INTO Matches(Season, WinnerID, Stadium_name, Stadium_city, Mom, Feild_Umpire1, Feild_Umpire2) VALUES (%d, %d, '%s', '%s', %d, '%s', '%s')" % (
            season, winner, stadiumName, stadiumCity, MoM, umpireOne, umpireTwo)
        cur.execute(query)
        query = "SELECT last_insert_id()"
        cur.execute(query)
        tmp = cur.fetchall()
        matchID = tmp[0]["last_insert_id()"]

        # update Scorecard
        query = "INSERT INTO Scorecard(MatchID, Team1, Team2) VALUES (%d, %d, %d)" % (
            matchID, teamID1, teamID2)
        cur.execute(query)

        # update PlayerScorecard
        for i in playerScorecard:
            query = "INSERT INTO PlayerScorecard(MatchID, PlayerID, Wickets, Runs) VALUES (%d, %d, %d, %d)" % (
                matchID, i["PlayerID"], i["Wickets"], i["Runs"])
            cur.execute(query)

        # update Plays
        query = "INSERT INTO Plays(Match_ID, Team_ID, Season_Year, Stadium_name, Stadium_city) VALUES (%d, %d, %d, '%s', '%s')" % (
            matchID, teamID1, season, stadiumName, stadiumCity)
        cur.execute(query)
        query = "INSERT INTO Plays(Match_ID, Team_ID, Season_Year, Stadium_name, Stadium_city) VALUES (%d, %d, %d, '%s', '%s')" % (
            matchID, teamID2, season, stadiumName, stadiumCity)
        cur.execute(query)

        # update TeamStandings
        query = "SELECT * FROM TeamResults WHERE TeamID=%d AND SeasonYear=%d" % (
            teamID1, season)
        cur.execute()
        resList = cur.fetchall()
        if len(resList) == 0:
            query = "INSERT INTO TeamResults(TeamID, SeasonYear, Points) VALUES (%d, %d, 0)" % (
                teamID1, season)
            cur.execute(query)
        query = "SELECT * FROM TeamResults WHERE TeamID=%d AND SeasonYear=%d" % (
            teamID2, season)
        cur.execute()
        resList = cur.fetchall()
        if len(resList) == 0:
            query = "INSERT INTO TeamResults(TeamID, SeasonYear, Points) VALUES (%d, %d, 0)" % (
                teamID2, season)
            cur.execute(query)
        query = "SELECT * FROM TeamResults WHERE TeamID=%d AND SeasonYear=%d" % (
            winner, season)
        cur.execute(query)
        tmp = cur.fetchall()
        newpoints = tmp[0]["Points"] + 2
        query = "UPDATE TeamResults SET Points=%d WHERE (TeamID=%d AND SeasonYear=%d)" % (
            newpoints, winner, season)
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
        query = "SELECT Year FROM Seasons WHERE Finished=0"
        cur.execute(query)
        checkRunning = cur.fetchall()
        if len(checkRunning) != 0:
            print("Oops, seems like year %d is running right now!" %
                  (checkRunning[0]["Year"]))
            tmp = input("Enter any key to continue> ")
            return
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
    return


def addStadium(cur, con):
    try:
        stadiumName = input("Enter name: ")
        stadiumCity = input("Enter city: ")
        maxCap = int(input("Enter max capacity: "))
        query = "SELECT * FROM Teams"
        cur.execute(query)
        rows = cur.fetchall()
        headers = rows[0].keys()
        rows = [x.values() for x in rows]
        print(tabulate(rows, headers, tablefmt="pretty"))
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


def addTeammanagement(cur, con):
    try:
        query = "SELECT * FROM Teams"
        cur.execute(query)
        rows = cur.fetchall()
        headers = rows[0].keys()
        rows = [x.values() for x in rows]
        print(tabulate(rows, headers, tablefmt="pretty"))
        # for i in rows:
        #     print(i)
        teamID = int(
            input("Enter the TeamID for which you want to add the management: "))
        name = input("Enter the name of the management: ")
        role = input(
            "Enter the role that you want to assign to the management: ")
        query = "INSERT INTO TeamManagement(TeamID, Name, Role) VALUES (%d, '%s', '%s')" % (
            teamID, name, role)
        cur.execute(query)
        con.commit()
        print("Team Mangement added!")
    except Exception as e:
        con.rollback()
        print("Addition Failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue")
    return
