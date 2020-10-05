#!/usr/bin/env python3

def markFinished(cur, con):
    try:
        query = "SELECT Year FROM Seasons WHERE Finished=0"
        cur.execute(query)
        seasonList = cur.fetchall()
        if len(seasonList) == 0:
            print("Oops, no season running right now!")
            tmp = input("Enter any key to continue> ")
            return
        seasonToUpdate = seasonList[0]["Year"]
        print("Marking season %d as finished" % (seasonToUpdate))
        query = "UPDATE Batsman SET CurrentRuns=0"
        cur.execute(query)
        query = "UPDATE Bowler SET CurrentWickets=0"
        cur.execute(query)
        query = "UPDATE AllRounder SET CurrentRuns=0, CurrentWickets=0"
        cur.execute(query)
        query = "SELECT TeamID, Points FROM TeamResults"
        cur.execute(query)
        teamList = cur.fetchall()
        sortedList = sorted(teamList, key=lambda i: i["points"])
        for i in range(len(sortedList)):
            query = "INSERT INTO TeamResults(TeamID, SeasonYear, Standing) VALUES (%d, %d, %d)" % (
                sortedList["TeamId"], seasonToUpdate, i + 1)
            cur.execute(query)
        query = "UPDATE Seasons SET Finished=1 WHERE Year=%d" % (
            seasonToUpdate)
        cur.execute(query)
        con.commit()
        print("Season updated successfully!")
        tmp = input("Enter any key to continue> ")
    except Exception as e:
        con.rollback()
        print("Sorry, unable to update :(")
        print("Error: ", e)
        tmp = input("Enter any key to continue> ")
