from application.database import db

user_permissions = db.Table('userpermissions',
	db.Column('userid', db.Integer, db.ForeignKey('user.id')),
	db.Column('permissionid', db.Integer, db.ForeignKey('permission.id'))
)