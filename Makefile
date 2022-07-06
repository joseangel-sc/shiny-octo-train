build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

terminal:
	docker-compose run back bash 

mysql: 
	docker-compose exec db mysql -uadminuser -pfantastic
	
