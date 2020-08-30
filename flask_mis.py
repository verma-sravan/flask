# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:58:31 2020

@author: Sravan
"""  
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
   return render_template('mis.html')
@app.route('/action_performed',methods = ['POST', 'GET'])
def action_performed():
    if request.method == 'POST':
        data = request.form
        action=request.form.get('action')
        startdate=request.form.get('startdate')
        enddate=request.form.get('enddate')
        print(action)
        print(startdate)
        print(enddate)
        if action=='freq_raw_data_creation':
            print('Call index file of raw freq generation')
        elif action=='vol_raw_data_creation':
            print('call index file of voltage raw generation function')
        elif action=='freq_derived_data_creation':
            print('call index file of freq derived data creation function')
        elif action=='Vol_derived_data_creation':
            print('call index file of voltage derived data creation file')
        else:
            print('do nothing')

    return render_template("resultmis.html",data = data)

if __name__ == '__main__':
   app.run(debug = False)