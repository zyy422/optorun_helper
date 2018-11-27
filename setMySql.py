import pymysql

def exeData(startID =0, endID = 0):
    db = pymysql.connect("localhost", "root", "021213", "world")
    cursor=db.cursor()
    if startID==0 and endID ==0:
        sql = "SELECT Population,Name from  city"
    else:
        sql = "SELECT Population,Name from city where ID between "+str(startID)+" and "+str(endID)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except:
        print("Error:unable fetch data")
        db.close()
if  __name__  ==  "__main__" :
    print(exeData())