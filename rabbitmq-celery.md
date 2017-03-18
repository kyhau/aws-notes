# rabbitmq-notes

## Celery and Rabbitmq

#### How to config Celery with rabbitmq to creates one queue instead of multiple queues?

When you use *amqp* as result backend, it will create a new temporary queue for every result corresponding to each tasks that worker consumes.

If you are not interested in the result, you can try `CELERY_IGNORE_RESULT = True` setting.

The temporary queue will last for 24 hours by default. You can try setting CELERY_TASK_RESULT_EXPIRES=<time in secs> for that.

For details see [ext-link](https://stackoverflow.com/questions/20998658/celery-with-rabbitmq-creates-results-multiple-queues)


## Upgrading rabbitmq

For details see https://www.rabbitmq.com/install-debian.html

```sh

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

```
