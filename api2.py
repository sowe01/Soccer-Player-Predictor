'''

@app.route("/get/sofifa_id/<df>, <name>")

def sofifa_id (df,short_name): 
    return df[df["short_name"] == short_name]["sofifa_id"][0]
    '''

@app.route('/bestonce', methods=['GET'])

def insertArg():
    return '''<form method="POST" action="/bestonce">
            Insert an overall: <input name="overall"   />
            Insert a strategy: <input name="strategia"   />
            <input type="submit" />
              </form>'''

@app.route('/bestonce', methods=['POST'])
def getBest11():    
    overall = request.form.get('overall')
    strategia = request.form.get('strategia')
    resultado = q.get_best_squad(overall,strategia)
    return json.dumps(resultado)   

@app.route('/bestonce')
def getBest11():    
    overall = request.form.get('overall')
    position = request.form.get('position')
    resultado = q.get_best_squad(overall,position)
    return json.dumps(resultado)  

'''
@app.route('/edad')
def devuelvedad(overall, position, df):
    overall = 
    info = q.age()

    return json.dumps(info)

    '''
    def insertArg():
    return '''<form method="POST" action="/bestonce">
            Insert an overall: <input name="overall"   />
            Insert a position: <input name="position"   />
            <input type="submit" />
              </form>'''



@app.route('/age/<n>/<m>')
def devuelveage(n,m):
    info = q.age(n,m)
    return json.dumps(info)
