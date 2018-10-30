build:
	docker build --tag=docker-flask-gpu .

start:
	docker run -it -d -p 80:8000 docker-flask-gpu
