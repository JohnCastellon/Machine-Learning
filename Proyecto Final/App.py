import Modelo
from flask import Flask, render_template, request,redirect, url_for, flash


app = Flask(__name__)
app.secret_key="mysecretkey"

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/prediciendo',methods=['POST'])
def prediction():
    a=request.form['Baseline Value']
    b=request.form['Accelerations']
    c=request.form['Fetal_movement']
    d=request.form['Uterine contractions']
    e=request.form['Light Deceleration']
    f=request.form['Severe deceleration']
    g=request.form['Prolongued deceleration']
    h=request.form['Abnormal short term variability']
    i=request.form['Mean value of short term variability']
    j=request.form['Percentage of time with abnormal long term variability']    

    x=[a,b,c,d,e,f,g,h,i,j]

    if Modelo.prediccion(x)==1:
        flash('Predicción: La salud del feto es normal')
        return redirect(url_for('inicio'))

    elif Modelo.prediccion(x)==2:
        flash('Predicción: La salud del feto es sospechosa')
        return redirect(url_for('inicio'))

    elif Modelo.prediccion(x)==3:
        flash('Predicción: Se ha detectado que el feto sufre una patologia')
        return redirect(url_for('inicio'))

if __name__=='__main__':
    app.run(port=3000,debug=True)

