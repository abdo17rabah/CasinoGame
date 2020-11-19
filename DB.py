from configparser import ConfigParser
from Player import *
from datetime import datetime as date
import pymysql.cursors
from pymysql.cursors import Cursor
from Stats import *


class DB:

    today = date.today()

    def __init__(self):
        #Read config.ini file
        # self.config_object = ConfigParser()
        # self.config_object.read("config.ini")
        # self.db = self.config_object["DATABASE"]
        self.player = None
        self.connection = None
        self.stats= Stats()

    
    def connectDB(self):
        char = str("%")
        self.connection = pymysql.connect(host='localhost',
        unix_socket='/Applications/MAMP/tmp/mysql.sock',
        user="root",
        passwd="",
        database="Casino")
        return self.connection

    def getAllPlayers(self):
        sql = "SELECT name FROM players"

    def addPlayer(self,username):

        checkPlayer = self.checkRegistredPlayer(username) 
        if(checkPlayer== None):
            try:
                with self.connection.cursor() as cursor:
                    sql = "INSERT INTO players ( name,created_at,solde ) VALUES ( %s,%s,%s )"
                    cursor.execute(sql,(username,self.today,Player.INIT_MISE))
                    self.connection.commit()
                    checkPlayer = self.checkRegistredPlayer(username)
                    sql = "INSERT INTO stats (levelMax, miseMax, idPlayer) VALUES (%s, %s, %s)" 
                    cursor.execute(sql,(1, 0, checkPlayer['id']))
                    self.connection.commit()
                # with self.connection.cursor() as cursorStats : 
            except ValueError:
                print(ValueError)
                print("ERROR dans addPlayer")         
            finally:
                self.connection.cursor().close()  
                # self.closeConnection() 
            self.player = Player(username)
            self.player.setStats(self.stats)
                
        else :
            self.player =Player(username)
            self.player.setSolde(checkPlayer['solde'])
            #TODO : request to get all stats of the player
            #TODO : initialize the player' stats
            #self.stats.updateAllStats()

        return self.player
    #TODO
    def checkRegistredPlayer(self,username):
        try:
            with self.connection.cursor() as cursor:
                
                cursor.execute("SELECT * FROM players WHERE name= %s ", (str(username,)))
                fetchAnswer= cursor.fetchone()
                return fetchAnswer
                
        except ValueError:
            # self.closeConnection()
            print(ValueError)

    # #TODO
    # def getPlayerStats(self,username):

    # #TODO
    # def getPlayerStats(self,username):

    def updateTable(self,table,champs, val, idPlayer, username):
        checkPlayer = self.checkRegistredPlayer(username)
        if(checkPlayer != None):
            try:
                with self.connection.cursor() as cursor :
                    
                    # print(cursor.execute(sql, Vall))
                    cursor.execute(("UPDATE "+table+" SET " +champs+ "=" +str(val)+ "  WHERE idPlayer = %s"),(idPlayer,))
                    self.connection.commit()
                    print(cursor.rowcount, "record(s) affected")
            except ValueError:
                print(ValueError)
                print("ERROR dans updateStats")
            finally:
                self.connection.cursor().close()
                # self.closeConnection()
        else:
            print("Player introuvable")

            


    # make a habit to close the database connection once you create it 
    def closeConnection(self):
        self.connection.close()



db = DB()
db.connectDB()

