build:
	docker build --tag=docker-flask-gpu .

start:
	docker run -it -d -p 8000:80 docker-flask-gpu
