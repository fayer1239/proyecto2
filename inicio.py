
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/area')
def area():
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
 cursor = conn.cursor()
 cursor.execute('select idArea, descripcion from area order by idArea')
 datos = cursor.fetchall()
 return render_template("area.html", area = datos)
@app.route('/carrera')
def carrera():
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
 cursor = conn.cursor()
 cursor.execute('select idCarrera, descripcion from carrera order by idCarrera')
 datos = cursor.fetchall()
 return render_template("carrera.html", carrera = datos)
@app.route('/escolaridad')
def escolaridad():
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
 cursor = conn.cursor()
 cursor.execute('select idEscolaridad, descripcion from escolaridad order by idEscolaridad')
 datos = cursor.fetchall()
 return render_template("escolaridad.html", escolaridad = datos)
@app.route('/estadoCivil')
def estadocivil():
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
 cursor = conn.cursor()
 cursor.execute('select idEstadoCivil, descripcion from estadocivil order by idEstadoCivil')
 datos = cursor.fetchall()
 return render_template("estadocivil.html", estadocivil = datos)
@app.route('/gradoAvance')
def gradoavance():
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
 cursor = conn.cursor()
 cursor.execute('select idGradoAvance, descripcion from gradoavance order by idGradoAvance')
 datos = cursor.fetchall()
 return render_template("gradoavance.html", gradoavance = datos)
@app.route('/habilidad')
def habilidad():
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
 cursor = conn.cursor()
 cursor.execute('select idHabilidad, descripcion from habilidad order by idHabilidad')
 datos = cursor.fetchall()
 return render_template("habilidad.html", habilidad = datos)
@app.route('/idioma')
def idioma():
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
 cursor = conn.cursor()
 cursor.execute('select idIdioma, descripcion from idioma order by idIdioma')
 datos = cursor.fetchall()
 return render_template("idioma.html", idioma = datos)                 

@app.route('/area_editar/<string:id>')
def area_editar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('select idArea, descripcion from area where idArea = %s', (id))
 dato = cursor.fetchall()
 return render_template("area_edi.html", area=dato[0])
@app.route('/carrera_editar/<string:id>')
def carrera_editar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('select idCarrera, descripcion from carrera where idCarrera = %s', (id))
 dato = cursor.fetchall()
 return render_template("carrera_edi.html", carrera=dato[0])
@app.route('/escolaridad_editar/<string:id>')
def escolaridad_editar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('select idEscolaridad, descripcion from escolaridad where idEscolaridad = %s', (id))
 dato = cursor.fetchall()
 return render_template("escolaridad_edi.html", escolaridad=dato[0])
@app.route('/estadocivil_editar/<string:id>')
def estadocivil_editar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('select idEstadoCivil, descripcion from estadocivil where idEstadoCivil = %s', (id))
 dato = cursor.fetchall()
 return render_template("estadocivil_edi.html", estadocivil=dato[0])
@app.route('/gradoavance_editar/<string:id>')
def gradoavance_editar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('select idGradoAvance, descripcion from gradoavance where idGradoAvance = %s', (id))
 dato = cursor.fetchall()
 return render_template("gradoavance_edi.html", gradoavance=dato[0])
@app.route('/habilidad_editar/<string:id>')
def habilidad_editar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('select idHabilidad, descripcion from habilidad where idHabilidad = %s', (id))
 dato = cursor.fetchall()
 return render_template("habilidad_edi.html", habilidad=dato[0])
@app.route('/idioma_editar/<string:id>')
def idioma_editar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('select idIdioma, descripcion from idioma where idIdioma = %s', (id))
 dato = cursor.fetchall()
 return render_template("idioma_edi.html", idioma=dato[0])

@app.route('/area_fedita/<string:id>',methods=['POST'])
def area_fedita(id):
 if request.method == 'POST':
    desc=request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('update area set descripcion=%s where idArea=%s', (desc,id))
    conn.commit()
 return redirect(url_for('area'))
@app.route('/carrera_fedita/<string:id>',methods=['POST'])
def carrera_fedita(id):
 if request.method == 'POST':
    desc=request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('update carrera set descripcion=%s where idCarrera=%s', (desc,id))
    conn.commit()
 return redirect(url_for('carrera'))
@app.route('/escolaridad_fedita/<string:id>',methods=['POST'])
def escolaridad_fedita(id):
 if request.method == 'POST':
    desc=request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('update escolaridad set descripcion=%s where idEscolaridad=%s', (desc,id))
    conn.commit()
 return redirect(url_for('escolaridad'))
@app.route('/estadocivil_fedita/<string:id>',methods=['POST'])
def estadocivil_fedita(id):
 if request.method == 'POST':
    desc=request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()   
    cursor.execute('update estadocivil set descripcion=%s where idEstadoCivil=%s', (desc,id))
    conn.commit()
 return redirect(url_for('estadocivil'))
@app.route('/gradoavance_fedita/<string:id>',methods=['POST'])
def gradoavance_fedita(id):
 if request.method == 'POST':
    desc=request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('update gradoavance set descripcion=%s where idGradoAvance=%s', (desc,id))
    conn.commit()
 return redirect(url_for('gradoavance'))
@app.route('/habilidad_fedita/<string:id>',methods=['POST'])
def habilidad_fedita(id):
 if request.method == 'POST':
    desc=request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('update habilidad set descripcion=%s where idHabilidad=%s', (desc,id))
    conn.commit()
 return redirect(url_for('habilidad'))
@app.route('/idioma_fedita/<string:id>',methods=['POST'])
def idioma_fedita(id):
 if request.method == 'POST':
    desc=request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('update idioma set descripcion=%s where iIdioma=%s', (desc,id))
    conn.commit()
 return redirect(url_for('idioma'))

@app.route('/area_borrar/<string:id>')
def area_borrar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('delete from area where idArea = {0}'.format(id))
 conn.commit()
 return redirect(url_for('area'))
@app.route('/carrera_borrar/<string:id>')
def carrera_borrar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('delete from carrera where idCarrera = {0}'.format(id))
 conn.commit()
 return redirect(url_for('carrera'))
@app.route('/escolaridad_borrar/<string:id>')
def escolaridad_borrar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('delete from escolaridad where idEscolaridad = {0}'.format(id))
 conn.commit()
 return redirect(url_for('escolaridad'))
@app.route('/estadocivil_borrar/<string:id>')
def estadocivil_borrar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('delete from estadocivil where idEstadoCivil = {0}'.format(id))
 conn.commit()
 return redirect(url_for('estadocivil'))
@app.route('/gradoavance_borrar/<string:id>')
def gradoavance_borrar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('delete from gradoavance where idGradoAvance = {0}'.format(id))
 conn.commit()
 return redirect(url_for('gradoavance'))
@app.route('/habilidad_borrar/<string:id>')
def habilidad_borrar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('delete from habilidad where idHabilidad = {0}'.format(id))
 conn.commit()
 return redirect(url_for('habilidad'))
@app.route('/idioma_borrar/<string:id>')
def idioma_borrar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('delete from idioma where idIdioma = {0}'.format(id))
 conn.commit()
 return redirect(url_for('idioma'))
@app.route('/area_agregar')
def area_agregar():
 return render_template("area_agr.html")
@app.route('/carrera_agregar')
def carrera_agregar():
 return render_template("carrera_agr.html")
@app.route('/escolaridad_agregar')
def escolaridad_agregar():
 return render_template("escolaridad_agr.html")
@app.route('/estadocivil_agregar')
def estadocivil_agregar():
 return render_template("estadocivil_agr.html")
@app.route('/gradoavance_agregar')
def gradoavance_agregar():
 return render_template("gradoavance_agr.html")
@app.route('/habilidad_agregar')
def habilidad_agregar():
 return render_template("habilidad_agr.html")
@app.route('/idioma_agregar')
def idioma_agregar():
 return render_template("idioma_agr.html")
@app.route('/area_fagrega', methods=['POST'])
def area_fagrega():
 if request.method == 'POST':
    desc = request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('insert into area (descripcion) values (%s)',(desc))
    conn.commit()
 return redirect(url_for('area'))
@app.route('/carrera_fagrega', methods=['POST'])
def carrera_fagrega():
 if request.method == 'POST':
    desc = request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('insert into carrera (descripcion) values (%s)',(desc))
    conn.commit()
 return redirect(url_for('carrera'))
@app.route('/escolaridad_fagrega', methods=['POST'])
def escolaridad_fagrega():
 if request.method == 'POST':
    desc = request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('insert into escolaridad (descripcion) values (%s)',(desc))
    conn.commit()
 return redirect(url_for('escolaridad'))
@app.route('/estadocivil_fagrega', methods=['POST'])
def eestadocivil_fagrega():
 if request.method == 'POST':
    desc = request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('insert into estadocivil (descripcion) values (%s)',(desc))
    conn.commit()
 return redirect(url_for('estadocivil'))
@app.route('/gradoavance_fagrega', methods=['POST'])
def gradoavance_fagrega():
 if request.method == 'POST':
    desc = request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('insert into gradoavance (descripcion) values (%s)',(desc))
    conn.commit()
 return redirect(url_for('gradoavance'))
@app.route('/habilidad_fagrega', methods=['POST'])
def habilidad_fagrega():
 if request.method == 'POST':
    desc = request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('insert into habilidad (descripcion) values (%s)',(desc))
    conn.commit()
 return redirect(url_for('habilidad'))
@app.route('/idioma_fagrega', methods=['POST'])
def idioma_fagrega():
 if request.method == 'POST':
    desc = request.form['descripcion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('insert into idioma (descripcion) values (%s)',(desc))
    conn.commit()
 return redirect(url_for('idioma'))

@app.route('/puesto')
def puesto():
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
 cursor = conn.cursor()
 cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
 datos = cursor.fetchall()
 return render_template("puestos.html", pue=datos, dat=' ', catArea=' ', catEdoCivil=' ',catEscolaridad=' ',catGradoAvance=' ', catCarrera=' ', catIdioma=' ', catHabilidad=' ')

@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
 datos = cursor.fetchall()
 cursor.execute('select idPuesto, codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
 dato = cursor.fetchall()
 cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
 datos1 = cursor.fetchall()
 cursor.execute('select a.idEstadoCivil, a.descripcion from estadocivil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s', (idP))
 datos2 = cursor.fetchall()
 cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idP))
 datos3 = cursor.fetchall()
 cursor.execute('select a.idGradoAvance, a.descripcion from gradoavance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s', (idP))
 datos4 = cursor.fetchall()
 cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera =b.idCarrera and b.idPuesto = %s', (idP))
 datos5 = cursor.fetchall()
 cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b,puesto_has_idioma c where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s',(idP))
 datos6 = cursor.fetchall()
 cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b,puesto_has_habilidad c where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto =%s', (idP))
 datos7 = cursor.fetchall()
 return render_template("puestos.html", pue = datos, dat=dato[0], catArea=datos1[0],catEdoCivil=datos2[0],catEscolaridad=datos3[0],catGradoAvance=datos4[0],catCarrera=datos5[0],catIdioma=datos6,catHabilidad=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('delete from puesto where idPuesto = %s',(idP))
 conn.commit()
 cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
 conn.commit()
 cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
 conn.commit()
 return redirect(url_for('puesto'))
@app.route('/puesto_agregar')
def puesto_agregar():
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('select idArea, descripcion from area ')
 datos1 = cursor.fetchall()
 cursor.execute('select idEstadoCivil, descripcion from estadocivil ')
 datos2 = cursor.fetchall()
 cursor.execute('select idEscolaridad, descripcion from escolaridad ')
 datos3 = cursor.fetchall()
 cursor.execute('select idGradoAvance, descripcion from gradoavance ')
 datos4 = cursor.fetchall()
 cursor.execute('select idCarrera, descripcion from carrera ')
 datos5 = cursor.fetchall()
 cursor.execute('select idIdioma, descripcion from idioma ')
 datos6 = cursor.fetchall()
 cursor.execute('select idHabilidad, descripcion from habilidad ')
 datos7 = cursor.fetchall()
 return render_template("puestos_agr.html", catArea=datos1, catEdoCivil=datos2,
catEscolaridad=datos3, catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6,
catHabilidad=datos7)
@app.route('/puesto_fagrega', methods=['POST'])
def puesto_fagrega():
 if request.method == 'POST':
  codP = request.form['codPuesto']
  if 'idArea' in request.form:
    idAr = request.form['idArea']
  else:
    idAr = '1'
  nomP = request.form['nomPuesto']
  pueJ = request.form['puestoJefeSup']
  jorn = request.form['jornada']
  remu = request.form['remunMensual']
  pres = request.form['prestaciones']
  desc = request.form['descripcionGeneral']
  func = request.form['funciones']
  eda = request.form['edad']
  if 'sexo' in request.form:
    sex = request.form['sexo']
  else:
    sex = '1'
  if 'idEstadoCivil' in request.form:
    idEC = request.form['idEstadoCivil']
  else:
    idEC = '1'
  if 'idEscolaridad' in request.form:
    idEs = request.form['idEscolaridad']
  else:
    idEs = '1'
  if 'idGradoAvance' in request.form:
    idGA = request.form['idGradoAvance']
  else:
    idGA = '1'
  if 'idCarrera' in request.form:
    idCa = request.form['idCarrera']
  else:
    idCa = '1'
  expe = request.form['experiencia']
  cono = request.form['conocimientos']
  manE = request.form['manejoEquipo']
  reqF = request.form['reqFisicos']
  reqP = request.form['reqPsicologicos']
  resp = request.form['responsabilidades']
  conT = request.form['condicionesTrabajo']
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
 cursor = conn.cursor()
 cursor.execute('insert into puesto(codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa,expe, cono, manE, reqF, reqP, resp, conT))
 conn.commit()
 cursor.execute('select idPuesto, nomPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
 dato=cursor.fetchall()
 idpue = dato[0]
 idP = idpue[0]
 cursor.execute('select count(*) from idioma ')
 dato = cursor.fetchall()
 nidio = dato[0]
 ni = nidio[0] + 1
 for i in range(1, ni):
    idio = 'i' + str(i)
    if idio in request.form:
       cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP,i))
 conn.commit()
 cursor.execute('select count(*) from habilidad ')
 dato = cursor.fetchall()
 nhab = dato[0]
 nh = nhab[0] + 1
 for i in range(1, nh):
    habi = 'h' + str(i)
    if habi in request.form:
       cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)',(idP, i))
 conn.commit()
 return redirect(url_for('puesto'))

@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
        'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
        'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estadocivil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from gradoavance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s',
                   (idP))
    datos11 = cursor.fetchall()

    cursor.execute(
        'select a.idEstadoCivil, a.descripcion from estadocivil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s',
        (idP))
    datos12 = cursor.fetchall()

    cursor.execute(
        'select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s',
        (idP))
    datos13 = cursor.fetchall()

    cursor.execute(
        'select a.idGradoAvance, a.descripcion from gradoavance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s',
        (idP))
    datos14 = cursor.fetchall()

    cursor.execute(
        'select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s',
        (idP))
    datos15 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos16 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos17 = cursor.fetchall()

    return render_template("puesto_edi.html", dat=dato[0], catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7,
                           Area=datos11[0], EdoCivil=datos12[0], Escolaridad=datos13[0], GradoAvance=datos14[0],
                           Carrera=datos15[0], Idioma=datos16, Habilidad=datos17)

@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        if 'idGradoAvance' in request.form:
            idGA = request.form['idGradoAvance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        codP = request.form['codPuesto']
        idAr = request.form['idArea']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        sex = request.form['sexo']
        idEC = request.form['idEstadoCivil']
        idEs = request.form['idEscolaridad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('update puesto set codPuesto = %s, idArea = %s, nomPuesto = %s, puestoJefeSup = %s, jornada = %s, '
                   'remunMensual = %s, prestaciones = %s, descripcionGeneral = %s, funciones = %s, edad = %s, sexo = %s, '
                   'idEstadoCivil = %s, idEscolaridad = %s, idGradoAvance = %s, idCarrera = %s, experiencia = %s, '
                   'conocimientos = %s, manejoEquipo = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, '
                   'condicionesTrabajo = %s where idPuesto = %s', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda,
                   sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('select idPuesto, nomPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato=cursor.fetchall()
    idpue = dato[0]
    idP = idpue[0]
    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1
    for i in range(1, ni):
       idio = 'i' + str(i)
       if idio in request.form:
          cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP,i))
    conn.commit()
    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh = nhab[0] + 1
    for i in range(1, nh):
       habi = 'h' + str(i)
       if habi in request.form:
          cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)',(idP, i))
    conn.commit()
    return redirect(url_for('puesto'))
@app.route('/requision')
def requision():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
   cursor = conn.cursor()
   cursor.execute('select idArea, descripcion from area')
   datos1 = cursor.fetchall()
   cursor.execute('select idPuesto, nomPuesto from puesto')
   datos2 = cursor.fetchall()
   return render_template("requision.html",catArea = datos1, catPuesto = datos2)
@app.route('/requision_pagrega',methods=['POST'])
def requision_pagrega():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
   cursor = conn.cursor()
   if request.method == 'POST':
      fol=request.form['inputfolio']
      if 'idArea' in request.form:
       idAr = request.form['idArea']
      else:
       idAr = '1'
      fee=request.form['inputfecha']
      if 'idPuesto' in request.form:
        idPu = request.form['idPuesto']
      else:
        idPu = '1'
      nomSoli = request.form['nomSolicita']
      fecEl = request.form['fechaInicVac']
      fecRe = request.form['fechaRecluta']
      motRe = request.form['motivoRequisicion']
      motEs = request.form['motivoEspecifique']
      tipVa = request.form['tipoVacante']
      
   

   cursor.execute('insert into requisicion(folio,idArea,fechaElab,idPuesto,nomSolicita,fechaInicVac,fechaRecluta,motivoRequisicion,motivoEspecifique,tipoVacante) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(fol,idAr,fee,idPu,nomSoli,fecEl,fecRe,motRe,motEs,tipVa))
   conn.commit()
   return redirect(url_for('requision'))

@app.route('/requisiciones_pendientes')
def requisiciones_pendientes():
    conexion = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conexion.cursor()

    cursor.execute(
        'SELECT a.idRequisicion, a.folio, b.NomPuesto FROM requisicion a, puesto b WHERE '
        'a.idPuesto = b.idPuesto AND a.autorizada =! %s', ('1'))
    datoRequisicion = cursor.fetchall()

    return render_template("requisicionna.html", requisicion=datoRequisicion,RequisicionDatos='', AreaDatos='', PuestoDatos='', EstadoCivilDatos='',EscolaridadDatos='')
      
@app.route('/requisicion_detalles/<string:idRequisicion>', methods=['GET'])
def requisicion_detalle(idRequisicion):
    conexion = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT a.idRequisicion, a.folio, b.NomPuesto FROM requisicion a, puesto b WHERE '
        'a.idPuesto = b.idPuesto AND a.autorizada=! %s', ('1'))
    datoRequisicion = cursor.fetchall()

    cursor.execute('SELECT a.idarea, a.descripcion FROM area a, requisicion b WHERE '
                   'a.idarea = b.idArea AND b.idRequisicion = %s', (idRequisicion))
    datosArea = cursor.fetchall()

    cursor.execute(
        'SELECT * FROM requisicion WHERE idRequisicion =%s', (idRequisicion))
    datosRequisicion = cursor.fetchall()

    cursor.execute('SELECT a.* FROM puesto a, requisicion b WHERE a.idPuesto = b.idPuesto '
                   'AND b.idRequisicion = %s', (idRequisicion))
    datosPuesto = cursor.fetchall()

    datoPuesto = datosPuesto[0]
    idPuesto = datoPuesto[0]

    cursor.execute('SELECT a.idEstadoCivil, a.descripcion FROM estadocivil a, puesto b WHERE '
                   'a.idEstadoCivil = b.idEstadoCivil AND b.idPuesto = %s', (idPuesto))
    datosEstadoCivil = cursor.fetchall()

    cursor.execute('SELECT a.idEscolaridad, a.descripcion FROM escolaridad a, puesto b WHERE '
                   'a.idEscolaridad = b.idEscolaridad AND b.idPuesto = %s', (idPuesto))
    datosEscolaridad = cursor.fetchall()

    return render_template("requisicionna.html", requisicion=datoRequisicion,RequisicionDatos=datosRequisicion[0], AreaDatos=datosArea[0],PuestoDatos=datosPuesto[0], EstadoCivilDatos=datosEstadoCivil[0],EscolaridadDatos=datosEscolaridad[0])
@app.route('/autorizar_requisicion/<string:idRequisicion>')
def autorizar_requisicion(idRequisicion):
    conexion = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conexion.cursor()
    cursor.execute('SELECT a.idRequisicion, a.folio, b.NomPuesto FROM requisicion a, puesto b '
                   'WHERE a.idPuesto = b.idPuesto AND a.idRequisicion = %s', (idRequisicion))
    datosAutorizar = cursor.fetchall()
    return render_template("autorizar.html", AutorizarDatos=datosAutorizar[0])
@app.route('/requisicion_autorizar/<string:idRequisicion>', methods=['POST'])
def requisicion_autorizar(idRequisicion):
    if request.method == 'POST':
        NombreRevisado = request.form['revizado']
        NombreAutorizado = request.form['autorizada']

        conexion = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conexion.cursor()

        cursor.execute('UPDATE requisicion SET nomRevisa = %s, nomAutoriza = %s, autorizada = %s '
                       'WHERE idRequisicion = %s', (NombreRevisado, NombreAutorizado, '1', idRequisicion))
        conexion.commit()
    return redirect(url_for('requisiciones_autorizadas'))
@app.route('/borrar_requisicion/<string:idRequisicion>')
def borrar_requisicion(idRequisicion):
    conexion = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conexion.cursor()

    cursor.execute('DELETE FROM requisicion WHERE idRequisicion  = %s', (idRequisicion))
    conexion.commit()

    return (redirect(url_for('requisiciones_pendientes')))
   
@app.route('/requisiciones_autorizadas')
def requisiciones_autorizadas():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='rh3')
    cursor = conexion.cursor()

    cursor.execute(
        'SELECT a.idRequisicion, a.folio, b.NomPuesto FROM requisicion a, puesto b WHERE '
        'a.idPuesto = b.idPuesto AND a.autorizada =! %s', ('0'))
    datoRequisicion = cursor.fetchall()

    return render_template("autorizadas.html", requisicion=datoRequisicion,RequisicionDatos='', AreaDatos='', PuestoDatos='', EstadoCivilDatos='',EscolaridadDatos='')
if __name__ == "__main__":
 app.run(debug=True)