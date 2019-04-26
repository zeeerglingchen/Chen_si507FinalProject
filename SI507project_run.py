import csv
import os
from flask import Flask, render_template, session, redirect, url_for, request # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this
from SI507project_tools import getweibodata
from random import choice

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./fans.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


class Fans(db.Model):
    __tablename__ = "fans"
    Id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    User_id = db.Column(db.String(32))
    Name = db.Column(db.String(32))
    # Rank = db.Column(db.Integer)
    Self_intro = db.Column(db.String(70))
    # Other_intro = db.Column(db.String(32))
    Fans_count = db.Column(db.Integer)
    Following_count = db.Column(db.Integer)
    # Posts_count = db.Column(db.Integer)


    Userid_id = db.Column(db.Integer,db.ForeignKey("userid.Id"))
    Type_id = db.Column(db.Integer,db.ForeignKey("type.Id"))

    userid = db.relationship("UserId")
    type = db.relationship("Type")

        # wonder what will the foriegnkey return
    def __repr__(self):
        return "The user whose name is {} has {} followers and is following {} people".format(self.Name, self.Fans_count,self.Following_count)

class UserId(db.Model):
    __tablename__ = "userid"
    Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    IdNum = db.Column(db.String(64))


class Type(db.Model):
    __tablename__ = "type"
    Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    TypeName = db.Column(db.String(64))

    def __repr__(self):
        return"The type of the user is {}".format(self.TypeName)

# if __name__ == '__main__':

proxy_addr_lst = ["122.241.72.191:808","121.40.78.138:3128","118.190.73.168:808","122.241.72.191:808","27.191.234.69:9999","112.85.168.236:9999"]
random_ip = choice(proxy_addr_lst)

def set_up_database(userid,csv_file_name):

    userid_data = UserId.query.filter_by(IdNum = userid).first()
    if userid_data:
        pass
    else:
        userid_data = UserId(IdNum = userid)
    session.add(userid_data)


    row_lst = []
    with open(csv_file_name,"r") as csvdata:
        reader = csv.reader(csvdata)
        for row in reader:
            row_lst.append(row)
    csvdata.close()

    for i in row_lst[1:]:
        type_data = Type.query.filter_by(TypeName = i[-1]).first()
        if type_data:
            pass
        else:
            type_data = Type(TypeName = i[-1] )


        session.add(type_data)

    session.commit()

    for i in row_lst[1:]:
        type_data = Type.query.filter_by(TypeName = i[-1]).first()
        userid_data = UserId.query.filter_by(IdNum = userid).first()

        fan_data = Fans(
                User_id = i[1],
                Name = i[0],
                # Rank = i[2],
                Self_intro = i[2],
                # Other_intro = i[4],
                Fans_count = i[3],
                Following_count = i[4],
                # Posts_count = i[8],
                Userid_id = userid_data.Id,
                Type_id = type_data.Id
            )

        session.add(fan_data)

    session.commit()

@app.route('/')
def index():
    db.create_all()
    return render_template("index.html")

@app.route('/get_data',methods =['GET','POST'])
def test():
    if request.method == "POST":
        weiboid = request.form
        USERID = str(weiboid["Id"])
        userid_data = UserId.query.filter_by(IdNum = USERID).first()


        if userid_data:
            return render_template("error.html")

        else:
            csv_file_name = getweibodata(USERID,random_ip)
            set_up_database(USERID, csv_file_name)
            user_primary_id = UserId.query.filter_by(IdNum = USERID).first().Id

            all_fans = Fans.query.filter_by(Userid_id = user_primary_id).all()
            num_fans = len(all_fans)

            real_fans = Type.query.filter_by(TypeName = "real").first().Id
            fake_fans = Type.query.filter_by(TypeName = "fake").first().Id
            unsure = Type.query.filter_by(TypeName = "unsure").first().Id


            real = len( Fans.query.filter_by(Type_id = real_fans).filter_by(Userid_id = user_primary_id).all())
            fake = len(Fans.query.filter_by(Type_id = fake_fans).filter_by(Userid_id = user_primary_id).all())
            unsure = len(Fans.query.filter_by(Type_id = unsure).filter_by(Userid_id = user_primary_id).all())



            return render_template("getdata.html",
            fans_count = num_fans,
            real_fans_counts = real,
            fake_fans_counts = fake,
            unsure_counts = unsure )


    else:
        print("request")


@app.route('/result')
def result():
    id_lst = []
    lst = UserId.query.all()
    num = len(lst)
    # id_lst.append(lst[0].IdNum)
    for i in range(num):
        id_lst.append(lst[i].IdNum)

    return render_template("result.html",id_lst = id_lst, num = num)

@app.route('/result/<id>')
def profile(id):
    user_primary_id = UserId.query.filter_by(IdNum = id).first().Id

    all_fans = Fans.query.filter_by(Userid_id = user_primary_id).all()
    num_fans = len(all_fans)

    real_fans = Type.query.filter_by(TypeName = "real").first().Id
    fake_fans = Type.query.filter_by(TypeName = "fake").first().Id
    unsure = Type.query.filter_by(TypeName = "unsure").first().Id


    real = len( Fans.query.filter_by(Type_id = real_fans).filter_by(Userid_id = user_primary_id).all())
    fake = len(Fans.query.filter_by(Type_id = fake_fans).filter_by(Userid_id = user_primary_id).all())
    unsure = len(Fans.query.filter_by(Type_id = unsure).filter_by(Userid_id = user_primary_id).all())



    return render_template("getdata.html",
            fans_count = num_fans,
            real_fans_counts = real,
            fake_fans_counts = fake,
            unsure_counts = unsure )






app.run()

# how to overwrite everytime I run this code,
# how to store the data(db) from different search
