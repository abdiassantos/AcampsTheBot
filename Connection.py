import postgresql as psql

class Connection(object):
    _db = None

    def __init__(self, banco):
        self._db = psql.open(banco)

    def manipulate(self, sql):
        try:
            self._db.execute(sql)
        except:
            return False
        return True

    def consult(self, sql):
        rs = None
        try:
            rs = self._db.prepare(sql)
        except:
            return None
        return rs

    def nextPk(self, table, key):
        sql = 'select max(' + key + ') from' + table
        rs = self.consultar(sql)
        pk = rs.first()
        return pk + 1

    def close(self):
        self._db.close()