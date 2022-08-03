import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date integers , professor text , course text , assignment text , deadline integers ,remarks text)")
    conn.commit()
    conn.close()

def insert(date , professor , course, assignment , deadline , remarks):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)",(date,professor,course,assignment,deadline,remarks) )
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=? ", (id,))
    conn.commit()
    conn.close()

def search(date='' , professor='' , course='' , assignment='' , deadline='' , remarks=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR professor=? OR course=? OR assignment=? OR deadline=? OR remark=?" , (date , professor , course , assignment , deadline , remarks))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
