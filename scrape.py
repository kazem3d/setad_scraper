import requests
from bs4 import BeautifulSoup
import csv
import codecs
import jdatetime
import sqlite3

conn=sqlite3.connect('scrape_database')
curser=conn.cursor()
curser.execute('''CREATE TABLE IF NOT EXISTS catched (
    need_number TEXT,
    need TEXT NOT NULL ,
    client TEXT  ,
    province TEXT  ,
    stuff_type TEXT,
    announce_time TEXT,
    deadline_date TEXT  
    
 
)''')


def fill_database(data_list):
    curser.execute('INSERT INTO catched (need_number,need,client,province,stuff_type,announce_time,deadline_date)  VALUES (?,?,?,?,?,?,?)' ,tuple(data_list))
    conn.commit()

# f = csv.writer(codecs.open('output.csv', 'w','utf-8'))
# f.writerow(['need','client','province','stuff_type','announce_time','dead_line'])

pages=[]
for i in range(1,2):

    # url='https://eproc.setadiran.ir/eproc/needs.do?d-146909-p='+str(i)
    url='https://eproc.setadiran.ir/eproc/needs.do'
    pages.append(url)


for item in pages:    
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    scrape_time=jdatetime.datetime.now()


    # soup = BeautifulSoup(open('needs.html'), 'html.parser')

    table_list=soup.find_all('tbody')[0]
    table_rows_list=table_list.find_all('tr')

    for row in table_rows_list:
        l=[]
        print('***************************************************')
        need_number=row.find('a').contents[0]
        cell_contents=row.find_all('span')
        need=cell_contents[0].get('title')
        client=cell_contents[1].get('title')
        province=cell_contents[2].get('title')
        stuff_type=cell_contents[4].get('title')
        announce_time=cell_contents[6].text
        dead_line=cell_contents[7].get('title')

        
        dead_line_list=dead_line.split()
    
        if 'روز' in dead_line_list:
            i=dead_line_list.index('روز')
            day=dead_line_list[i-1]
        else: 
            day=0
        if 'ساعت' in dead_line_list:
            i=dead_line_list.index('ساعت')
            hour=dead_line_list[i-1]
        else : 
            hour=0    

        deadline_obj=scrape_time+jdatetime.timedelta(days=int(day),hours=int(hour))
        deadline_date=deadline_obj.strftime('%Y/%m/%d')

        l=[int(need_number),need,client,province,stuff_type,announce_time,deadline_date]

        #display each row cintents
        print('need_number=', need_number)

        print('need=', need)
        print('client=', client)
        print('province=', province)
        print('stuff_type=', stuff_type)
        print('announce_time=', announce_time)
        print('deadline_date=', deadline_date)

        fill_database(l)
        # f.writerow(l)

#when reading new page if some duplicate item is in deleting them
def delete_duplicate():
    curser.execute('DELETE FROM catched WHERE rowid NOT IN (SELECT min(rowid) FROM catched GROUP BY need_number);')
    conn.commit()
    print('duplicate item deleted')

delete_duplicate()