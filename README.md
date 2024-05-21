**Задание 1**

Реализовать простое веб приложение, у которого обрабатывает запросы на два endpoint’а:

GET /time - этот endpoint должен отдавать текущее время 

GET /statistics - этот endpoint должен отдавать количество обращений к endpoint’у /time в виде одного числа. Соответственно, ваше приложение должно хранить информацию о каждом обращении и отдавать эту информацию по запросу. 

Далее необходимо реализовать скрипт, который будет обращаться к endpoint’у GET /statistics и записывать полученный результат в файл. Этот скрипт должен будет вызываться раз в 5 секунд.

Все перечисленное выше должно запускаться в Kubernetes. Для этого вам необходимо: 
контейнеризировать ваше приложение и скрипт(docker образы)
написать манифесты конфигураций для этих двух образов
bash скрипт для сборки образов и запуска всего внутри Kubernetes

В readme проекта опишите куда надо сделать запрос, чтобы получить результат

________________________________________________________________________________________

Запустим minikube:

```minikube start```

Проведем сборку образов:


```docker build -t kirillacharya/app -f dcrfl-0 .```

```docker build -t kirillacharya/scr -f dcrfl-1 .```

Запушим образы в докер хаб:

```docker push kirillacharya/app```

```docker push kirillacharya/scr```

Применяем манифесты конфигураций:

```kubectl create -f /home/kirillacharya/mipt_dev/PPPRP/Task1/script_dpl.yaml```

```kubectl create -f /home/kirillacharya/mipt_dev/PPPRP/Task1/app_dpl.yaml```

```kubectl create -f /home/kirillacharya/mipt_dev/PPPRP/Task1/clstr_ip.yaml```

Далее, проводим соединение с LoadBalancer service:

```minikube tunnel```

Затем, можем получить ссылку для подключения (открываем второй терминал):

```minikube service my-service```

Следующие запросы дают доступ ко времени и статистике соответственно:

```minikube service my-service/time```

```minikube service my-service/statistics```

Наконец, мы можем прочитать файл ```stats.txt```. Название pod со скриптом получим по:

```kubectl get pods```

Для получения доступа к статистике вводим:

```kubectl exec -it <pod_name> -- /bin/bash```, и

```cat stats.txt```