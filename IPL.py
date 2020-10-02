#!/usr/bin/env python3

import subprocess as sp
import pymysql as sql
import pymysql.cursors as sqlcursor

from libs.addqueries import addPlayer, addTeam, addSeason, addMatch, addStadium
from libs.removequeries import removePlayer, removeTeam, removeSeason, removeMatch, removeStadium
from libs.updatequeries import updatePlayer, updateTeam, updateSeason, updateMatch, updateStadium


def main():
    while(1):
        tmp = sp.call("clear", shell=True)

        username = input("Username: ")
        password = input("Password: ")

        try:
            con = sql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='IPL',
                              cursorclass=sqlcursor.DictCursor)
            tmp = sp.call("clear", shell=True)

            if(con.open):
                print("Connected")
            else:
                print("Connection failed")

            tmp = input("Enter any key to continue>")

            with con.cursor() as cur:
                while(1):
                    tmp = sp.call("clear", shell=True)
                    print("1. Add player")
                    print("2. Add team")
                    print("3. Add match")
                    print("4. Add season")
                    print("5. Add stadium")
                    print("6, Delete player")
                    print("7, Delete team")
                    print("8, Update player")
                    print("9, Update Team")
                    print("10, Update Stadium")
                    print("11, Update Season")
                    choice = int(input("Enter choice> "))
                    if choice == 1:
                        addPlayer(cur, con)
                    elif choice == 2:
                        addTeam(cur, con)
                    elif choice == 3:
                        addMatch(cur, con)
                    elif choice == 4:
                        addSeason(cur, con)
                    elif choice == 5:
                        addStadium(cur, con)
                    elif choice == 6:
                        removePlayer(cur, con)
                    elif choice == 7:
                        removeTeam(cur, con)
                    elif choice == 8:
                        updatePlayer(cur, con)
                    elif choice == 9:
                        updateTeam(cur, con)
                    elif choice == 10:
                        updateStadium(cur, con)
                    elif choice == 11:
                        updateSeason(cur, con)
                    else:
                        print("Invalid choice")

        except Exception as e:
            tmp = sp.call("clear", shell=True)
            print("Connection failed!")
            print("Error: ", e)
            tmp = input("Enter any key to continue> ")


if __name__ == '__main__':
    main()
