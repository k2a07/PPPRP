Задание 2

Перевести приложение из предыдущего задания для работы через Istio. Для этого:
написать скрипт для запуска Istio в вашем кластере, и настройки добавления лейблов для того, чтобы Istio начал автоматически внедрят sidecat контейнеры к вашим приложениям в Kubernetes. Также, в этом скрипте, при запуске Istio в вашем кластере, необходимо указать настройку, которая запрещает внешний трафик по умолчанию, если нет необходимых манифестов.

написать все необходимые манифесты, чтобы теперь весь входящий трафик шел через Ingress Gateway

теперь при обращении на endpoint GET /time вашего приложения, оно должно делать запрос на http://worldtimeapi.org/api/timezone/Europe/Moscow и возвращать пользователю значение поля datetime из запроса выше.

создать манифейсты, которые разрешают внешний трафик на worldtimeapi.org
в readme проекта опишите куда надо сделать запрос, чтобы получить результат(оставить с предыдущего задания, если ничего не поменялось).

________________________________________________________________________________________

Запустим minikube:

```minikube start```

Установим Istio согласно документации (https://istio.io/latest/docs/setup/install/)

```curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.22.0 TARGET_ARCH=x86_64 sh -```

```cd istio-1.21.0```

```export PATH=$PWD/bin:$PATH```

```istioctl install --set profile=demo -y --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY```

```kubectl label namespace default istio-injection=enabled```

Далее аналогично заданию 1 проведем сборку образов:

```docker build -t kirillacharya/app -f dcrfl-0 .```

```docker build -t kirillacharya/scr -f dcrfl-1 .```

Запушим образы в докер хаб:

```docker push kirillacharya/app```

```docker push kirillacharya/scr```

Применяем манифесты конфигураций аппа:

```kubectl create -f /home/kirillacharya/mipt_dev/PPPRP/Task1/script_dpl.yaml```

```kubectl create -f /home/kirillacharya/mipt_dev/PPPRP/Task1/app_dpl.yaml```

```kubectl create -f /home/kirillacharya/mipt_dev/PPPRP/Task1/clstr_ip.yaml```

Применение манифесты конфигураций Istio:

```kubectl apply -f /home/kirillacharya/mipt_dev/PPPRP/Task2/gateway.yaml```

```kubectl apply -f /home/kirillacharya/mipt_dev/PPPRP/Task2/my_service.yaml```

```kubectl apply -f /home/kirillacharya/mipt_dev/PPPRP/Task2/other_service.yaml```

Оставшиеся шаги делаем аналогично первому заданию, а именно проводим соединение с LoadBalancer service:

```minikube tunnel```

Затем, можем получить ссылку для подключения (открываем второй терминал):

```minikube service my-service```

Следующие добавления к ссылке дают доступ ко времени и статистике соответственно:

```/time``` и ```/statistics```

Наконец, мы можем прочитать файл ```stats.txt```. Название pod со скриптом получим по:

```kubectl get pods```

Для получения доступа к статистике вводим:

```kubectl exec -it <pod_name> -- /bin/bash```, и

```cat stats.txt```