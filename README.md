## Kafka-Pizza-Order-Streamer

This project streams fake pizza orders to a Kafka topic using Python, Faker, and a custom pizza provider.

## Features

- Generates realistic fake pizza orders (customer info, pizza type, quantity)
- Sends orders to a Kafka topic (`pizza-orders`)
- Uses SSL for secure Kafka connection

## Prerequisites

- Python 3.10+
- Kafka cluster with SSL enabled (e.g., Aiven)
- SSL certificate files: `ca.pem`, `service.cert`, `service.key`
- Required Python packages:
  - `kafka-python`
  - `faker`

## Setup

1. **Install dependencies:**
   ```bash
   pip install kafka-python faker
   ```

2. **Place SSL certificates**  
   Put `ca.pem`, `service.cert`, and `service.key` in the project folder.

3. **Configure Kafka connection**  
   Edit `main.py` to set your Kafka `bootstrap_servers` and topic names if needed.

## Usage

Run the producer script to stream fake pizza orders:

```bash
python main.py
```

You should see output like:
```
Sent order: {'order_id': 1, 'customer': {...}, 'pizza': 'Margherita', 'quantity': 2}
...
```

## Files

- `main.py` — Streams fake pizza orders to Kafka.
- `pizzaproducer.py` — Custom Faker provider for pizza names.
- `ca.pem`, `service.cert`, `service.key` — SSL certificates for Kafka connection.

## Customization

- Change the number of orders by editing the loop in `main.py`.
- Add more pizza names in `pizzaproducer.py`.

## Troubleshooting

- **SSL errors:** Ensure your certificate files are correct and paths are set properly.
- **Kafka connection issues:** Verify your Kafka server address and topic exist.

## License

MIT License
