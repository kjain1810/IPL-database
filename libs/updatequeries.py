#!/usr/bin/env python3

def updatePlayer(cur, con):
    try:
        query = "SELECT * FROM Players;"
        cur.execute(query)
        rows = cur.fetchall()
        for i in range(len(rows)):
            print(rows[i])
        playerid = int(
            input("Select PlayerID of Player whose data you wish to change: "))
        new_name = input("New Name: ")
        new_age = int(input("New Age: "))
        new_teamId = int(input("New TeamID: "))
        query = "SELECT * FROM Players WHERE (PlayerID = %d)" % (playerid)
        cur.execute(query)
        rows = cur.fetchall()
        previous_team = rows[0]["TeamID"]
        if(previous_team != new_teamId):
            query = "SELECT * FROM Teams WHERE (TeamID = %d)" % (previous_team)
            cur.execute(query)
            rows = cur.fetchall()
            if(playerid == rows[0]["CaptainID"]):
                print(
                    "Can't change the player team since player in captain of the team :(")
                tmp = input("Enter any key to continue> ")
                return
        # new_role = input("Role(Batsman, Bowler, AllRounder): ")
        query = "UPDATE Players SET Name = '%s', Age = %d, TeamID = %d WHERE PlayerID = %d" % (
            new_name, new_age, new_teamId, playerid)
        cur.execute(query)
        con.commit()
        print("Player Updated!")
    except Exception as e:
        con.rollback()
        print("Update failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue> ")
    return


def updateTeam(cur, con):
    try:
        query = "SELECT * FROM Teams"
        cur.execute(query)
        rows = cur.fetchall()
        for i in range(len(rows)):
            print(rows[i])
        teamid = int(
            input("Select TeamID of Team whose data you wish to change: "))
        new_name = input("New Name: ")
        query = "SELECT PlayerID, Name FROM Players WHERE (TeamID = %d)" % (
            teamid)
        cur.execute(query)
        rows = cur.fetchall()
        for i in rows:
            print(i)
        captainID = int(input("Select the PlayerID of the team Captain: "))
        query = "UPDATE Teams SET Name = '%s', CaptainID = %d WHERE TeamID = %d" % (
            new_name, captainID, teamid)
        cur.execute(query)
        con.commit()
        print("Team Updated!")
    except Exception as e:
        con.rollback()
        print("Update failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue> ")
    return


def updateMatch(cur, con):
    pass


def updateSeason(cur, con):
    try:
        query = "SELECT * FROM Seasons;"
        cur.execute(query)
        rows = cur.fetchall()
        for i in range(len(rows)):
            print(rows[i])
        oldyear = int(input("Select Year whose data you wish to change: "))
        SeasonYear = int(input("New Year: "))
        query = "UPDATE Seasons SET Year = %d WHERE Year = %d" % (
            SeasonYear, oldyear)
        cur.execute(query)
        con.commit()
        print("Season Updated!")
    except Exception as e:
        con.rollback()
        print("Update failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue> ")
    return


def updateStadium(cur, con):
    try:
        query = "SELECT * FROM Stadium;"
        cur.execute(query)
        rows = cur.fetchall()
        for i in range(len(rows)):
            print(rows[i])
        stadiumname = input(
            "Select Stadium Name of Stadium whose data you wish to change: ")
        stadiumName = input("New name: ")
        stadiumCity = input("New city: ")
        maxCap = int(input("New max capacity: "))
        homeTeamID = int(input("New home team ID: "))
        query = "UPDATE Stadium SET Stadium_Name = '%s', Stadium_City = '%s', Max_Capacity = %d, Home_Team = %d WHERE Stadium_Name = '%s' " % (
            stadiumName, stadiumCity, maxCap, homeTeamID, stadiumname)
        cur.execute(query)
        con.commit()
        print("Stadium updated!")
    except Exception as e:
        con.rollback()
        print("Update failed :(")
        print("Error: ", e)
    tmp = input("Enter any key to continue")
    return
