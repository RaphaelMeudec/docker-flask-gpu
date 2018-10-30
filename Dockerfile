from tensorflow/tensorflow:1.9.0-gpu-py3

RUN pip install keras

ADD . .

CMD ["python", "api/app.py"]
