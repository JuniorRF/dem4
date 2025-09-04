# [dem4](https://демчак-резюме.рф)

### Собираю учебные проекты ЯП в один

##### Зупуск(требуется [docker compose](https://docs.docker.com/compose/install/)):

- разработка

```docker compose build && docker compose up -d```

- прод

```docker compose -f docker-compose.production.yml down && docker compose -f docker-compose.production.yml up -d```