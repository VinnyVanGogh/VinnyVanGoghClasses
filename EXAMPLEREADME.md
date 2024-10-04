# toml-cfg-tool  

## Table of Contents

- [Prerequisites](#prerequisites)

## Prerequisites

- [Python](https://www.python.org/downloads/)

## Arguments 

The tool accepts the following arguments:
- `--show`: Show the current configuration. (only shows the options that can be updated)

# Testing block code reading

```python
import os
import sys
import requests
import json
from datetime import datetime

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        sys.exit(1)

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

def main():
    url = "https://api.example.com/data"
    data = fetch_data(url)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data_{timestamp}.json"
    save_data(data, filename)

if __name__ == "__main__":
    main()
```
