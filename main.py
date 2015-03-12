from dataBase.DataBase import DataBase
from model.UnSerializerActivity import UnSerializerActivity
from model.UnSerializerEquipment import UnSerializerEquipment
from model.UnSerializerInstallation import UnSerializerInstallation

''' instanciates our database '''
data = DataBase()
data.connect()

''' tables creation '''
data.creationTableActivity()
data.creationTableEquipment()
data.creationTableInstallation()

''' export json data into the dataBase '''
seri = UnSerializerActivity()
seri.unSerialize()
data.exportObjectList(seri.collection)

seri = UnSerializerEquipment()
seri.unSerialize()
data.exportObjectList(seri.collection)

seri = UnSerializerInstallation()
seri.unSerialize()
data.exportObjectList(seri.collection)

''' commit and disconnection ''' 
data.conn.commit()
data.disconnect()