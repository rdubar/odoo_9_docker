# Odoo 9 Easy Docker Install

Created for use with the Udemy Course 
`Mastering Odoo Development - Technical Fundamentals`:

https://www.udemy.com/course/mastering-odoo-9-development-technical-fundamentals/

Clone this code, then use Docker to easily start a working server.

```
git clone https://github.com/rdubar/odoo_9_docker.git
docker-compose up -d
```
Wait a few seconds for the service to boot, 
then point your browser at: http://localhost:8009/

It's easy to change the `odoo` and `postgres` 
versions in the configuration file, `docker-compose.yml`.

For further information, see the documentation for the 
official Odoo Docker image at: https://hub.docker.com/_/odoo

To see the names of your services, check the server logs, 
stop the server, and restart it with logging:
```
docker ps

docker-compose up -d

docker logs odoo9-web-1

docker stop odoo9-web-1
docker start -a odoo9-web-1
```