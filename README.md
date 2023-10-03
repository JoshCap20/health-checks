# Health Checker Tool

A robust tool designed to monitor and report on the health of specified URLs. It includes a variety of checks like simple pinging and custom response times. Alerts and logs are generated based on the health of the URLs, ensuring you are always aware of the status of your services.

## Features
- **Ping Check**: Verifies if a URL is reachable and logs the status.
- **Custom Response Time Thresholds**: Set custom thresholds for warning and error response times.
- **Wi-Fi Connectivity Check**: Continuously checks for Wi-Fi connectivity and pauses the health checks if disconnected.

## Installation
```bash
git clone https://github.com/JoshCap20/health-checks.git
cd health_checker
pip install -r requirements.txt
```

## Usage

Run the tool using:

```bash
python main.py --urls "https://example.com,https://another-example.com" 
```

### Command-Line Arguments

- `--ping-timeout`: Specify the ping timeout in seconds (default: 180 seconds).
  
- `--urls`: A comma-separated list of URLs you want to monitor.
  
- `--modules`: Modules to be used for health checking. Available options are `ping` and more to be added later. Default is `ping`.
  
- `--error-response-time`: Set the minimum acceptable response time in seconds. Any response slower than this will trigger an error. Default is 2 seconds.
  
- `--warning-response-time`: Set the response time threshold for warnings. Any response slower than this but faster than the error-response-time will trigger a warning. Default is 1 second.

## Expansion

The architecture of this tool is modular, making it easy to expand with additional health checks as needed. New checks can be added in the `checks` directory and then integrated into the main tool.

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
