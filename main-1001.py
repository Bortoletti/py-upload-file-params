import psycopg2
from Logar import Logar


def conecta_db():
  con = psycopg2.connect(host='localhost', 
                         database='vlpr',
                         user='neurotech', 
                         password='neuro2022')
  return con


def inserir_db(sql):
    con = conecta_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()


appLog = Logar("main")

appLog.escrever("inicio")

nomep = "Alexandre"

sql = "insert into usuario( id_usuario, nome )";
sql += f" values( nextval('usuario_seq'), '{nomep}')"

appLog.escrever( sql )

inserir_db( sql )


sql = "update usuario set fl_ativo ='N'"
inserir_db( sql )
appLog.escrever( sql )


appLog.escrever("fim")
