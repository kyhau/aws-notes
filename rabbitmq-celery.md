# rabbitmq-notes

## Celery and Rabbitmq

#### How to config Celery with rabbitmq to creates one queue instead of multiple queues?

When you use *amqp* as result backend, it will create a new temporary queue for every result corresponding to each tasks that worker consumes.

If you are not interested in the result, you can try `CELERY_IGNORE_RESULT = True` setting.

The temporary queue will last for 24 hours by default. You can try setting CELERY_TASK_RESULT_EXPIRES=<time in secs> for that.

For details see [ext-link](https://stackoverflow.com/questions/20998658/celery-with-rabbitmq-creates-results-multiple-queues)


## Updating rabbitmq

```
sudo service rabbitmq-server stop
ps aux | grep rabbit
sudo apt-get install --only-upgrade rabbitmq-server
ps aux | grep rabbit
sudo rabbitmqctl list_users
sudo rabbitmqctl list_vhosts
sudo rabbitmqctl environment
```

## Reinstalling rabbitmq

For details see https://www.rabbitmq.com/install-debian.html

```
# Stop RabbitMQ
$ rabbitmqctl stop 
 
#Change /etc/hosts
#Change /etc/hostname
 
#Uninstall old RabbitMQ: 
$ dpkg -P rabbitmq-server
 
#Remove RabbitMQ’s database: 
$ rm -rf /var/lib/rabbitmq
 
#Find erlang’s process that is running rabbit: ps ax | grep rabbit
#Kill the listed process
 
#Reinstall RabbitMQ: 
$ apt-get install rabbitmq-server

#Check versions
$ sudo rabbitmqctl status | grep RabbitMQ
```

## rabbitmq basic

```
sudo service rabbitmq-server restart

rabbitmqctl list_queues -p (vhostname)
rabbitmqctl delete_vhost (vhostname)
rabbitmqctl add_vhost (vhostname)

# How to set permission to local rabbitmq
rabbitmqctl set_permissions (uname) -p (vhostname) ".*" ".*" ".*"
```

## Rabbitmq Management Plugin - https://www.rabbitmq.com/management.html

```
sudo rabbitmq-plugins enable rabbitmq_management
sudo service rabbitmq-server restart
sudo rabbitmq-plugins list

nano /etc/rabbitmq/rabbitmq.config
------------------------
[{rabbitmq_management,
  [{listener, [{port,     15671},
               {ssl,      true},
               {ssl_opts, [{cacertfile, "/path/to/cacert.pem"},
                           {certfile,   "/path/to/cert.pem"},
                           {keyfile,    "/path/to/key.pem"}]}
              ]}
  ]}
].
------------------------
```


