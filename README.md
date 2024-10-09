# flask-prometheus
1. Соберите Docker-образ, используя содержимое папки app. 
2. Загрузите собранный образ в docker-репозиторий.
3. В манифесте k8s/app/pod.yml, в параметре "image:" отредактируйте путь к Docker-образу. 
4. Разверните приложение в Kubernetes, используя содержимое папки k8s/app.
5. Разверните Prometheus в Kubernetes, используя содержимое папки k8s/prometheus.
6. Запустите нагрузку на приложение в Kubernetes следующим образом:
   - Добавьте в файл /etc/hosts строку следующего вида: 
        <внешний IP-адрес Kubernetes> flask01.terop-kuber.com
   - Запустите скрипт app_load.py

График HTTP-запросов с алертом
![график](https://github.com/terop1989/flask-prometheus/blob/master/screenshots/graph.png)

Настройки запросов для выборки данных графика и алерта
![настройки запросов](https://github.com/terop1989/flask-prometheus/blob/master/screenshots/query.png)

Настройки алерта
![настройки алерта](https://github.com/terop1989/flask-prometheus/blob/master/screenshots/alert.png)
