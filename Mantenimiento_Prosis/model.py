from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:CAPUFE@localhost/mantenimiento'
db = SQLAlchemy(app)


class Usuarios(db.Model):

    __tablename__ = 'Usuarios'

    Id = db.Column(db.Integer, primary_key = True)
    UserName = db.Column(db.String(80), unique = True)
    Email = db.Column(db.String(120), unique = True)


class CatalogoRefacciones(db.Model):

    __tablename__ = 'CatalogoRefacciones'

    NoParte = db.Column(db.String(50), primary_key = True, nullable = False)
    TipoServicio = db.Column(db.String(25), nullable = False) 
    Nombre = db.Column(db.String(25), nullable = False)
    Marca = db.Column(db.String(25), nullable = False)
    Precio = db.Column(db.Float, nullable = False)
    Unidad = db.Column(db.Integer, nullable = False)
    YearPieza = db.Column(db.String(5), nullable = False)
    ImagenRefaccion = db.Column(db.Text, nullable = True)       
    Descripcion = db.Column(db.Text, nullable = True)


class CatalogoCarriles(db.Model):

    __tablename__ = 'CatalogoCarriles'

    NoCapufeLane = db.Column(db.Integer, primary_key = True, unique = True)
    Lane = db.Column(db.String(4), nullable = False, unique = False)
    TipoLane = db.Column(db.String(15), nullable = False)

    PlazaId = db.Column(db.Integer, db.ForeignKey('CatalogoPlazas.NoPlaza'), nullable = False )
    Plaza = relationship("CatalogoPlazas", back_populates = "CatalogoPlazas")


class CatalogoPlazas(db.Model):

    __tablename__ = 'CatalogoPlazas'
    
    NoPlaza = db.Column(db.Integer, primary_key = True, unique = True)
    NombrePlaza = db.Column(db.String(20), nullable = False)
    Delegacion = db.Column(db.String(20), nullable = False)


class DTCEncabezado(db.Model):

    __tablename__ = 'DTCEncabezado'

    Id = db.Column(db.Integer, primary_key = True, unique = True)
    NoConvenio = db.Column(db.Integer, nullable = False)
    NombreEncargado = db.Column(db.String(20), nullable = False)
    Cargo = db.Column(db.String(20), nullable = False)




class DTCTecnico(db.Model):

    __tablename__ = 'DTCTecnico'   

    NoReferencia = db.Column(db.String(10), primary_key = True, nullable = False)

    CarrilId = db.Column(db.Integer, db.ForeignKey('CatalogoCarriles.NoCapufeLane'), nullable = False)
    Carril = relationship("CatalogoCarriles",  back_populates = "CatalogoCarriles")

    UsuarioId = db.Column(db.Integer, db.ForeignKey('Usuarios.Id'), nullable = False)
    Usuarios = relationship("Usuarios",  back_populates = "Usuarios")

    ConvenioId = db.Column(db.Integer, db.ForeignKey('DTCEncabezado.Id'), nullable = False)
    Convenio = relationship("DTCEncabezado",  back_populates = "DTCEncabezado")

    RefaccionId = db.Column(db.String(50), db.ForeignKey('CatalogoRefacciones.NoParte'), nullable = False)
    Refaccion = relationship("CatalogoRefacciones",  back_populates = "CatalogoRefacciones")

    NoAXA = db.Column(db.String(8), unique = True)
    FolioFalla = db.Column(db.Integer, unique = True)
    Estatus = db.Column(db.String(30))
    DateFalla = db.Column(db.DateTime)
    DateSiniestro = db.Column(db.DateTime)
    DateElaboracion = db.Column(db.DateTime)
    DateEnvio = db.Column(db.DateTime)
    TipoDictamen = db.Column(db.String(20))
    Descripcion = db.Column(db.Text)
    Diagnostico = db.Column(db.String(30))
    Observacion = db.Column(db.Text)
    Imagen = db.Column(db.Text)



