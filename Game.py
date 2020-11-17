from Player import connection


class Game:

    
    def setStack(stack,idPlayer):
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO game (stack, idPlayer) VALUES (%s, %s) "
                val = (stack,idPlayer)
                cursor.execute(sql,val)
                connection.commit()
                
        finally:
            connection.close() 
            
    def getGame(idPlayer):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM game WHERE idPlayer= %s",(int(idPlayer,)))
            return cursor.fetchall()