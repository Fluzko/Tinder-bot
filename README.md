# Tinder-bot

Tinder-bot is a bot that logins into your Tinder account and start 'autoliking' people, handling any popup on its way

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) and [venv](https://pypi.org/project/virtualenv/) to install all the requirements that Tinder-bot needs.

Download chromedriver, unzip, move to /usr/local/bin (mac os / linux)
```bash
cd Tinder-bot
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage
First you need to modify the config.py file in order to set your preferences.
When ready, just run the command:

```bash
python3 run.py
```
and have fun.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Changelog
- Dislikes the ones who has no photo

## Fixings
- sleeps replaced for implicit waits
- fixed the "find_element_by_xpath" by custom xpath

