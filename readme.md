# QR CODE GENERATOR - Team 53 solution


## Table of contents

- [Overview](#overview)
  - [Architecture](#architecture)
  - [The challenge](#the-challenge)
  - [Features](#features)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
- [Run locally](#run-locally)




## Overview

A platform that allows users generate QR code for data inputted while also providing analytics and metrics. 


## Architecture

Monolith

### The challenge

User: Unauthenticated

- Visit the platform to view basic information about it
- View and Interact with the documentation
- Register to view more details
- No access to use until registered

User: Authenticated
- Full access to the platform
- Allow setting on what should happen when qr is scanned - give at least 2 options
- Allow user to download (allow png, jpeg and pdf download format), or share code by email or social media
- Allow user save data and come back to it

### Features


### Links

- link to site hosted by github: [Pseudo-site](https://zuri-training.github.io/QR_GEN_TEAM-53/runner/index.html)

## My process

### Built with

- Semantic HTML5 markup
- CSS custom properties
- CSS Grid
- Javascript
- Django
- [Segno]("https://segno.readthedocs.io/en/stable/make.html")
- [django]("https://www.djangoproject.com/")

## Run locally.

If you want to run locally,then you can use the following command to run locally on your machine:

Clone the project

```
  git clone git@github.com:zuri-training/QR_GEN_TEAM-53.git
```

Go to the project directory

```
  cd QR_GEN_TEAM-53.git
```

Create a Virtual Environment

```
python -m venv venv
```

Activate Virtual Environment

```
venv\scripts\activate
```

Install Dependencies

```
  pip install -r requirements.txt
```

Change directory 

```
  cd qrgen53
```


make migrations

```
python manage.py makemigrations
```

Migrate the database

```
python manage.py migrate
```

create superuser

```
python manage.py createsuperuser
```

Finally, Start The Server.

```
python manage.py runserver
```

