# Odoo 9

https://hub.docker.com/_/odoo

See `docker-compose.yml` for setup.
```
docker-compose up -d

docker logs odoo9-web-1

docker stop odoo9-web-1
docker start -a odoo9-web-1
```
Use `-a` with `start` to show logging info.