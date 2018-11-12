build:
	docker build --tag=docker-flask-gpu .

build/gpu:
	docker build --tag=docker-flask-gpu -f Dockerfile.gpu .

lint:
	pylint api/

start:
	docker run -it -p 80:8000 docker-flask-gpu

deploy:
	docker stack deploy -c docker-compose.yml deep_api
