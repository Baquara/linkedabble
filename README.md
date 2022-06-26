# Linkedabble

This is a simple Python script that scrapes job data from LinkedIn. The project uses Selenium and pandas. A requirements.txt file is included. The main script generates a CSV file. It needs the user to enter the login and password on the terminal (for now).

## Installation

First, clone the repository:

```
$ git clone https://github.com/baquara/linkedabble.git
```

Then, install the dependencies:

```
$ pip install -r requirements.txt
```

## Usage

To run the script, simply enter:

```
$ python main.py --login your_login@email.com --password your_password
```
Then enter your LinkedIn login and password on the terminal when requested.
The project will generate a CSV file with job data from the listings.
