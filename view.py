from rami import app, db
from flask import url_for, render_template
import os
from forms import DataForm
from model import Data


@app.route('/', methods=['GET','POST'])
def index():
    form = DataForm()

    last_message = db.session.query(Data).order_by(Data.id.desc()).first()
    form.last_message.data = str(last_message.message)
    print ("last message: " + str(last_message.message))

    if form.validate_on_submit:
        if form.message.data:
            print (form.message.data)

            msg = Data(form.message.data)
            db.session.add(msg)
            db.session.commit()
            
    return render_template('index.html', form=form)