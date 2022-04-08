"""
Cit Citas, formularios
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Optional
from citas_cliente.blueprints.distritos.models import Distrito
from citas_cliente.blueprints.oficinas.models import Oficina


def distritos_opciones():
    """Distritos: opciones para select"""
    return Distrito.query.filter_by(estatus="A").order_by(Distrito.nombre).limit(100).all()


def oficinas_opciones():
    """Oficinas: opciones para select"""
    return Oficina.query.filter_by(estatus="A").order_by(Oficina.descripcion).limit(100).all()


class CitCitaForm(FlaskForm):
    """Formulario CitCita"""

    # distritos = StringField("Distrito Judicial", validators=[DataRequired(), Length(max=256)])
    # juzgados = StringField("Juzgado o Unidad Administrativa", validators=[DataRequired(), Length(max=256)])
    distrito = QuerySelectField(label="Distrito Judicial", query_factory=distritos_opciones, get_label="nombre")
    oficina = QuerySelectField(label="Juzgado o Unidad Administrativa", query_factory=oficinas_opciones, get_label="descripcion")
    tipo_tramite = StringField("Tipo de tramite", validators=[DataRequired()])
    indicaciones_tramite = StringField("Indicaciones del tramite", validators=[Optional()])
    # fecha = DateField("Fecha", format="%Y-%m-%d", validators=[DataRequired()])
    # hora = TimeField("Hora:Minuto", format="%H:%M", validators=[DataRequired()])
    guardar = SubmitField("Guardar")
