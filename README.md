
# Selenium Web Automation Project

A Python-based web automation project using Selenium WebDriver with Firefox in headless mode, designed to run on Replit.

## Features

- Headless Firefox browser automation
- Configurable logging system
- Error handling and recovery
- Ready to run on Replit's infrastructure

## Prerequisites

The project uses Poetry for dependency management and requires the following packages:
- Python 3.10+
- Selenium 4.24.0
- Flask 3.0.3
- BeautifulSoup4 4.12.3
- Requests 2.32.3
- OpenAI Whisper

## Project Structure

```
├── templates/
│   └── index.html
├── main.py         # Main driver script
├── scraper.py      # Web scraping functionality
├── transcriber.py  # Audio transcription functionality
└── pyproject.toml  # Project dependencies
```

## Usage

1. The project runs automatically when deployed on Replit
2. The main script initializes a headless Firefox browser
3. Logs are generated to track the automation process
4. Browser session is properly managed and cleaned up after use

## Error Handling

The project includes comprehensive error handling:
- WebDriver initialization failures
- Navigation errors
- Resource cleanup
- Detailed logging for debugging

## Development

To modify the project:
1. Fork this Repl
2. Make your changes
3. Test using the built-in Replit runtime
4. Deploy directly using Replit's deployment features

## License

This project is open source and available under the MIT License.
