build:
	docker build --tag=docker-flask-gpu .

start:
	docker run -it -d docker-flask-gpu
