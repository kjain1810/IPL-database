#!/usr/bin/env python3

import subprocess as sp
import pymysql as sql
import pymysql.cursors as sqlcursor

from libs.addqueries import addPlayer, addTeam, addSeason, addMatch, addStadium


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
                    choice = int(input("Enter choice> "))
                    if choice == 1:
                        addPlayer(cur, con)
                    elif choice == 2:
                        addTeam(cur, con)
                    elif choice == 3:
                        addMatch()
                    elif choice == 4:
                        addSeason()
                    elif choice == 5:
                        addStadium()
                    else:
                        print("Invalid choice")

        except Exception as e:
            tmp = sp.call("clear", shell=True)
            print("Connection failed!")
            print("Error: ", e)
            tmp = input("Enter any key to continue> ")


if __name__ == '__main__':
    main()
