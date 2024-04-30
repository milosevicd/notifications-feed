# Notifications Feed

## Description

Test project for notifications feed.

The notification feed is from a hypothetical social website that allows users to write posts, like posts and comment on posts. The notifications can be of two types: Like and Comment. Like indicates that one user liked a user's post and Comment indicates that one user commented on a user's post. In the scope of this test project, all posts are considered to belong to a single user (while comments and likes are coming from other users), it's like the user has their own private DB to manage his posts.

The notifications are aggregated per type (comment / like) and post. The order in which the notifications are served or aggregated is not managed. 

UI is very simple, the focus was on the backend part development. There's no authentication (nor authorization) checks, the page and API endpoint are open for access.

In Dev env, on server startup, all notifications are loaded into a DB from a JSON file `notifications-feed.json` (stored within the project). All user avatars are also loaded and stored in the DB. Simple in memory SQL DB is used.

In Prod, a real SQL DB is expected to be configured.

One API endpoint is exposed that returns a JSON of aggregated notifications, at `/api/notifications/aggregate`. This endpoint is documented on swagger, which is also exposed through swagger-ui, at `/swagger`.

One web page is available at `/notifications.html` that contains a simple HTML table and fetches (through XHR) aggregated notifications from the API and displays them in the table.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Running tests](#running-tests)

## Requirements

Python >= 3.3

OR

Python < 3.3 with venv module installed (`pip install virtualenv`)

## Installation

Windows:
```
git clone https://github.com/milosevicd/notifications-feed.git
cd notifications-feed
python -m venv nfd_venv
nfd_venv\Scripts\activate.bat
pip install -r requirements.txt
python -m run
```

Linux:
```
git clone https://github.com/milosevicd/notifications-feed.git
cd notifications-feed
python -m venv nfd_venv
source nfd_venv/bin/activate
pip install -r requirements.txt
python -m run
```

## Usage

Go to [local Swagger](http://127.0.0.1:5000/swagger/) to play with the API or to [local webpage](http://127.0.0.1:5000/notifications.html) to see the notifications formatted in a table.

## Running tests

After installation, you can run the tests:
```
python -m pytest
```
