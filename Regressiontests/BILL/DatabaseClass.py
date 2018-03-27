import pymssql
import _mssql
import Global

class DatabaseClass:
#http://www.pymssql.org/en/stable/pymssql_examples.html
#http://www.pymssql.org/en/stable/_mssql_examples.html
    def DB_Execute_Querry(self, sql):
        connection = pymssql.connect(server=Global.DATABASE_IP,
                                user=Global.DATABASE_USER,
                                password=Global.DATABASE_PWD,
                                port=Global.DATABASE_PORT,
                                database=Global.DATABASE_NAME)
        try:
                cursor = connection.cursor()
                cursor.execute(sql)
                result = cursor.fetchall()
                #connection.commit()   # commit transaction
                print "DB_Execute_Querry"
                print  result  # shows result from query!
        finally:
            connection.close()
        return result
    def DB_Execute_Scalar(self, sql):
        connection = _mssql.connect(server=Global.DATABASE_IP,
                                user=Global.DATABASE_USER,
                                password=Global.DATABASE_PWD,
                                port=Global.DATABASE_PORT,
                                database=Global.DATABASE_NAME)
        try:
                result = connection.execute_scalar(sql)
                print "DB_Execute_Scalar"
                print  result  # shows result from query!
        finally:
            connection.close()
        return result
