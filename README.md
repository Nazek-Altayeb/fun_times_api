# Fun times API

Goal: Develop backend services that receive requests from the [frontend project](https://github.com/Nazek-Altayeb/fun-times).
The functionalities range from Authentication to add/retrieve content from database through this API.

## Table of Content

- [Fun times API](#fun-times-api)
  - [Table of Content](#table-of-content)
  - [System Design](#system-design)
  - [Functionalities](#functionalities)
  - [Agile development process](#agile-development-process)
  - [Bugs](#bugs)
  - [Test](#test)
  - [Tools And Languages](#tools-and-languages)
  - [Frameworks](#frameworks)
  - [Libraries and Packages](#libraries-and-packages)
  - [Deployment](#deployment)
- [Credits](#credits)
  - [Documentation](#documentation)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## System Design

The Database for this project is a relational DB, consists of four tables, Profiles, Posts, Comments, Likes, Followers. The backend has been developed using the Django REST Framework.

<details><summary>See Database Schema</summary>
<img src="https://res.cloudinary.com/nazek/image/upload/v1696682617/fun_times-erd_uo0j12.png">
</details> 


[Back to the top](#table-of-content)

<br>

## Functionalities
The base functionalities of the API are re-used ones from [external resource](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopmentadvancedfrontend). New functionalities have been implemented according to the project needs and logic.

Each of the following apps consist of:
- A model class, consist  of the data members that hold the each piece of information the end user expected in the frontend.  
- A serilizer to transform data to jason format when sending respond to the front end.
- A url file, that hold the path relate to each method in the views file
- A view, where the functionalities are define.

**Setup Api environment**
  
  Required libraries have been installed, new apps are added to the list of apps in the setting file.
  env file have been created in order to hold values of (DATABASE_URL, CLOUDINARY_URL, SECRET_KEY, CLIENT_ORIGIN_DEV, CLIENT_ORIGIN, HEROKU_POSTGRESQL_WHITE_URL), those which are not upload a log with the project to the Github.

**CRUD profiles**
  
  i have extended this model and added new fields, so user can enter more info. 
  The read/write/update/delete service helps the user to manage the profile, , 
  
**Authenticate the Profile**
  
  Use the JSON Web Token to extend the time that the page holds the sign in credentials, 
  so the user is not asked to enter the credentials over again.

**CRUD posts**
  
  I have extend the Post related field that are serialized, so the end user can add more information related to the post, 
  for example: the post's visibility.

**CRUD Comments**
  
  Logged in users could add/update/remove comments at any post

**Add /Remove likes**
  
  Users could like/unlike posts except their own ones.

**Post's Visibility**
  
  I have created a new app, the main purpose of this app is to let the user to specify whether his post will be visible to all users or only the folowers.
  The model class of this app is connected to both the Profile and Post table.

**Deploy and test**
  
  In earlier stages the API has been deployed to the Heroku platform.
  this step was done continously to ensure the consistency.

## Agile development process
The development process went smoothly with the use of the Github roadmap project board.
I named my project in the Github **fun times api**.
I created and prioritized  the issues according to `MOSCOW`.
I have followed the iterative approach, each sprint last for 5 days.

- **Sprint 1 (Aug 29th To Sep 2nd, 2023)**
  - [x] [Set up environmet](https://github.com/Nazek-Altayeb/fun_times_api/issues/1) <code style="color:red">(Must have)</code>
  - [x] [CRUD profiles](https://github.com/Nazek-Altayeb/fun_times_api/issues/2) <code style="color:#5319E7">(Should have)</code>
  - [x] [Authenticate the Profile](https://github.com/Nazek-Altayeb/fun_times_api/issues/3) <code style="color:red">(Must have)</code>
  - [x] [CRUD Posts](https://github.com/Nazek-Altayeb/fun_times_api/issues/4) <code style="color:#5319E7">(Should have)</code>
  - [x] [CRUD comments](https://github.com/Nazek-Altayeb/fun_times_api/issues/5) <code style="color:#5319E7">(Should have)</code>
  - [x] [Add /Remove likes](https://github.com/Nazek-Altayeb/fun_times_api/issues/6) <code style="color:#5319E7">(Should have)</code>
- **Sprint 2 (Sep 3rd To 7th, 2023)**
  - [x] [Deploy and test](https://github.com/Nazek-Altayeb/fun_times_api/issues/7) <code style="color:#5319E7">(Should have)</code>
- **Sprint 3 (Sep 8th To 12th, 2023)**
  - [x] [Bugs fix](https://github.com/Nazek-Altayeb/fun_times_api/issues/9) <code style="color:red">(Must have)</code>
- **Break (Sep 13th To Oct 2nd, 2023)**
  During this time, all efforts went to the frontend.
- **Sprint 4 (Oct 3rd To 7th, 2023)**
  - [x] [Set post visibility](https://github.com/Nazek-Altayeb/fun_times_api/issues/8) <code style="color:red">(Must have)</code>
  - [x] [Documentation](https://github.com/Nazek-Altayeb/fun_times_api/issues/10) <code style="color:#5319E7">(Should have)</code>

## Bugs
  - visibility object return null when loading posts, this was resolved by adding the visibility objects to Post's serializer set of fields.
  - URL is not defined, resolved by adding the execution path to the array of ALLOWED_HOSTS 

## Test
Manual testing is applied to ensure the reliability and consistency of the api.

Tests results are available [here](TEST.md).

## Tools And Languages

- Git: A distributed version control system used for tracking changes in the project's source code.
- GitHub: A web-based hosting service for version control repositories, used for storing and managing the project's source code.
- CodeAnyWhere: An online integrated development environment (IDE) used for developing and testing the Travel Tickr project.
- Heroku: A cloud platform that enables deployment and hosting of web applications. Heroku was used for deploying the Travel Tickr project to a live server.
- Django : Coding language.

## Frameworks
  Django Rest Framework is the used to develop the api swervices.

## Libraries and Packages

- cloudinary, django-cloudinary-storage: Used for managing the storage and delivery of images through Cloudinary, a cloud-based service.
- dj-database-url: Utility to help you load your database into your dictionary from the DATABASE_URL environment variable.
- dj-rest-auth, Django-allauth, djangorestframework-simplejwt, PyJWT, oauthlib, requests-oauthlib, python3-openid: These libraries are used for managing user authentication, providing support for JWT tokens, OAuth and OpenID.
- Django, djangorestframework, django-filter: These are core components of the Django web framework, used for building the backend of the Travel Tickr application.
- gunicorn: A Python WSGI HTTP server for UNIX, used in deploying the application.
- Pillow: An imaging library in Python, allowing support for opening, manipulating, and saving many different image file formats.
- psycopg2: PostgreSQL adapter for Python, enabling Python to connect to the PostgreSQL database.
- sqlparse: A non-validating SQL parser module for Python, it provides support for parsing, splitting and formatting SQL statements.

## Deployment

Deploying the fun times api was as follow:

1. Create Required Accounts: If you haven't done so yet, create accounts on Heroku, ElephantSQL, and Cloudinary. These services are necessary for hosting the application, managing the database, and storing images, respectively.
2. Prepare the Application:  Ensures that the application runs in production mode during deployment. Commit all changes and push your code to your GitHub repository.
3. Create a New Application on Heroku: From your Heroku dashboard, create a new application and select the appropriate region.
4. Set Environment Variables: In your local env file, set your environment variables including the ElephantSQL URL, Cloudinary URL, and Django Secret Key. These variables should also be added to your Heroku app settings under the Config Vars section. This ensures that these services can communicate with your Heroku app.
5. Database Management: Ensure that all database migrations have been made and the current state of your models is reflected in the database schema. The command python manage.py makemigrations and python manage migrate are usually used for this purpose in Django.
6. Deployment Process: In your Heroku dashboard, go to your application's deploy page. Connect your GitHub repository to your Heroku application under the "Deployment method" section. Under the "Manual deploy" section, select the branch you want to deploy and click "Deploy Branch".
7. Verify Deployment: Once the deployment is successful, Heroku will provide a URL to access the live application. Test the application to ensure all components are functioning properly.

# Credits

## Documentation
At some parts of the Readme.md and ManualTest.md, i follow the design of the following [Readme.md](https://github.com/SandraBergstrom/travel-tickr-api/blob/main/README.md)
