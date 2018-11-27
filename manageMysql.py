import pymysql

def show_leakrate():
    db = pymysql.connect("localhost", "root", "021213", "optorun")
    cursor = db.cursor()
    sql = "SELECT 0_min,1_min,2_min,3_min,4_min,5_min,\
    6_min,7_min,8_min,9_min,10_min,11_min,12_min,13_min,\
    14_min,15_min,16_min,17_min,18_min,19_min,20_min from  LeakRate;"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except:
        print("Error: leakrate unable fetch data")
    db.close()

def show_exhaust_nor():
    db = pymysql.connect("localhost", "root", "021213", "optorun")
    cursor = db.cursor()
    sql = "SELECT aa,bb,cc,dd,ee,ff,\
    gg,hh,ii,jj,kk,ll,mm from  Exhaust_nor;"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except:
        print("Error:exhaust_nor unable fetch data")
    db.close()

def show_exhaust_150():
    db = pymysql.connect("localhost", "root", "021213", "optorun")
    cursor = db.cursor()
    sql = "SELECT aa,bb,cc,dd,ee,ff,\
    gg,hh,ii,jj,kk,ll,mm from  Exhaust_150;"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except:
        print("Error:exhaust_nor unable fetch data")
    db.close()

def insert_leakrate(serial_no,coater_style,times):
    db = pymysql.connect("localhost", "root", "021213", "optorun")
    cursor = db.cursor()
    sql = "INSERT INTO LeakRate (SerialNo,Coater_Style,0_min,1_min,2_min,3_min,4_min,5_min," \
          "6_min,7_min,8_min,9_min,10_min,11_min,12_min,13_min,14_min,15_min," \
          "16_min,17_min,18_min,19_min,20_min) values ('%s','%s'," \
          "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
          "%s,%s,%s)" %(serial_no,coater_style,times[0],times[1],times[2],times[3],times[4],
                        times[5],times[6],times[7],times[8],times[9],
                        times[10],times[11],times[12],times[13],times[14],times[15],
                        times[16],times[17],times[18],times[19],times[20])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("存入表insert_leakrate失败")
        db.rollback()
    db.close()

def insert_exhaust_nor(serial_no,coater_style,exhaust_nor_data):
    db = pymysql.connect("localhost", "root", "021213", "optorun")
    cursor = db.cursor()
    sql = "INSERT INTO Exhaust_nor (SerialNo,Coater_Style,aa,bb,cc,dd,ee,ff,gg," \
          "hh,ii,jj,kk,ll,mm) values ('%s','%s',%s,%s,%s,%s,%s,%s,%s," \
          "%s,%s,%s,%s,%s,%s)" %(serial_no,coater_style,exhaust_nor_data[0],exhaust_nor_data[1],
                                  exhaust_nor_data[2],exhaust_nor_data[3],exhaust_nor_data[4],
                                  exhaust_nor_data[5],exhaust_nor_data[6],exhaust_nor_data[7],
                                  exhaust_nor_data[8],exhaust_nor_data[9],exhaust_nor_data[10],
                                  exhaust_nor_data[11],exhaust_nor_data[12])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("存入表insert_exhaust_nor失败")
        db.rollback()
    db.close()

def insert_exhaust_150(serial_no,coater_style,exhaust_150_data):
    db = pymysql.connect("localhost", "root", "021213", "optorun")
    cursor = db.cursor()
    sql = "INSERT INTO Exhaust_150 (SerialNo,Coater_Style,aa,bb,cc,dd,ee,ff,gg," \
          "hh,ii,jj,kk,ll,mm) values ('%s','%s',%s,%s,%s,%s,%s,%s,%s," \
          "%s,%s,%s,%s,%s,%s)" %(serial_no,coater_style,exhaust_150_data[0],exhaust_150_data[1],
                                  exhaust_150_data[2],exhaust_150_data[3],exhaust_150_data[4],
                                  exhaust_150_data[5],exhaust_150_data[6],exhaust_150_data[7],
                                  exhaust_150_data[8],exhaust_150_data[9],exhaust_150_data[10],
                                  exhaust_150_data[11],exhaust_150_data[12])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("存入表insert_exhaust_150失败")
        db.rollback()
    db.close()

def inquire_mode_2(machine_no, selected_mode):
    db = pymysql.connect("localhost", "root", "021213", "optorun")
    cursor = db.cursor()
    if selected_mode == '抽速（室温）':
        sql = "SELECT * FROM Exhaust_nor WHERE SerialNo = '%s'" % (machine_no)
    elif selected_mode == '抽速（150℃）':
        sql = "SELECT * FROM Exhaust_150 WHERE SerialNo = '%s'" % (machine_no)
    else:
        sql = "SELECT * FROM Leakrate WHERE SerialNo = '%s'" % (machine_no)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except:
        print("Error:exhaust_nor unable fetch data")
    db.close()

def show_machine_no():
    db = pymysql.connect("localhost", "root", "021213", "optorun")
    cursor = db.cursor()
    sql = "SELECT SerialNo FROM Exhaust_nor"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()      # 未经处理的数据库的数据
    except:
        print("Error:show_machine_no unable fetch data")
    buffer = []             # 用来存数据库中获取的数据
    for item in result:
        buffer.append(item[0])
    return buffer
    db.close()