import psycopg2


class TransacaoSQL:
    con = ""
    def __init__(self):
        self.con = psycopg2.connect(host='localhost', 
                                database='vlpr',
                                user='neurotech', 
                                password='neuro2022')



    def executar(self, sql):
        cur = self.con.cursor()
        try:
            cur.execute(sql)
            self.con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.con.rollback()
            cur.close()
            return 1
        cur.close()

    def consultar( self, sql):
        con = self.con
        cur = con.cursor()
        cur.execute(sql)
        recset = cur.fetchall()
        registros = []
        for rec in recset:
            registros.append(rec)
        con.close()
        return registros

