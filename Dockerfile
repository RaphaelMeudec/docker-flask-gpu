from tensorflow/tensorflow:1.9.0-gpu-py3

ADD . .

RUN pip install -r requirements/requirements-cpu.txt

CMD ["python", "api/app.py"]
