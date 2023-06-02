## Requirements

 - [Python](https://www.python.org/)
 - [Node.js](https://nodejs.org/en)
 - [Docker](https://www.docker.com/)

## Usage
Open a terminal window and type the following commands

``` 
$ git clone https://github.com/ElCirko/Shaurmichnaya-u-Gurama && cd Shaurmichnaya-u-Gurama/backend
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ docker-compose up -d
$ ./manage.py runserver
```

In another terminal window, navigate to the project folder and enter the following commands
```
$ cd frontend
$ npm install
$ npm run serve
```