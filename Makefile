PORT 	:= 17674
SERVER  := 2.tcp.ngrok.io


sync:
	rsync -ai --exclude *idea/ --exclude *.git --exclude *.pyc --exclude *pycache*  --exclude *.pytest_cache* \
	 -a --delete $(shell pwd) -e 'ssh -p ${PORT}'  \
	 interview@${SERVER}:/home/interview/code;

ssh:
	ssh -p ${PORT} interview@${SERVER}

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

terminal:
	docker-compose run back bash 

run:
	docker run interview_concept_back

mysql: 
	docker-compose exec db mysql -upinner -ppintastic
	