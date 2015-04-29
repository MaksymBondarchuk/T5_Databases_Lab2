__author__ = 'Maxim'

import MySQLdb

def get_db():
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab2")
    return db

def db_cursor():
    # db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab2")
    return get_db().cursor()


def start_trigger():
    try:
        cursor = db_cursor()

        cursor.execute("create trigger trigger1 after insert on app_user\
                    for each row\
                    update trigger_test set number = number + 1 where id = 0")
    except:
        ()


def stop_trigger():
    try:
        cursor = db_cursor()

        cursor.execute("drop trigger trigger1")
    except:
        ()


def get_columns(cursor, table):
    cursor.execute("show columns from " + table)
    x0 = ""
    x1 = ""
    x2 = ""
    i = 0
    for x in cursor.fetchall():
        if i == 0:
            x0 = x[0]
        elif i == 1:
            x1 = x[0]
        else:
            x2 = x[0]
        i += 1
    return [(x0, x1)]


def get_data(table):
    cursor = db_cursor()

    cols = get_columns(cursor, table)
    cursor.execute("select * from " + table)
    return cols + [(x[0], x[1]) for x in cursor.fetchall()]


def get_data_proc(name):
    cursor = db_cursor()

    cursor.execute("show columns from app_user")
    x0 = ""
    x1 = ""
    x2 = ""
    i = 0
    for x in cursor.fetchall():
        if i == 0:
            x0 = x[0]
        elif i == 1:
            x1 = x[0]
        else:
            x2 = x[0]
        i += 1
    cols = [(x1, x2)]


    cursor.execute("call proc1('" + name + "')")
    return cols + [(x[0], x[1]) for x in cursor.fetchall()]