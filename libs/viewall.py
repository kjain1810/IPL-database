def viewPlayers(cur, con):
    try:
        query = "SELECT * FROM Players"
        cur.execute(query)
        res = cur.fetchall()
        for i in range(len(res)):
            print(res[i])
    except Exception as e:
        print("Couldn't fetch list :(")
        print("Error: ", e)
    tmp = input("Press any key to continue> ")
    return


def viewTeams(cur, con):
    try:
        query = "SELECT * FROM Teams"
        cur.execute(query)
        res = cur.fetchall()
        for i in range(len(res)):
            print(res[i])
    except Exception as e:
        print("Couldn't fetch list :(")
        print("Error: ", e)
    tmp = input("Press any key to continue> ")
    return


def viewMatches(cur, con):
    try:
        query = "SELECT * FROM Matches"
        cur.execute(query)
        res = cur.fetchall()
        for i in range(len(res)):
            print(res[i])
    except Exception as e:
        print("Couldn't fetch list :(")
        print("Error: ", e)
    tmp = input("Press any key to continue> ")
    return


def viewSeasons(cur, con):
    try:
        query = "SELECT * FROM Seasons"
        cur.execute(query)
        res = cur.fetchall()
        for i in range(len(res)):
            print(res[i])
    except Exception as e:
        print("Couldn't fetch list :(")
        print("Error: ", e)
    tmp = input("Press any key to continue> ")
    return


def viewStadiums(cur, con):
    try:
        query = "SELECT * FROM Stadium"
        cur.execute(query)
        res = cur.fetchall()
        for i in range(len(res)):
            print(res[i])
    except Exception as e:
        print("Couldn't fetch list :(")
        print("Error: ", e)
    tmp = input("Press any key to continue> ")
    return

def viewPlayersAndTeamManagement(cur, con):
    try:
        query = "SELECT * FROM Teams"
        cur.execute(query)
        res = cur.fetchall()
        for i in range(len(res)):
            print(res[i])
        teamID = int(input("Select the teamID for which you want to view the information: "))
        query = "SELECT * FROM Players Where (TeamID = %d)" % (teamID)
        cur.execute(query)
        res = cur.fetchall()
        print("Players:")
        for i in range(len(res)):
            print(res[i])
        query = "SELECT * FROM TeamManagement WHERE (TeamID = %d)" % (teamID)
        cur.execute(query)
        res = cur.fetchall()
        print("Team Management:")
        for i in range(len(res)):
            print(res[i])
    except Exception as e:
        print("Couldn't fetch list :(")
        print("Error: ", e)
    tmp = input("Press any key to continue> ")
    return
