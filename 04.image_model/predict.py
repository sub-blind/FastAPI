from tensorflow.keras.applications.imagenet_utils import decode_predictions
from PIL.Image import Image
import numpy as np
from model_loader import model


def predict(image: Image):
    image = np.asarray(image.resize((224, 224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0

    result = decode_predictions(model.predict(image), 3)[0]

    response = []

    for i, res in enumerate(result):
        response.append({"class": res[1], "confidence": f"{res[2]*100:0.2f} %"})
    return response
