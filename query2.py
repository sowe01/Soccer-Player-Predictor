'''
squad_433 = ['GK', 'LI', 'DF', 'DF', 'LD', 'CM', 'CM', 'CM', 'EI', 'ST', 'ED']
squad_343 = ['GK', 'DF', 'DF', 'DF', 'CI', 'CM', 'CM', 'CD', 'EI', 'ST', 'ED']
squad_352 = ['GK', 'DF', 'DF', 'DF', 'LI', 'LD', 'CM', 'CM', 'MP', 'ST', 'ST']
squad_442 = ['GK', 'LI', 'DF', 'DF', 'LD', 'CI', 'CM', 'CM', 'CD', 'ST', 'ST']
squad_523 = ['GK', 'LI', 'DF', 'DF', 'DF', 'LD', 'CM', 'CM', 'ST', 'ST', 'ST']
squad_451 = ['GK', 'LI', 'DF', 'DF', 'LD', 'CM', 'CM', 'EI', 'MP', 'ED', 'ST']



def get_best_squad(overall, position ):
    escoge el mejor once, segun el año y la estrategia

    
    df = getdataframe()
    print(df)
    df_copy = df.copy()
    store = []
    for i in position:
        store.append([i,df_copy.loc[[df_copy[df_copy['player_positions'] == i][overall].idxmax()]]['short_name'].to_string(index = False), df_copy[df_copy['player_positions'] == i][overall].max()])
        df_copy.drop(df_copy[df_copy['player_positions'] == i][overall].idxmax(), inplace = True)
    #return store

    return pd.DataFrame(np.array(store).reshape(11,3), columns = ['Position', 'Player', 'Overall']).to_string(index = False)

def getoverall(df =getdataframe()):
    devuelve la estrategia  
    overall_15 = df['overal_15']
    overall_16 = df['overal_16']
    overall_17 = df['overal_17']
    overall_18 = df['overal_18']
    overall_19 = df['overal_19']
    overall_20 = df['overal_20']
    
    return overall'''


#getDataUser('Casillas')

'''


def age(n, m, df =getdataframe()):
    elige en un rango de edad entre n y m 
    return df[(df['age'] >= n) & (df['age'] < m)]
'''
squad_433 = ['GK', 'LI', 'DF', 'DF', 'LD', 'CM', 'CM', 'CM', 'EI', 'ST', 'ED']
squad_343 = ['GK', 'DF', 'DF', 'DF', 'CI', 'CM', 'CM', 'CD', 'EI', 'ST', 'ED']
squad_352 = ['GK', 'DF', 'DF', 'DF', 'LI', 'LD', 'CM', 'CM', 'MP', 'ST', 'ST']
squad_442 = ['GK', 'LI', 'DF', 'DF', 'LD', 'CI', 'CM', 'CM', 'CD', 'ST', 'ST']
squad_523 = ['GK', 'LI', 'DF', 'DF', 'DF', 'LD', 'CM', 'CM', 'ST', 'ST', 'ST']
squad_451 = ['GK', 'LI', 'DF', 'DF', 'LD', 'CM', 'CM', 'EI', 'MP', 'ED', 'ST']


def get_best_squad(df_name, position):
    df_copy = df_name.copy()
    store = []
    for i in position:
        store.append([i,df_copy.loc[[df_copy[df_copy['player_positions'] == i]['overall'].idxmax()]]['short_name'].to_string(index = False), df_copy[df_copy['player_positions'] == i]['overall'].max()])
        df_copy.drop(df_copy[df_copy['player_positions'] == i]['overall'].idxmax(), inplace = True)
    #return store
    return pd.DataFrame(np.array(store).reshape(11,3), columns = ['Position', 'Player', 'Overall']).to_string(index = False)

