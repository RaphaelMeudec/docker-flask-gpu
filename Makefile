build:
	docker build --tag=docker-flask-gpu .

start:
	docker run --runtime=nvidia -it -d docker-flask-gpu

start/cpu:
	docker run -it -d docker-flask-gpu
