import pika

def enviar_mensagem(mensagem, channel, routing_key):
    channel.basic_publish(
        exchange=directExchangeName,
        routing_key=routing_key,
        body=mensagem
    )
    print(f"Mensagem enviada: {mensagem}")

def main():
    try:
        connection = pika.BlockingConnection(
            pika.URLParameters("")
        )
        channel = connection.channel()

        channel.exchange_declare(exchange=directExchangeName, exchange_type="direct", auto_delete=True)


        while True:
            mensagem = input("Digite a mensagem (Ctrl+C para encerrar): ")
            enviar_mensagem(mensagem, channel, routingKey)

    except KeyboardInterrupt:
        print("Programa encerrado.")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    directExchangeName = "direct-exchange"
    routingKey = "rota-um"

    try:
        main()
    except KeyboardInterrupt:
        pass
