
from tabulate import tabulate


def viewPlayers(cur, con):
    try:
        query = "SELECT * FROM Players"
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("There are no Players")
        else:
            headers = res[0].keys()
            res = [x.values() for x in res]
            print(tabulate(res, headers, tablefmt="pretty"))   
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
        if len(res) == 0:
            print("There are no Teams")
        else:
            headers = res[0].keys()
            res = [x.values() for x in res]
            print(tabulate(res, headers, tablefmt="pretty"))
        # for i in range(len(res)):
            # print(res[i])
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
        if len(res) == 0:
            print("There are no Matches")
        else:
            headers = res[0].keys()
            res = [x.values() for x in res]
            print(tabulate(res, headers, tablefmt="pretty"))        
        # for i in range(len(res)):
        #     print(res[i])
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
        if len(res) == 0:
            print("There are no Seasons")
        else:
            headers = res[0].keys()
            res = [x.values() for x in res]
            print(tabulate(res, headers, tablefmt="pretty"))
        # for i in range(len(res)):
        #     print(res[i])
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
        if len(res) == 0:
            print("There are no Stadiums")
        else:
            headers = res[0].keys()
            res = [x.values() for x in res]
            print(tabulate(res, headers, tablefmt="pretty"))
        # for i in range(len(res)):
        # print(res[i])
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
        if len(res) == 0:
            print("There are no Teams")
        else:
            headers = res[0].keys()
            res = [x.values() for x in res]
            print(tabulate(res, headers, tablefmt="pretty"))
            # for i in range(len(res)):
                # print(res[i])
            teamID = int(input("Select the teamID for which you want to view the information: "))
            query = "SELECT * FROM Players Where (TeamID = %d)" % (teamID)
            cur.execute(query)
            res = cur.fetchall()
            if len(res) == 0:
                print("There are no Players")
            else:
                headers = res[0].keys()
                res = [x.values() for x in res]
                print(tabulate(res, headers, tablefmt="pretty"))
                # print("Players:")
                # for i in range(len(res)):
                    # print(res[i])
                query = "SELECT * FROM TeamManagement WHERE (TeamID = %d)" % (teamID)
                cur.execute(query)
                res = cur.fetchall()
                if len(res) == 0:
                    print("There is no TeamMananagement")
                else:
                    headers = res[0].keys()
                    res = [x.values() for x in res]
                    print(tabulate(res, headers, tablefmt="pretty"))
        # print("Team Management:")
        # for i in range(len(res)):
            # print(res[i])
    except Exception as e:
        print("Couldn't fetch list :(")
        print("Error: ", e)
    tmp = input("Press any key to continue> ")
    return
