import sqlite

conn=sqlite3.connect('scrape_database')
curser=conn.cursor()

curser.execute('''CREATE TABLE IF NOT EXISTS catched (
    name TEXT NOT NULL ,
    client TEXT  ,
    annonce TEXT  ,
    deadline TEXT,
    receiver TEXT,
    description TEXT  
    
 
)''')
def fill_database():
    curser.execute('INSERT INTO main (name,letter_date,moment,deadline,receiver,description)  VALUES (?,?,?,?,?,?)' ,data_tupel)
    conn.commit()


def read_from_datebase():
    letters_list=[]
    curser.execute('SELECT * FROM main ORDER BY moment DESC')
    rows=curser.fetchall()
    for row in rows:
        #print (row)
        row=list(row)
        letters_list.append(row[1:])
 
    return letters_list

def delete_from_database(name):
    curser.execute('DELETE FROM main WHERE name = \'%s\'; ' %(name) )
    conn.commit()
