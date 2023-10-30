import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='',
    virtual_host='',
    credentials=pika.PlainCredentials('', '')
))

channel = connection.channel()

exchange_name = 'direct-exchange'
routing_key = 'rota-um'

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

def callback(ch, method, properties, body):
    print(f" [x] Recebido: {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Aguardando mensagens. Pressione CTRL+C para sair.')

channel.start_consuming()
