# Health Management System Dashboard

## Overview

The Health Management System Dashboard is a web application built using Django for backend functionality and Tailwind CSS for frontend styling. The application aims to streamline the management of clients, health programs, and client enrollments in a health management system. The dashboard provides a comprehensive view of all clients, health programs, and upcoming tasks, making it easier for healthcare administrators and doctors to manage their tasks.

## Features

- **Dashboard**: A central place to view tasks, reminders, and key metrics.
- **Client Management**: Register new clients and view existing clients.
- **Health Program Management**: Create, view, and manage health programs.
- **Client Enrollment**: Enroll clients into available health programs.
- **AJAX-Based Content Loading**: Seamlessly load content without page refreshes.

## Tech Stack

- **Backend**: Django
- **Frontend**: Tailwind CSS, AJAX
- **Database**: SQLite (or specify your database)
- **Version Control**: Git

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django 4.x
- pip (Python package installer)

### Setup

1. Clone the repository:
   git clone https://github.com/yourusername/your-repository-name.git
2. Navigate into the project directory:
   cd your-repository-name
3. Install the required dependencies:
   pip install -r requirements.txt
4. Run the migrations to set up the database:
   python manage.py migrate
5. Create a superuser (for admin access):
   python manage.py createsuperuser
6. Run the development server:
   python manage.py runserver

Now you can open the app in your browser at http://127.0.0.1:8000/.
