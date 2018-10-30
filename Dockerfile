from tensorflow/tensorflow:1.9.0-gpu-py3

ADD . .

RUN pip install -r requirements.txt

CMD ["python", "api/app.py"]
