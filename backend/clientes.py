
from flask import Flask
from flask_cors import CORS
from flask import Blueprint, jsonify,request
import pymysql
# app=Flask(__name__)
# CORS(app)
## Funcion para conectarnos a la base de datos de mysql
cliente_blueprint = Blueprint('clientes',__name__)
def conectar(vhost,vuser,vpass,vdb):
     conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset = 'utf8mb4')
     return conn 
       
#  tabla cLIENTE       
@cliente_blueprint.route("/clientes")
def consulta_general():
     try:
         conn=conectar('localhost','root','','emprendimiento')
         cur = conn.cursor()
         cur.execute(""" SELECT * FROM clientes """)
         #Extre todos los registros que se encuentran en el cursor cur
         datos=cur.fetchall()
         data=[]
         for row in datos:
             dato={'idcliente':row[0],'nombres':row[1],'apellidos':row[2],'telefono':row[3],'correo':row[4]}
             data.append(dato)
         cur.close()
         conn.close()
         return jsonify({'clientes':data,'mensaje':'Registros encontrados'})
     except Exception as ex:
         return jsonify({'mensaje':'Error'}) 
     
@cliente_blueprint.route("/registro_cliente/",methods=['POST'])
def registro_administrador():
    try:
        conn = conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        x = cur.execute(""" insert into clientes (idcliente,nombres,apellidos,telefono,correo) values
            ('{0}',{1},{2},{3},{4},')""".format(request.json['idcliente'],request.json['nombres'],request.json['apellidos'],request.json['telefono'],request.json['correo'],))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
    
@cliente_blueprint.route("/consulta_individual_clientes/<codigo>",methods=['GET'])
def consulta_individual(codigo):
    try:
        conn=conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM clientes where idcliente='{0}' """.format(codigo))
        datos=cur.fetchone()
        cur.close()
        conn.close()
        if datos!=None:
            dato={'idcliente':datos[0],'nombres':datos[1],'apellidos':datos[2],'telefono':datos[3],'correo':datos[3]}
            return jsonify({'cliente':dato,'mensaje':'Registro encontrado'})  
        else:
            return jsonify({'mensaje':'Registro no encontrado'})     
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
    
@cliente_blueprint.route("/eliminar_clientes/<codigo>",methods=['DELETE'])
def eliminar(codigo):
    try:
        conn=conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        x=cur.execute(""" delete from clientes where idcliente={0}""".format(codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'eliminado'}) 
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'}) 
if __name__=='__main__':
    cliente_blueprint.run(debug=True)  
     
      