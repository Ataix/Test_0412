
# Test exercise
### Python 3.11, Django 4.2, Stripe

### Задача:
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
  1. Django Модель Item с полями (name, description, price)
  2. API с двумя методами:
  * 1. GET /buy/{id} ( localhost/api/v1/item/buy/{id}/ )
  * 2. GET /item/{id} ( localhost/api/v1/item/item/{id}/ , HTML страница с простыми элементами)

### Выполненные бонусные задачи:
  1. Запуск используя Docker
  2. Использование environment variables
  3. Просмотр Django Моделей в Django Admin панели
 
#### Список эндпонтов доступен по ссылке localhost/api/schema/swagger-ui/

* Перед запуском необходимо заполнить .env.dev 
для Stripe Secret Key.

### Запуск:
    1.  docker-compose build
    2.  docker-compose up
