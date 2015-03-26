from dataBase.DataBase import DataBase
from model.UnSerializerActivity import UnSerializerActivity
from model.UnSerializerEquipment import UnSerializerEquipment
from model.UnSerializerInstallation import UnSerializerInstallation

''' instanciates our database '''
data = DataBase()

''' tables creation '''
data.creation_table_activity()
data.creation_table_equipment()
data.creation_table_installation()

''' export json data into the dataBase '''
seri = UnSerializerActivity()
seri.unSerialize()
data.export_object_list(seri.collection)

seri = UnSerializerInstallation()
seri.unSerialize()
data.export_object_list(seri.collection)

seri = UnSerializerEquipment()
seri.unSerialize()
data.export_object_list(seri.collection)

''' commit and disconnection ''' 
data.conn.commit()
data.disconnect()