build:
	docker build --tag=docker-flask-gpu .

start:
	docker run -it -p 80:8000 docker-flask-gpu
