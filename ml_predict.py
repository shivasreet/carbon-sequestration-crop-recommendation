import pandas as pd


def predict_crop(
        model,
        encoders,
        target_encoder,
        soil,
        water):


    data = pd.DataFrame({

        "Suitable_Soil": [soil],
        "Water_Requirement": [water]

    })


    for column in data.columns:

        data[column] = encoders[column].transform(
            data[column].astype(str)
        )


    prediction = model.predict(data)


    crop = target_encoder.inverse_transform(
        prediction
    )


    return crop[0]