build:
	docker build --tag=docker-flask-gpu .

build/gpu:
	docker build --tag=docker-flask-gpu -f Dockerfile.gpu .

start:
	docker run -it -p 80:8000 docker-flask-gpu
