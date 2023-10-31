<p align="center"><img src="pygmyui/static/logo/logov2.png" alt="herme.li" height="200px"></p>

<div align="center">
  <h1>Herme.li</h1>

Web: [https://herme.li](https://herme.li)
</div>

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Technical Info](#technical-info)
- [Setup](#setup)
  - [Clone](#clone-the-repository)
  - [Docker](#docker)
  - [Manual](#manual)
  - [DB Setup](#db-setup)
  - [Using Pygmy API](#using-pygmy-api)
    - [Create User](#create-user)
  - [Shell Usage](#shell-usage)
- [Development](#development)
- [Deployment](#deployment)
  - [Deploying changes](#deploying-changes)
  - [Run tests:](#run-tests)
      - [Run tests with coverage report](#run-tests-with-coverage-report)
- [License](#license)

Herme.li is a fork of the open-source URL-shortener web-app Pygmy by [amitt001](https://github.com/amitt001/).

It has been customized and extended to match our company internal needs by [raphael-s](https://github.com/raphael-s).

Pygmy or is an open-source, extensible & easy-to-use but powerful URL shortener. It's created keeping in mind that it should be easy to host and run your custom URL shortener without much effort. [Open-source Python URL shortener]

The architecture is very loosely coupled which allows custom integrations easily.

**The project has 3 major parts**

- The core URL shortening code
- A REST API on top. Uses Flask framework
- The UI layer for rendering the UI. It uses the Django framework

# Features

- URL shortener
- Customized short URL's
- User Login to track shortened URL's and link stats
- Automatic QR code generation as SVG image
- User dashboard
- Link Analytics

# Technical Info

- Python 3.9, Javascript, JQuery, HTML, CSS
- REST API: Flask
- Pygmyui: Django
- DB: SQLite
- Docker

# Setup

Since we customized the web-app to match our own demands, using the official Docker image is no longer viable.

## Clone the repository

1. Clone this repository to your local machine `git clone git@github.com:Herrmann-AG/herme-li.git`
2. Open the new folder `cd herme-li`

## Docker

To run the app locally using Docker, you just have to build the images and then start the containers.

1. In terminal run this command: `docker compose up -d --build`
3. Open http://localhost:10101 in your browser

## Manual

1. Create a new Python virtualenv and activate it
    - `python -m venv .`
    - `source ./bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
4. `python run.py`
5. Visit `127.0.0.1:8000` to use the app
6. Logs can be viewed at `pygmy/data/pygmy.log`

Note:

 - **This module only supports Python up to version 3.9. Make sure pip and virtualenv are both python 3 based versions.**
 - The project has two config files:
    - pygmy.cfg: `pygmy/config/pygmy.cfg` rest API and pygmy core settings file
    - settings.py: `pygmyui/pygmyui/settings.py` Django settings file
 - You can run pygmy shell also. Present in the root directory. To run the program on the terminal: `python shell.py`
 - By default, DEBUG is set to False in `pygmyui/pygmyui/settings.py` file, set it to True if you have to make changes to the code.

## DB Setup:

The original Pygmy had options to use MySQL, or Postgres. We simply use SQLite since it is the easiest version to deploy and manage on our production server.

## Using Pygmy API

### Create User

    curl -XPOST http://127.0.0.1:9119/api/user/1 -H 'Content-Type: application/json' -d '{
    "email": "test@wochen-zeitung.ch",
    "f_name": "Test",
    "l_name": "WZ",
    "password": "huere_sicher"
    }'

Q. How  are link stats generated?
> For getting geo location stats from IP, maxminds GeoLite2-Country.mmd database is used. It's in the `pygmy/app` directory.

Q. How does the pygmy auth token work?
> It uses JWT. When user logs in using username and password two tokens are generated, refresh token and auth token. Auth token is used for authentication with the Pygmy API. The refresh token can only be used to generate a new auth token. Auth token has a very short TTL but refresh token has a longer TTL. After 30 minutes. When a request comes with the old auth token, a new token is generated from the refresh token API. User passwords are encrypted by [bcrypt](https://en.wikipedia.org/wiki/Bcrypt) hash algorithm.

# Development

To contribute:

1. Follow the steps described in [Setup](#manual)
2. Make your changes to the code
3. Commit your changes to a new branch
4. Push the changes to the Github repository
5. Open a pull request and assign somebody to review your changes

# Deployment

Herme.li is deployed using Docker on our VPS server Wachthubel, hosted at Hostfactory.

## Deploying changes

If there were changes made to the app, follow these steps to apply them to the production deployment:

1. Connect to the Wachthubel VPS (check Hostfactory for access Data) via SSH
2. Change into the herme-li directory `cd /var/www/vhosts/herme-li`
3. Make sure the ssh-agent is running (`eval $(ssh-agent)`) and the SSH key is present (`ssh-add ~/.ssh/id_github`)
4. Pull your changes from the Github repo `git pull`
5. Update, rebuild and recreate the Docker container `docker compose up -d --build`
6. That's it, make sure the site is running as expected!

## Run tests:

Tests no longer work due to the changes we had to make to pygmy.

# License

MIT License

Copyright (c) 2022 Amit Tripathi(https://twitter.com/amitt019)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Read License Terms](https://github.com/amitt001/pygmy/blob/master/LICENSE)
