import json
from faker import Faker
from kafka import KafkaProducer
from pizzaproducer import PizzaProvider



folderName = "./" 
producer = KafkaProducer(
    bootstrap_servers = "kafka-demo-ruhanirekhi-856c.h.aivencloud.com:26666",
    security_protocol = "SSL",
    ssl_cafile= folderName+"ca.pem", 
    ssl_certfile= folderName+"service.cert",
    ssl_keyfile= folderName+"service.key",
    value_serializer = lambda v: json.dumps(v).encode('ascii'),
    key_serializer = lambda v:json.dumps(v).encode('ascii')
)

producer.send("test-topic",
              key={"key":1},
              value= {"message": "hello world"}
              )

fake = Faker()
fake.add_provider(PizzaProvider)

for i in range(10):  # Stream 10 fake orders
    order = {
        "order_id": i + 1,
        "customer": {
            "name": fake.name(),
            "address": fake.address(),
            "phone": fake.phone_number()
        },
        "pizza": fake.pizza_name(),
        "quantity": fake.random_int(min=1, max=5)
    }
    producer.send(
        "pizza-orders",
        key={"order_id": order["order_id"]},
        value=order
    )
    print(f"Sent order: {order}")

producer.flush()



