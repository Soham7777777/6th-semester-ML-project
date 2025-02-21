from flask_wtf import FlaskForm # type: ignore
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class WineQualityForm(FlaskForm): # type: ignore
    fixed_acidity = FloatField('Fixed Acidity', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 7.4"})
    volatile_acidity = FloatField('Volatile Acidity', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 0.7"})
    citric_acid = FloatField('Citric Acid', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 0.0"})
    residual_sugar = FloatField('Residual Sugar', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 1.9"})
    chlorides = FloatField('Chlorides', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 0.076"})
    free_sulfur_dioxide = FloatField('Free Sulfur Dioxide', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 11.0"})
    total_sulfur_dioxide = FloatField('Total Sulfur Dioxide', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 34.0"})
    density = FloatField('Density', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 0.9978"})
    pH = FloatField('pH', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 3.51"})
    sulphates = FloatField('Sulphates', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 0.56"})
    alcohol = FloatField('Alcohol', validators=[InputRequired(), NumberRange(min=0)], render_kw={"placeholder": "e.g. 9.4"})
    
    submit = SubmitField('Predict Wine Quality')
