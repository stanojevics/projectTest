@app.route('/api/validate/', methods = ['POST', 'GET'])
def validateRoute():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['user'])
        POST_PASSWORD = str(request.form['password'])
        if check_for_user(POST_USERNAME, POST_PASSWORD) == True:
            session['logged_in'] = True
            user_id = get_user_id(POST_USERNAME, POST_PASSWORD)
            return jsonify({"Status":"ok", "Route":url_for('home'), "user_id": user_id})
        else:
            print ('wrong')
            flash('wrong password!')
            return 'wrong password'
    elif request.method == 'GET':
        if session['logged_in'] == True:
            return redirect(url_for('home'))
        
       