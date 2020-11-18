from configparser import ConfigParser
from Player import *
from datetime import datetime as date
import pymysql.cursors
from pymysql.cursors import Cursor
#Les variables 


class DB:

    today = date.today()

    def __init__(self):
        #Read config.ini file
        # self.config_object = ConfigParser()
        # self.config_object.read("config.ini")
        # self.db = self.config_object["DATABASE"]
        self.player = None
        self.connection = None

    
    def connectDB(self):
        char = str("%")
        self.connection = pymysql.connect(host="127.0.0.1",
        user="root",
        passwd="",
        database="Casino",
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
        return self.connection
        
    
        

    def getAllPlayers(self):
        sql = "SELECT username FROM players"

    def addPlayer(self,username):

        checkPlayer = self.checkRegistredPlayer(username) 
        if(checkPlayer== None):
            try:
                with self.connection.cursor() as cursor:
                    sql = "INSERT INTO Players ( username,createdAt,solde ) VALUES ( %s,%s,%s )"
                    cursor.execute(sql,(username,self.today,Player.INIT_MISE))
                    self.connection.commit()
    
            finally:
                self.closeConnection()
            
            return Player(username)
                
        else :
            self.player =Player(username)
            self.player.setSolde(checkPlayer["solde"])
            return self.player  

    #TODO
    def checkRegistredPlayer(self,username):
        try:
            with self.connection.cursor() as cursor:
                sql = ("SELECT username FROM Players WHERE username=%s ", (username,))
                cursor.execute(sql,(username))
                self.connection.commit()
                return cursor.fetchone()
                
        finally:
            self.closeConnection()

    # #TODO
    # def getPlayerStats(self,username):

    # #TODO
    # def getPlayerStats(self,username):


    

    # make a habit to close the database connection once you create it 
    def closeConnection(self):
        self.connection.close()



        

