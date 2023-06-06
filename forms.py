from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField



class DateForm(FlaskForm):
	amount_money = StringField(" Введіть вашу сумму :  ")
	submit = SubmitField("Порахувати")