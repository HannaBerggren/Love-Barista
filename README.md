# Love Barista

![Image](/static/css/images/responsive.png)

[Live Site](https://8000-hannaberggr-lovebarista-4l76yoe8zfr.ws-eu101.gitpod.io/)

## Table Of Contents:
1. [Project Goals](#project-goals)
    * [CRUD functionality](#crud-functionality)
2. [UX Design](#ux-design)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)    
3. [Features](#features)
    * [Navigation Bar](#navigation-bar)  
    * [Home Page](#home-page)
    * [Register Page](#register-page)
    * [Create Blogpost](#create-blogpost)
    * [Login Page](#login-page)
    * [Logout Page](#logout-page)
    * [Edit Page](#edit-page)
    * [Delete Page](#delete-page)
    * [footer](#footer)

4. [Future Features](#future-features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgements](#acknowledgements)

### Project goals

* This site is created with the intention to help the coffee lovers around the world to share their passion for coffee. They should be able to view and change the blogpost if they think it should be neccessary.

### First time user goals
* As a first time user I want the navigation to be simple
* As a first time user I want the registration to be simple
* As a first time user I want the login to be simple
* As a first time user I want the logout to be simple
* As a first time user I want to easily understand how to change/delete my blogpost

### CRUD functionality

Love Barista features a data store with full Create, Read, Update and Delete functionality.

- Create - users can create a user account, and authenticated users can create a profile, collaboration requests and messages to their approved collaborators.
- Read - users can view the profiles and posts of other users. Authenticated users can read messages sent to them.
- Update - authenticated users can update their profiles and save the changes. They can approve collaboration requests sent to them wich results in a new many-to-many relationship in the database.
- Delete - authenticated users can delete their profile and pending collaboration requests, chosing to cancelling, rejecting or approving them. Authenticated users can also delete messages sent by or to them, the message is not deleted from the database until both the sending and receiving users have marked them as deleted.

## UX Design:

### Wireframes
Wireframes that where created in [Balsamiq](https://balsamiq.com/) for this project are displayed below. The wireframes were  created in the planning phase of the project. Please note that the wireframes might not be exactly a copy of the project due to the fact that the site has changed during development.

![design image](/static/css/images/wireframe.png)

### User Stories
After the first planning phase user stories were implemented one by one. The wireframes created became the base for the User stories. 

Individual user stories were categorised according to whether they had to be implemented to produce a Minimum Viable Product (MVP), with priority for development to be given to those that were part of the MVP specification. 

The user stories that where created can be found [here](https://github.com/users/malinpalo/projects/9) and are added below.

### Agile Methodology
GitHub issues, milestones and projects were used to document and track an agile development approach.
An issue was created for each user story. These were labelled as 'MVP' if they were part of the MVP spec. All user stories were then added to a 'Product Backlog' milestone  [Link to product backlog]().

I set up a plan for development this plan was just to show how it could work in real life. Development was divided into iterations with a timebox of four working days, each with a total value of 16 story points. The duration in calendar days was variable during development, due to fitting the four working days around work and other commitments. A milestone and a GitHub project board (a Kanban board) were created for each iteration, and user stories moved from the Product Backlog and into iterations as each cycle of work began. They were labelled as 'must have', 'could have' or 'should have' goals for the iteration, and assigned story point values. Story points for 'must have' user stories never exceeded 9 (60%).

A project Kanban board was used to track progress, with user stories moved between 'Todo', 'In Progress' and 'Done' columns as appropriate. 
![Image](/static/css/images/kanbanboard.png)

There was consideable uncertainty as to how many story point to allocate to each task. Therefor the first iteration had tasks exceeding 16 storie points in total. Tasks that didn't finish in time where to be moved in to the next iteration.

### Typography

### Color Scheme

* I decided to choose colors to get a warm and calm feeling. 
![design image](/static/css/images/colors.png)

I used [Coolors](https://coolors.co/) to generate a color scheme from the default post image. I chose a natural background color with complimentary colors in green, blue and orange for text, buttons and icons to make the sites content stand out to be clear to the user.

### Database Diagram

I created an entity relationship diagram using LucidCharts.

![ERD](/static/css/images/erd.png)

### Design Image

![design image](/static/css/images/lovebarista.jpg)

## Features:

### Navigation Bar

- The Navigation bar sits at the very top of each page, The logo is at the right hand side and the navigation links are on the left.
- When logged in the **Login** becomes **Logout** and the **Registeration** link is removed.
- The Navbar background is white with the Navigation links and logo in black and darkgreen colored text.
- When the logo is clicked it redirects the user to the home page.
- On large to xx-large screens the navigation bar is in the center of the page.
- When on medium to small screens the navigation menu changes to burger menu which shows all the nav links when clicked on (second two screenshot below).

![NavBar]()

Navigation bar on mobile and tablets
![NavBar Burger]()
![NavBar Burger Menu dropdown]()



### Home Page

* The Home page introduce the user to the blog by showing different blogposts. It's easy to click on every blogpost to read more about a place the viewer finds interesting.

![Image](/static/css/images/homepage.png)

### Register

* Makes it available for a new user to create an account, you have to have an account to be able to make a blogpost.

![Image](/static/css/images/register.png)


### Create/manage blogpost

* After you have register, after that when you click on your name in the navbar, you
can choose between the create blogpost page or the manage blogpost page.
* Create a blogpost offers the user to easily pick when they want to make their post.

![Image](/static/css/images/newpost-oldpost.png)



### Login

* This page is where the user can log in. 

![Image](/static/css/images/signin.png)

### Logout

* This page is where the user can log out if they want.

![Image](/static/css/images/signout.png)

### Footer

- The footer is found at the bottom of every page and is responsive for small and large screens.
- The footer displays author and icons for Facebook, Twitter, Instagram and Google. These are all in different colours to pop out to get the viewers interest.
- When any of the icons are clicked the social media site opens on a seperate tab, this way the user still has the Love Barista website open so they can easily navigate back to it.


![Image](/static/css/images/footer.png)



### Edit Page

![Edit page]()
![Edit page]()
![Edit page]()

### Delete Page

![Delete page]()



## Future Features

## Testing

Please click [**_here_**](TESTING.md) to read more information about testing Love Barista.

## Technologies 

* [GitHub](https://github.com/) - to host the repositories.
* [Gitpod](https://www.gitpod.io/) - as the IDE for the application.
* [Elephantsql](https://www.elephantsql.com/) - for the postgresql
* [Python](https://docs.python.org/3/contents.html) - primary language of the application.
* [HTML](https://www.w3schools.com/html/) - Structure/skeleton of the page
* [CSS](https://www.w3schools.com/css/) - extra styling of the webpage
* [Javascript](https://www.w3schools.com/js/) - the apply some extra button functions that I wanted
* [Stack overflow](https://stackoverflow.com/) - basic explaining 
* [Bootstrap 5](https://www.w3schools.com/bootstrap5/bootstrap_get_started.php) - for design and placement
* [PEP8](http://pep8online.com/) - for testing and validating the code.
* [Google Fonts](https://fonts.google.com/about) - for the font of the text
* Love Barista is a blog post for everyone who likes or love coffee. This app is a blog designed so that visitors and staff easily can manage the posts by them self. Both parties can post, view, change and delete their blogposts as per their own liking. 



## Planning

* This project was developed through the Kanban board, you can find this via the github projects. Here the developer creates cards to help them during the development, this is mainly to make it easier to keep track of the different user stories and make sure everything is completed.

### Features left to implement

* I would like to add a map function to point out where the location is
* I would like to spend smore time on the styling and make sure it looks even better.
* I would like to add a favicon for a better layout.

### Images

* images used n the project were all found on google.


## Admin Page
* Admin has access via the default Django Admin page. The Admin login can be accessed from the navigation menus once a superuser has logged in. Once logged in, Admin users have all the access to create, edit and delete all bookings. All the requests can be viewed from the admin page.

## Technologies 

* [GitHub](https://github.com/) - to host the repositories.
* [Gitpod](https://www.gitpod.io/) - as the IDE for the application.
* [Elephantsql](https://www.elephantsql.com/) - for the postgresql
* [Python](https://docs.python.org/3/contents.html) - primary language of the application.
* [HTML](https://www.w3schools.com/html/) - Structure/skeleton of the page
* [CSS](https://www.w3schools.com/css/) - extra styling of the webpage
* [Javascript](https://www.w3schools.com/js/) - the apply some extra button functions that I wanted
* [Stack overflow](https://stackoverflow.com/) - basic explaining 
* [Bootstrap 5](https://www.w3schools.com/bootstrap5/bootstrap_get_started.php) - for design and placement
* [PEP8](http://pep8online.com/) - for testing and validating the code.
* [Google Fonts](https://fonts.google.com/about) - for the font of the text


## Testing

### Lighthouse

* This is the read from lighthouse:

![image](/static/css/images/lighthouse1.png)
![image](/static/css/images/lighthouse2.png)
![image](/static/css/images/lighthouse4.png)

### Manual testing

* Only the admin can make a post puplished.
* If the user try to create a account, a text is shown if they havn't filled in the form correct.
* It is not possible to add a post unless the user has an account.
* The user can like all blogpost if they have an account and are logged in.
* The user can only delete/edit their own blogpost.
* The admin/staff can delete/edit all posts.

### Bugs

* 

## Deployment

### [Elephantsql](https://www.elephantsql.com/) 

* Heroku needs sql's to work
* ElephantSQL will manage administrative tasks of PostgreSQL, such as installation, upgrades to latest stable version and backup handling.
* It automates every part of setup and running of PostgreSQL clusters.

1. Log into Heroku 
The first step to creating a free PostgreSQL database is to log in to Heroku. To create a new database on Heroku, an app must first be created within the personal dashboard. 

2. Create a new Heroku app 
Once logged in to Heroku, navigate to the personal app dashboard to create a new Heroku app. Simply click the Create new app button, which should be located on the top-right corner of the dashboard. 

3. Add a PostgreSQL database 
After creating the new app, it's time to attach a PostgreSQL database to it. Simply navigate to the Resources tab located in the header of the app's dashboard. Add the ElephantSql and a free PostgreSQL database has now been successfully created. 

### [Github](https://github.com/) 

* When logging into github, navigate to the settings tab
* Here you can find pages down on the left side
* A new page will load which will present the branch to master or main, and then the save option
* Once the save button has been clicked and the page is reloaded there will be a link to the deployed site.

### [Heroku](https://www.heroku.com/) Deployment:

* Ensure your requirements.txt file has the required dependencies. To do this you can use the following
code in your IDE: pip3 freeze > requirements.txt
* Create or login to you Heroku account
* Navigate to Dashboard
* Click and select "Create app" in the middle of the page
* Enter a unique name for you app
* Select region and the "create app"

### App deployment
* Navgiate to the deploy section
* Scroll down to the "deployment method" and select "Github"
* Authorise the connection
* Also important to make sure you have the right config variables applied, these change the way the app behaves. 
* Go to the settings tab and then click reveal config vars
* Add the following config vars:
* * SECRET_KEY: (Your secret key)
* * DATABASE_URL: (This should already exist with add on of postgres)
* * EMAIL_HOST_USER: (email address)
* * EMAIL_HOST_PASS: (email app password)
* * CLOUNDINARY_URL: (cloudinary api url)
* Search for the repository name you've chosen
* Make sure you have selected the correct branch (master/main), and select the method you desire.

## Credits 

### Content

* I used Code Institute's I Think Therefore I Blog (walkthrough project) for guidance with code structure and deployment steps. It was really helpful and helped me alot along the way.

### Acknowledgements
* This Love Barista Blog was created as Portfolio Project 4 for the the Full Stack Software Developer diploma by the [Code Institute](https://codeinstitute.net/).
* I would like to thank the tutors at code institute for being extremely helpful considering my many questions and to my partner who helped me with mental support. And once again, thanks to my cousin for helping me with so many things!


Hanna Berggren, 2023
