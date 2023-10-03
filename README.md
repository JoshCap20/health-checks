# Health Checker Tool

A comprehensive monitoring tool designed to assess and send notifications about the health of specified URLs and database connections. With the flexibility to perform simple ping checks, database connection tests, and the ability to customize response times, this tool ensures you are always informed about the status of your services and databases. 

<img width="885" alt="Screenshot 2023-10-03 at 5 54 50 PM" src="https://github.com/JoshCap20/health-checks/assets/97563979/e841349c-bdc1-4134-8754-ddf6f5bc439b">

## Features

- **Ping Check**: Verifies if a URL is reachable and logs the status.
  
- **Database Connection Check**: Tests the connection to a given database and logs the response time.

- **Custom Response Time Thresholds**: Define your own thresholds for warning and error response times.
  
- **Wi-Fi Connectivity Check**: Continuously checks for Wi-Fi connectivity and pauses the health checks if disconnected.

- **Alerts**: Configurable alerts (like email notifications and telegram) based on specific log levels to keep you informed.

## Installation
```bash
git clone https://github.com/JoshCap20/health-checks.git
cd health_checker
pip install -r requirements.txt
```

## Usage

To monitor a single URL:

```bash
python main.py --urls "https://example.com"
```

To monitor both URLs and databases:

```bash
python main.py --modules "ping,db" --urls "https://example.com,https://another-example.com" --dbs "your_database_connection_string"
```

### Command-Line Arguments

- `--ping-timeout`: Specify the ping timeout in seconds (default: 180 seconds).
  
- `--urls`: A comma-separated list of URLs you want to monitor.
  
- `--dbs`: A comma-separated list of database connection strings you want to check.
  
- `--modules`: Modules to be used for health checking. Available options are `ping`, `db`, and more to be added later. Default is `ping`.
  
- `--error-response-time`: Set the minimum acceptable response time in seconds. Any response slower than this will trigger an error. Default is 2 seconds.
  
- `--warning-response-time`: Set the response time threshold for warnings. Any response slower than this but faster than the error-response-time will trigger a warning. Default is 1 second.

### Alert Configuration

Alerts are configurable through `config.json`. You can set up various alert types, such as email notifications. 

For instance, to set up an email alert:

```json
{
  "alerts": {
    "email": {
      "active": true,
      "to_email": "your_email@gmail.com",
      "smtp_server": "smtp.gmail.com",
      "smtp_port": 587,
      "smtp_user": "your_smtp_user@gmail.com",
      "smtp_pass": "your_password",
      "alert_level": "WARNING"
    },
   "telegram": {
      "active": true,
      "bot_token": "bot_token",
      "user_id": "user_id",
      "alert_level": "INFO"
    }
  }
}
```

## Expansion

The architecture of this tool is modular, allowing for seamless expansion with additional health checks or alert methods. New checks can be added in the `checks` directory, and new alert methods in the `alerts` directory.

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
