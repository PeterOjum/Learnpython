'''
hw4.py
'''

import pandas as pd, numpy as np

def csv_to_dataframe(csv_name):
    return pd.read_csv(csv_name, decimal = ',', index_col=0)
    
def format_df(df):
    df.index = df.index.str.strip() # = [idx.strip() for idx in df.index]
    df['Region'] = df['Region'].str.strip().str.title() # = [reg.strip().title() for reg in df['Region']]
    
def growth_rate(df):
    df['Growth Rate'] = df['Birthrate'] - df['Deathrate']
    
def dod(p, r):
    num_yrs = 0
    while p  > 2:
        p = p + p * r / 1000 
        num_yrs += 1
    return num_yrs
    
def years_to_extinction(df):
    df['Years to Extinction'] = np.nan
    for country in df.index:
        if df.loc[country, 'Growth Rate'] < 0:
            df.loc[country, 'Years to Extinction'] = dod( 
                df.loc[country, 'Population'], df.loc[country, 'Growth Rate'])
    
def dying_countries(df):
    return df[df['Years to Extinction'] > 0]['Years to Extinction'].sort_values()
    
def class_performance(conn, tname="ISTA_131_F17"):
    c = conn.cursor()
    c.execute('SELECT UPPER(grade), 100.0 * count(*) / (SELECT count(*) FROM ' + tname + ') FROM ' + tname + ' GROUP BY grade;')
    performance = {}
    for row in c.fetchall():
        performance[row[0]] = round(row[1],1)
    return performance
    
def improved(conn, t1name, t2name):
    c = conn.cursor()
    c.execute('SELECT ' + t1name + '.last AS name FROM ' + 
        t1name + ' INNER JOIN ' + t2name + ' ON ' + 
        t1name + '.email = ' + t2name + '.email ' + 
        'WHERE ' + t1name + '.grade < ' + t2name + 
        '.grade ORDER BY name;')
   
    return [row[0] for row in c.fetchall()]
    
def main():
    df = csv_to_dataframe('countries_of_the_world.csv')
    #df.to_pickle('all_countries0.pkkl') # delete extra 'k'
    '''
    print('-' * 20, 'Initial df:\n')
    print()
    print(df)
    '''
    format_df(df)
    #df.to_pickle('all_countries1.pkkl') # delete extra 'k'
    '''
    print('-' * 20, 'Formatted df:\n')
    print()
    print(df)
    '''
    growth_rate(df)
    #df.to_pickle('all_countries2.pkkl') # delete extra 'k'
    '''
    print('-' * 20, 'Growth rate col added to df:\n')
    print()
    print(df)
    '''
    years_to_extinction(df)
    #df.to_pickle('all_countries3.pkkl') # delete extra 'k'
    '''    
    print('-' * 20, 'Years to Extinction col added to df:\n')
    print()
    print(df)
    ''' 
    dying = dying_countries(df)
    #print(dying)
    #dying.to_pickle('dying.pkkl') # delete extra 'k'
    for i in range(5):
        print('{}: {} Years to Extinction'.format(dying.index[i], str(round(dying[i], 0))))
        
if __name__ == '__main__':
    main()