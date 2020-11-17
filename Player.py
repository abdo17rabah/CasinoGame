#Import mysql
import pymysql.cursors
from pymysql.cursors import Cursor
from datetime import datetime as date
#Les variables 
today = date.today()

class Player:
    global connection
    
    def connectDB():
        
        connection = pymysql.connect(host='127.0.0.1',
                                    user = 'root',
                                    password = 'Mysticfulls1',
                                    db = 'casino',
                                    cursorclass = pymysql.cursors.DictCursor)
        return connection
        
    connection = connectDB()

    def setPlayerName(name_user):
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO players (name, created_at) "\
                    + "values(%s, %s)"
                cursor.execute(sql,(name_user,today))
                connection.commit()
                
        finally:
            connection.close()
            print('Bienvenue, votre nom à bien été ajouté à notre base de donnée: ')
            
    def getPlayerName():
        with connection.cursor() as cursor:
            #SQL
            sql = "SELECT * FROM players"
            #Executer la requete sql 
            cursor.execute(sql)
            return cursor.fetchall()
    
    