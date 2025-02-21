import numpy as np
from app.forms import WineQualityForm
from flask import render_template, request
from app import scaler, model


sample_data = {
        "fixed_acidity": 7.4, "volatile_acidity": 0.7, "citric_acid": 0.0,
        "residual_sugar": 1.9, "chlorides": 0.076, "free_sulfur_dioxide": 11.0,
        "total_sulfur_dioxide": 34.0, "density": 0.9978, "pH": 3.51,
        "sulphates": 0.56, "alcohol": 9.4
}


def predict() -> str:
    prediction = None

    if request.args.get("sample") == "true":
        form = WineQualityForm(data=sample_data)
    else:
        form = WineQualityForm()
    
    if form.validate_on_submit():
        features = np.array([
            form.fixed_acidity.data, form.volatile_acidity.data, form.citric_acid.data,
            form.residual_sugar.data, form.chlorides.data, form.free_sulfur_dioxide.data,
            form.total_sulfur_dioxide.data, form.density.data, form.pH.data,
            form.sulphates.data, form.alcohol.data
        ]).reshape(1, -1)

        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
    
    return render_template("form.html", form=form, prediction=prediction)
