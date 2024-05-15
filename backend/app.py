from flask import Flask
from flask_cors import CORS
from flask import jsonify,request
import pymysql
app=Flask(__name__)
CORS(app)
## Funcion para conectarnos a la base de datos de mysql
def conectar(vhost,vuser,vpass,vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset = 'utf8mb4')
    return conn
@app.route("/")
def consulta_general():
    try:
        conn=conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM Tipo_Usuario """)
        #Extre todos los registros que se encuentran en el cursor cur
        datos=cur.fetchall()
        data=[]
        for row in datos:
            dato={'idTipo_Usuario':row[0],'nombre':row[1]}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify({'Tipo_Usuario':data,'mensaje':'Registros encontrados'})
    except Exception as ex:
        return jsonify({'mensaje':'Error'})






@app.route("/consulta_usuario/<id>",methods=['GET'])
def consulta_usuario(id):
    try:
        conn=conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM Tipo_usuario where nombre='{1}' """.format(id))
        datos=cur.fetchone()
        cur.close()
        conn.close()
        if datos!=None:
            dato={'idTipo_usuario':datos[0],'nombre':datos[1],}
        else:
            return jsonify({'mensaje':'Registro no encontrado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})




@app.route("/registro_usuario/",methods=['POST'])
def registro_usuario():
    try:
        conn = conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        x = cur.execute("""insert into Tipo_Usuario  ( idTipo_Usuario,nombre) values  
           ('{0}',{1})""".format(request.json[' idTipo_Usuario'],
               request.json['nombre']))
        conn.commit() ## Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'}) 
    except Exception as ex:
         print(ex)
         return jsonify({'mensaje':'Error'})
        
# @app.route("/re/",methods=['POST'])         

         

