# Notifications Feed

## Description

Test project for notifications feed.

The notification feed is from a hypothetical social website that allows users to write posts, like posts and comment on posts. The notifications can be of two types: Like and Comment. Like indicates that one user liked a user's post and Comment indicates that one user commented on a user's post.

The notifications are aggregated per type (comment / like) and post. The order in which the notifications are served or aggregated is not managed.

On server startup, all notifications are loaded into a DB from a JSON file notifications-feed.json (stored within the project). They are all considered to belong to a single user.

One API endpoint is exposed that returns a JSON of aggregated notifications, at /api/notifications/aggregate. This endpiont is documented on swagger, which is also exposed through swagger-ui, at /swagger.

Single web page is available at /notifications.html that contains a simple HTML table and fetches (throug XHR) aggregated notifications from the API and displays them in the table.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

git clone https://github.com/milosevicd/notifications-feed.git
cd notifications-feed
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python -m run 

## Usage

Go to [local Swagger](http://127.0.0.1:5000/swagger/) to play with the API or to [local webpage](http://127.0.0.1:5000/notifications.html) to see the notifications formatted in a table.