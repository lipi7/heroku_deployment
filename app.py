from flask import Flask,render_template,request
import joblib
#__name__ is for when we run this file it tells it is executed as module or as a direct file
app = Flask(__name__)

model = joblib.load('dib_79.pkl')
print('[INFO] model loaded')




#127.0.0.1:5000/
#17.0.0.1 is the ip address
#here 500 is the port number
#/ is the route
#here we have not mentioned what will we do when we route at this
#so at the backend we should mention what should we do 
#to do this we use decorator @

@app.route('/')
def hello_world():
    return render_template('dib_ip.html')

@app.route('/predict',methods=['post'])
def predict():

    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    

    #save in database
    print(type(preg))
    print(type(plas))

    print(preg)
    print(plas)
    print(pres)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)
    

    output = model.predict([[int(preg), int(plas),int(pres), int(skin), int(test),int(mass),int(pedi),int(age)]])
    if output[0] == 1:
        ans = 'diabetic'
    else:
        ans = 'Not Diabetic'


    return render_template('home.html', predict = f'the person is:{ans}')
    


#run the app
if __name__ == '__main__':
    app.run(debug=True)

