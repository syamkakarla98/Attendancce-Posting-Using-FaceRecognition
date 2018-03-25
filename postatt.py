import sqlite3



def postatt(id):
    
    conn=sqlite3.connect('FaceBase.db')
    conn.execute("UPDATE people SET att=? WHERE Id=?",('Present' , id))
    conn.commit()
    conn.close()

#   conn.execute("UPDATE people SET att=? WHERE Id=?",('Present' , id))
#   conn.execute('''UPDATE people SET att = ? WHERE id = ? ''',('Present', id))
postatt(11)
