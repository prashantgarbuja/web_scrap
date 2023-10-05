# Web Scraping Google Trends

This project involves web scraping Google Trends data in Australia (or Anywhere in the World) using Python. The data is scraped using BeautifulSoup and Selenium, and the results are saved in a CSV file. The entire process is automated using GitHub Actions, and the resulting CSV file is stored as an artifact.

## Usage

### Prerequisites

Before running the code, make sure you have the following installed:

- Python
- Selenium (for dynamic page to load first and extract data based on the html elements)
- BeautifulSoup

You can install the required packages by running:

```bash
pip install selenium beautifulsoup4
```
## Running the Code
Clone this repository to your local machine:
```bash
git clone https://github.com/prashantgarbuja/web_scrap.git
```
Navigate to the project directory
```bash
cd web_scrap
```
Run the python script
```bash
python web_scrap_google_trends.py
```
## GitHub Actions
The project is set up with a GitHub Actions workflow that automates the web scraping process. The workflow runs on a schedule and stores the resulting CSV file as an artifact.

### Workflow Details
- Workflow File: [.github/workflows/web_scrap.yml](.github/workflows/web_scrap_scheduler.yml)
- Schedule: Every day at 9:00 AM AEDT

## Artifacts
The resulting CSV file containing the Google Trends data is stored as an artifact for each workflow run. You can download the artifact from the [Actions tab](https://github.com/prashantgarbuja/web_scrap/actions/workflows/web_scrap_scheduler.yml) of this repository.

## Contributing
Feel free to contribute to this project by creating pull requests or reporting issues.
