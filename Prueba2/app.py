from flask import Flask,render_template, request,url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///usuarios.db'
db=SQLAlchemy(app)

class User(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(200))
	python=db.Column(db.Boolean)
	fecha=db.Column(db.String(100))
	java=db.Column(db.Boolean)
	micro=db.Column(db.Boolean)
	elastic=db.Column(db.Boolean)

@app.route('/')
def index():
	nombres_usuarios=User.query.all()
	return render_template('index.html', name_users=nombres_usuarios)

@app.route('/add_contact',methods=['POST'])
def add_contact():
	nuevo_usuario=User(name=request.form['contenido'],
						fecha=request.form['fecha_ent'],
						python=bool(request.form.get("mycheckbox")),
						java=bool(request.form.get("mycheckbox2")),
						micro=bool(request.form.get("mycheckbox3")),
						elastic=bool(request.form.get("mycheckbox4")),
						)
	db.session.add(nuevo_usuario)
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/detalle/<id>')
def detalle_contact(id):
	dato=User.query.filter_by(id=int(id)).first()
	return render_template('usuario.html',name_users=dato)

@app.route('/delete/<id>')
def delete_contact(id):
	eliminar=User.query.filter_by(id=int(id)).delete()
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/back')
def regresar():
	return redirect(url_for('index'))

if __name__=='__main__':
	app.run(port=3000, debug=True)