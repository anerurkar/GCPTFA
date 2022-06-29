from flask import Flask
from flask import  request
import psycopg2
import json
app = Flask(__name__)

@app.route('/')
def hello():
    return "welcome to custom network of gcp!"

@app.route('/read')
def read():
    return_records={}
    select_query="select * from employee "
    records=read_from_database(select_query)
    record_no=0
    for each_record in records:
        return_records["record-" +str(record_no)] = each_record
        record_no=record_no+1
    return json.dumps(return_records)

@app.route('/write')
def write():
    id   = request.args.get("id")
    name = request.args.get("name")
    age  = request.args.get("age")
    insert_query ="insert into employee(id,emp_name,emp_organization,emp_salary,emp_age) values(%s,%s,%s,%s,%s)"
    value_list=[id,name,'agiltics',3000,age]

    write_in_database(insert_query,value_list)
    return "success"

def create_connection():
    db_connection=psycopg2.connect(database="postgres", user="postgres", password="123456",host="34.93.10.35",port="5432")
    return db_connection

def read_from_database(query):
    try:
        connection_for_database=create_connection()
        print("database connected successfully for read operation")
        cursor=connection_for_database.cursor()
        cursor.execute(query)
        result_from_database=cursor.fetchall()
        return result_from_database
    except Exception as ex:
        print("exception raised while talking to database ")
        print(ex)
    finally:
        if (connection_for_database):
            cursor.close()
            connection_for_database.close()

def write_in_database(query,value_list):
    try:
        db_connection=create_connection()
        print("Connection created with database successfully for write operation")
        cursor=db_connection.cursor()
        cursor.execute(query,value_list)
        db_connection.commit()
        print("end of write operation")
    except Exception as ex:
        print("could not connect to database in write operation")
        print(ex)
    finally:
        if (db_connection):
            cursor.close()
            db_connection.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='3000')