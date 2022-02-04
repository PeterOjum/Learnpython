import csv, sqlite3, numpy as np

def is_power_of_2(n):
    if n <= 0:
        return False
    if n in [1, 2]:
        return True
    while abs(n % 2) != 1 and n != 2:
        n //= 2
    return n == 2
    
def is_power_of_22(n):
    return n and not n & (n - 1)
    
def all_power_of_2(matrix):
    for row in matrix:
        for num in row:
            if not is_power_of_2(num):
                return False
    return True
    
def all_power_of_22(matrix):
    return all([is_power_of_2(n) for row in matrix for n in row])
    
def all_power_of_23(matrix):
    return np.vectorize(is_power_of_2)(arr).all()
    
def first_divisible(matrix, n=2):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not matrix[i, j] % n:
                return [i, j]
                
def first_divisible2(matrix, n=2):
    return np.argwhere(matrix % n == 0)[0] if len(np.argwhere(matrix % n == 0)) > 0 else None
    
def multiples_of_4(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not (i + j) % 4:
                result.append(matrix[i, j])
    return result
    
def to_array(dct):
    return np.array([dct[key] for key in sorted(dct)])
        
def to_table(csv_fname, sql_fname, tbl_name="new1"):
    csv_fp = open(csv_fname, newline='')
    reader = csv.reader(csv_fp)

    conn = sqlite3.connect(sql_fname)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    columns = next(reader)
    query = "CREATE TABLE " + tbl_name + " (" + columns[0] + " TEXT PRIMARY KEY"
    for col in columns[1:]:
        query += ', ' + col + ' TEXT'
    query += ');'
    c.execute(query)
    
    escapes = '?, ' * (len(columns) - 1) + '?'
    query = "INSERT INTO " + tbl_name + " VALUES (" + escapes + ");"
    for row in reader:
        c.execute(query, row)
        
    conn.commit()
    conn.close()
    csv_fp.close()
    
def to_csv(sql_fname, tbl_name, csv_fname="data.csv"):
    csv_fp = open(csv_fname, 'w', newline='')
    writer = csv.writer(csv_fp)

    conn = sqlite3.connect(sql_fname)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute('SELECT * FROM ' + tbl_name + ';')
    columns = [tup[0] for tup in c.description]
    writer.writerow(columns)
    for row in c.fetchall():
        writer.writerow(list(row))
    
    csv_fp.close()
    conn.close()
    
def get_students(conn, tbl, grd):
    c = conn.cursor()
    c.execute("SELECT last || ', ' || first AS name FROM " + 
      tbl + " WHERE grade = '" + grd + "' ORDER BY name;")
    return [row[0] for row in c.fetchall()]    
    
    
