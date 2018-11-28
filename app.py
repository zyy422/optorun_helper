from flask import Flask,render_template,request,jsonify,send_from_directory,abort
from manageMysql import *
import xlrd,os

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():        # 根目录,也就是主目录
    if request.method == 'GET':
        # leak_data = show_leakrate()
        # exhaust_data_nor = show_exhaust_nor()
        # exhaust_data_150 = show_exhaust_150()
        # print(leak_data[0],exhaust_data_nor,exhaust_data_150)
        leakrate = 0

        return render_template("test03.html", datas=leakrate)

@app.route('/mode_1', methods=['POST'])
def mode_1():
    coater_style = request.form.get('coater')
    selected_mode = request.form.get('test_mode')
    date_begin = request.form.get('date_1')
    date_end =  request.form.get('date_2')
    print(coater_style,selected_mode,date_begin,date_end)
    return 'There is no data in this time range!'

@app.route('/mode_2', methods = ['POST'])
def mode_2():
    machine_no = request.form.get('machineNo')
    selected_mode = request.form.get('test_mode')
    datas = inquire_mode_2(machine_no, selected_mode)
    if selected_mode != '漏率':
        datas = datas[0][3:16]
    else:
        datas = datas[0][3:24]
    print(datas)
    return render_template("test03.html", datas=datas, selected_mode=selected_mode)

@app.route('/update_file', methods = ['POST'])
def update_file():
    serial_no = request.form.get('machineID')   # 获取工番号
    coater_style = request.form.get('coater')   # 获取镀膜机类型

    file = request.files['file']
    f = file.read()
    book = xlrd.open_workbook(file_contents=f)
    sheet_1_obj = book.sheet_by_index(0)

    # 读取Leakrate
    column_1 = sheet_1_obj.col_values(1)
    leakrate_data = column_1[2:23]

    # 读取室温下的真空度
    exhaust_nor_data = []
    for i in range(3, 16):
        data = xlrd.xldate_as_tuple(sheet_1_obj.cell(i, 3).value, 0)
        data = data[3]*60+data[4]*60+data[5]
        exhaust_nor_data.append(data)

    # 读取加热到150摄氏度下的真空度
    exhaust_150_data = []
    for i in range(3,16):
        data = xlrd.xldate_as_tuple(sheet_1_obj.cell(i, 5).value, 0)
        data = data[3] * 3600 + data[4] * 60 + data[5]
        exhaust_150_data.append(data)

    print(leakrate_data)
    print(exhaust_nor_data)
    print(exhaust_150_data)
    insert_leakrate(serial_no,coater_style,leakrate_data,)
    insert_exhaust_nor(serial_no,coater_style,exhaust_nor_data)
    insert_exhaust_150(serial_no,coater_style,exhaust_150_data)

    return render_template('test03.html')

@app.route('/machine_no', methods = ['POST'])
def machine_no():
    machine_id = show_machine_no()
    return render_template('test04.html',machine_id=machine_id)

@app.route('/mode_file', methods = ['POST'])
def mode_file():
        if os.path.isfile(r'C:\Users\Administrator\Desktop\webDev\optorun_helper\static\add.xlsx'):
            return send_from_directory(r'C:\Users\Administrator\Desktop\webDev\optorun_helper\static', 'add.xlsx', as_attachment=True)
        abort(404)


if __name__ == '__main__':
        app.run()