from tensorflow/tensorflow:1.9.0-rc2-devel-gpu-py3

RUN pip install keras

ADD . .

CMD ["python", "example.py"]
