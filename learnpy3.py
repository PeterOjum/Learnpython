import pandas as pd
import sqlite3
from datetime import timedelta

def student_report(dbfile, id):
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    transcript = ""
    query = "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name;"
    for row in c.execute(query).fetchall():
        query = "SELECT last, first, grade FROM " + row[0] + " WHERE id = " + id + ";"
        result = c.execute(query).fetchone()
        if result: # the student is in this table
            if not transcript: # the header has not been created
                transcript += result['last'] + ', ' + result['first'] + ', ' + id 
                transcript += '\n' + '-' * len(transcript) + '\n'
            transcript += row['name'].replace('_', ' ') + ': ' + result['grade'] + '\n'
            
    conn.close()
    return transcript
    
def A_students(conn, tname="ISTA_131_F17", standing=None, max_results=10):
    c = conn.cursor()
    mid = (' AND level LIKE \'' + standing  + '\'' 
            if standing else '')
    query = ("SELECT last || ', ' || first AS name " +
             "FROM " + tname + " WHERE grade = 'A'")
    query += mid + " ORDER BY name LIMIT " + str(max_results) +  ";"
    c.execute(query)
    return [row[0] for row in c.fetchall()]
    
def class_performance(conn, tname="ISTA_131_F17"):
    c = conn.cursor()
    total_studs = c.execute('SELECT COUNT(*) FROM ' + tname + ';').fetchone()[0]
    c.execute('SELECT UPPER(grade), count(*) FROM ' + tname + ' GROUP BY grade;')
    performance = {}
    for row in c.fetchall():
        performance[row[0]] = round(row[1] / total_studs * 100, 1)
    return performance
    
def read_frame():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    names = [m + suffix for m in months for suffix in ['_r', '_s']]
    # sun_frame = pd.read_csv('sunrise_sunset.csv', header=None, index_col=0, names=names, dtype=str)
    # sun_frame.to_pickle('sun_frame.pkkl') # delete extra 'k'
    return pd.read_csv('sunrise_sunset.csv', header=None, index_col=0, names=names, dtype=str)

def get_series(sun_frame):
    ''' Change the name of set '''
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    rise = pd.concat([sun_frame[m + '_r'] for m in months])
    sset = pd.concat([sun_frame[m + '_s'] for m in months])
    rise, sset = rise.dropna(), sset.dropna()
    rise.index = sset.index = pd.date_range('010118', '123118')
    # rise.to_pickle('sunrise.pkkl') # delete extra 'k'
    # set.to_pickle('sunset.pkkl') # delete extra 'k'
    return rise, sset

def longest_day(rise, sset):
    rise_m = rise.astype(int) // 100 * 60 + rise.astype(int) % 100
    set_m = sset.astype(int) // 100 * 60 + sset.astype(int) % 100
    daylen = set_m - rise_m
    dt = daylen.idxmax()
    hm = str(daylen[dt] // 60) + str(daylen[dt] % 60)
    return dt, hm
    
def sunrise_dif(rise, dt):
    rise_m = rise.astype(int) // 100 * 60 + rise.astype(int) % 100
    return rise_m.loc[dt - timedelta(90)] - rise_m.loc[dt + timedelta(90)]

