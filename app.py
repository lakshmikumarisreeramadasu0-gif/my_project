from flask import Flask,session,render_template,request
import mysql.connector

app = Flask(__name__)
app.secret_key = "5878"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/adminloginchk",methods =["Get","post"])
def adminloginchk():
    uid = request.form.get('unm')
    pswd = request.form.get('pass')
    print(uid,pswd)

    if uid=="admin" and pswd=="admin":

        return render_template("admin_home.html")

    else:
        return render_template("admin.html",msg="fail")

    return

@app.route("/adminhome")
def adminhome():
    return render_template("admin_home.html")

@app.route("/add_car")
def add_car():
    return render_template("add_car.html")

@app.route("/add_new_car",methods=["get","post"])
def add_new_car():

    company = request.form['car_comp']
    model = request.form['car_model']
    cost = request.form['car_price']
    fuel = request.form['fuel_type']
    trans = request.form['trans_type']
    sun_roof = request.form['sunroof']
    air_bags = request.form['airbags']
    camera = request.form['cameras']
    gps_track = request.form['gps']
    seat = request.form['seats']
    engine_cap = request.form['cc']
    mileage = request.form['milg']
    files = request.files["file"]
    con, cur = database()
    qry = "insert into car_details (car_company,car_model,car_price,fuel_type,transmsn_type,sun_roof,air_bags,park_cameras,gps_track,seats,engine_cap,mileage,car_pic) values  ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    cur.execute(qry%(company,model,cost,fuel,trans,sun_roof,air_bags,camera,gps_track,seat,engine_cap,mileage,files.filename))
    con.commit()

    return render_template("add_car.html",msg="added")

@app.route("/add_bike")
def add_bike():
    return render_template("add_bike.html")

@app.route("/add_new_bike",methods=["get","post"])
def add_new_bike():

    company = request.form['bike_comp']
    model = request.form['bike_model']
    cost = request.form['bike_price']
    fuel = request.form['fuel_type']
    trans = request.form['trans_type']
    spdm = request.form['speedometer']
    brake_sytem = request.form['brakesystem']
    blue_tooth = request.form['bluetooth']
    usb_port = request.form['usb']
    gps_track = request.form['gps']
    engine_cap = request.form['cc']
    mileage = request.form['milg']
    files = request.files["file"]
    con, cur = database()
    qry = "insert into bike_details (bike_company,bike_model,bike_price,fuel_type,transmsn_type,speedometer,brake_system,bluetooth,usb_ports,gps_system,engine_cap,mileage,bike_pic) values  ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    cur.execute(qry%(company,model,cost,fuel,trans,spdm,brake_sytem,blue_tooth,usb_port,gps_track,engine_cap,mileage,files.filename))
    con.commit()

    return render_template("add_bike.html",msg="added")

@app.route("/view_cars")
def view_cars():
    con,cur = database()
    qry = "select * from car_details"
    cur.execute(qry)
    res = cur.fetchall()
    #print(res)
    return render_template("view_cars.html",car_details=res)

@app.route("/update_car/<sno>")
def update_car(sno):
    con,cur = database()
    qry="select * from car_details where sno='"+sno+"'"
    cur.execute(qry)
    vals = cur.fetchall()
    for row in vals:
        sno = row[0]
        cmpny = row[1]
        model = row[2]
        cost = row[3]
        fuel = row[4]
        trans = row[5]
        roof =row[6]
        bags = row[7]
        cam = row[8]
        gps = row[9]
        seats = row[10]
        cap = row[11]
        mil = row[12]
    return render_template("car_update.html",sno=sno,car_comp=cmpny,car_model=model,car_price=cost,fuel_type=fuel,trans_type=trans,
                           sunroof=roof,airbags=bags,park_cam=cam,gps_track=gps,seats=seats,cc=cap,milg=mil)

@app.route("/update_car2",methods=["POST", "GET"])
def update_car2():
    sno = request.form['id']
    cmpny = request.form['car_comp']
    model = request.form['car_model']
    cost = request.form['car_price']
    fuel = request.form['fuel_type']
    trans = request.form['trans_type']
    sun_roof = request.form['sunroof']
    air_bags = request.form['airbags']
    park_cam = request.form['cam']
    gps_track = request.form['gps']
    seat = request.form['seats']
    engine_cap = request.form['cc']
    mileage = request.form['milg']
    con, cur = database()
    acq = "UPDATE  car_details SET car_company='%s',car_model='%s',car_price='%s',fuel_type='%s'," \
          "transmsn_type='%s',sun_roof='%s',air_bags='%s',park_cameras='%s',gps_track='%s',seats='%s',engine_cap='%s',mileage='%s' where sno='"+sno+"'  "
    cur.execute(acq%(cmpny,model,cost,fuel,trans,sun_roof,air_bags,park_cam,gps_track,seat,engine_cap,mileage))
    con.commit()
    vq = "select * from car_details"
    cur.execute(vq)
    res = cur.fetchall()
    #print(res)
    return render_template("view_cars.html",car_details=res ,msg="updated")

@app.route("/delete_car/<sno>")
def delete_car(sno):
    con, cur = database()
    cur.execute("delete from car_details where sno='"+sno+"' ")
    con.commit()
    qry="select * from car_details"
    cur.execute(qry)
    res = cur.fetchall()
    return render_template("view_cars.html", car_details=res, msg2="deleted")

@app.route("/view_bikes")
def view_bikes():
    con,cur = database()
    qry = "select * from bike_details"
    cur.execute(qry)
    res = cur.fetchall()
    #print(res)
    return render_template("view_bikes.html",bike_details=res)

@app.route("/update_bike/<sno>")
def update_bike(sno):
    con,cur = database()
    qry="select * from bike_details where sno='"+sno+"'"
    cur.execute(qry)
    vals = cur.fetchall()
    for row in vals:
        sno = row[0]
        cmpny = row[1]
        model = row[2]
        cost = row[3]
        fuel = row[4]
        trans = row[5]
        spdm = row[6]
        brake = row[7]
        blth = row[8]
        usb = row[9]
        gps = row[10]
        cap = row[11]
        mil = row[12]

    return render_template("bike_update.html",sno=sno,bike_comp=cmpny,bike_model=model,bike_price=cost,fuel_type=fuel,trans_type=trans,
                           speed=spdm,bs=brake,bluetooth=blth,ports=usb,gps=gps,cc=cap,milg=mil)

@app.route("/update_bike2",methods=["POST", "GET"])
def update_bike2():
    sno = request.form['id']
    cmpny = request.form['bike_comp']
    model = request.form['bike_model']
    cost = request.form['bike_price']
    fuel = request.form['fuel_type']
    trans = request.form['trans_type']
    spdm = request.form['speedometer']
    bkstm = request.form['brakes']
    blth = request.form['bluetooth']
    usb = request.form['usb_charge']
    gps_track = request.form['gps']

    engine_cap = request.form['cc']
    mileage = request.form['milg']
    con, cur = database()
    acq = "UPDATE  bike_details SET bike_company='%s',bike_model='%s',bike_price='%s',fuel_type='%s',transmsn_type='%s'," \
          "speedometer='%s',brake_system='%s',bluetooth='%s',usb_ports='%s',gps_system='%s',engine_cap='%s',mileage='%s' where sno='"+sno+"'  "
    cur.execute(acq%(cmpny,model,cost,fuel,trans,spdm,bkstm,blth,usb,gps_track,engine_cap,mileage))
    con.commit()
    vq = "select * from bike_details"
    cur.execute(vq)
    res = cur.fetchall()
    #print(res)
    return render_template("view_bikes.html",bike_details=res ,msg="updated")

@app.route("/delete_bike/<sno>")
def delete_bike(sno):
    con, cur = database()
    cur.execute("delete from bike_details where sno='"+sno+"' ")
    con.commit()
    qry="select * from bike_details"
    cur.execute(qry)
    res = cur.fetchall()
    return render_template("view_bikes.html", bike_details=res, msg2="deleted")

#USER SECTION

@app.route("/signup")
def signup():

    return render_template("signup.html")

@app.route("/user_signup",methods=["post","get"])
def user_signup():
    name = request.form['name']
    uid = request.form['uid']
    pswd = request.form['pwd']
    mail = request.form['email']
    mno = request.form['phno']

    con, cur = database()

    sql = "select count(*) from register where userid='" + uid + "' "
    cur.execute(sql)
    res = cur.fetchone()[0]
    if res > 0:
        return render_template("signup.html", msg="already exists..!")

    else:
        sts = "insert into register(name,userid,passwrd,email,contact) values  ('%s','%s','%s','%s','%s')"
        cur.execute(sts % (name,uid,pswd,mail,mno))
        con.commit()

        return render_template("user.html", msg="Registered Successfully..! Login Here.")

    return " "

@app.route("/signin")
def signin():
    return render_template("user.html")

@app.route("/userloginchk",methods=["post","get"])
def userloginchk():
    uid = request.form['uid']
    pswd = request.form['pwd']
    con,cur = database()
    qry = "select count(*) from register where userid='%s' and passwrd='%s' "
    cur.execute(qry%(uid,pswd))
    res = cur.fetchone()[0]
    if res>0:
        session['uid']= uid
        sql = "select name from register where userid='"+uid+"' "
        cur.execute(sql)
        name = cur.fetchone()
        return render_template("user_home.html",name = name)
    else:
        return render_template("user.html",msg="fail")

@app.route("/uhome")
def uhome():
    return render_template("user_home.html")

@app.route("/search_car")
def search_car():
    return render_template("search_car.html")

@app.route("/search_bike")
def search_bike():
    return render_template("search_bike.html")

@app.route("/search_carlist", methods=["POST", "GET"])
def search_carlist():
    car_budget = request.form['budget']
    print(car_budget)

    # Split the budget range into min and max values
    min_budget, max_budget = map(int, car_budget.split('-'))
    # Database connection
    con, cur = database()

    # Corrected SQL query with parameterized values
    qry = "SELECT * FROM car_details WHERE car_price BETWEEN %s AND %s"

    cur.execute(qry, (min_budget, max_budget))
    res = cur.fetchall()
    print(res)

    return render_template("search_carlist.html",values=res)

@app.route("/search_bikelist", methods=["POST", "GET"])
def search_bikelist():
    bike_budget = request.form['budget']
    print(bike_budget)
    # Split the budget range into min and max values
    min_budget, max_budget = map(int, bike_budget.split('-'))
    # Database connection
    con, cur = database()
    # Corrected SQL query with parameterized values
    qry = "SELECT * FROM bike_details WHERE bike_price BETWEEN %s AND %s"

    cur.execute(qry, (min_budget, max_budget))
    res = cur.fetchall()
    print(res)

    return render_template("serach_bikelist.html",values=res)


@app.route("/compare_cars")
def compare_cars():
    car_model = []
    con,cur = database()
    qry = "select car_model from car_details"
    cur.execute(qry)
    models = cur.fetchall()
    for model in models:
        main = model[0]
        car_model.append(main)
    #print(car_model)

    return render_template("compare_cars.html",car_models=car_model)

@app.route("/compare_bikes")
def compare_bikes():
    bike_model = []
    con,cur = database()
    qry = "select bike_models from bike_details"
    cur.execute(qry)
    models = cur.fetchall()
    for model in models:
        main = model[0]
        bike_model.append(main)
    #print(car_model)

    return render_template("compare_bikes.html",bike_models=bike_model)

@app.route("/compare_carlist",methods=["get","post"])
def compare_carlist():
    first_car = request.form['car_comp']
    first_model = request.form['car_model']
    second_car = request.form['car_comp2']
    second_model = request.form['car_model2']
    con,cur = database()
    qry = "select * from car_details where car_company='"+first_car+"' and car_model='"+first_model+"'"
    cur.execute(qry)
    first_details = cur.fetchone()
    qry2 = "select * from car_details where car_company='" + second_car + "' and car_model='" + second_model + "'"
    cur.execute(qry2)
    second_details = cur.fetchone()
    print(first_details)
    print(second_details)
    return render_template("compare_carlist.html",car1=first_details,car2=second_details)

@app.route("/compare_bikelist",methods=["get","post"])
def compare_bikelist():
    first_bike = request.form['bike_comp']
    first_model = request.form['bike_model']
    second_bike = request.form['bike_comp2']
    second_model = request.form['bike_model2']
    con,cur = database()
    qry = "select * from bike_details where bike_company='"+first_bike+"' and bike_model='"+first_model+"'"
    cur.execute(qry)
    first_details = cur.fetchone()
    qry2 = "select * from bike_details where bike_company='" + second_bike + "' and bike_model='" + second_model + "'"
    cur.execute(qry2)
    second_details = cur.fetchone()
    print(first_details)
    print(second_details)
    return render_template("compare_bikelist.html",bike1=first_details,bike2=second_details)


def database():
    con = mysql.connector.connect(host="localhost",user="root",password="root",port="3306",database="car_comparison")
    cur = con.cursor()
    return con,cur



if __name__  == '__main__':
    app.run(port=1234,debug=True)

