# **Love Barista**

# Frontend Testing

## Table Of Contents:
1. [Validator Testing](#vadilidator-testing)
    * [Html](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Python](#python)
    * [Lighthouse](#lighthouse)
2. [User Story Testing](#user-story-testing)
3. [Responsiveness Testing](#responsivness-testing)
4. [Browser Compatibility](#browser-compatibility)
4. [Manual Testing](#manual-testing)
5. [Bugs](#bugs)

## Validator Testing

### W3C HTML validator
The site pages were run through the [W3C validator]([https://validator.w3.org/](https://validator.w3.org/nu/?showsource=yes&doc=https://8000-hannaberggr-lovebarista-4l76yoe8zfr.ws-eu101.gitpod.io/)) to check for any issues and HTML syntax errors. 
Given the presence of Django template code in the HTML templates, the rendered HTML was copied from the Chrome browser by right clicking, selecting 'view page source' for each page of the site and then pasting directly into the HTML validator.
No errors, but one warnings were to be found.

![W3C HTML](static/css/images/htmlchecker.png)

### CSS
- The CSS stylesheet was put through the [W3C validator](https://jigsaw.w3.org/css-validator/)  to check for errors.
- No errors were found.

![W3C CSS](static/css/images/w3c.png)  

### JavaScript
- The Javascript file was put through the [Jshint](https://jshint.com/) to check for errors. 
- No errors, but five warnings was found.

![JS Validator screenshot](static/css/images/jshint.png)

### Python
- Issues with the custom python code were fixed on an ongoing basis during development using the pycodestyle tool, which was installed to the IDE, GitPod.
- The code was also tested to check for errors using **Code Institutes pep8 online** website, [PEP8](https://pep8ci.herokuapp.com/). No errors returned as you can see from the screenshots below.

<details>
    <summary>admin.py</summary>  
    
![Admin PEP8 validator](static/css/images/pep8admin.png)  
</details>
  
<details>
    <summary>forms.py</summary>  
    
![Forms PEP8 validator](static/css/images/pep8forms.png)  
</details>  

<details>
    <summary>models.py</summary>  
    
![Models PEP8 validator](static/css/images/pep8models.png)
</details>  
  
<details>
    <summary>urls.py</summary>  
    
![Urls PEP8 validator](static/css/images/pep8urls.png)
</details>  

<details>
    <summary>views.py</summary>  
    
![Views PEP8 validator](static/css/images/pep8views.png)
</details>  

[Back to the top](#table-of-contents)
- - - 


---
[Back to the top](#table-of-contents)

## User story testing

##### Navigation
*As a user I can use a navbar so that I can easily navigate on the website*
 - The Navigation at the top of the page is easy to navigate, when hovering a page in the navbar the page name gets highlighted wich helps the user to see wich page they are entering.

#### Register
*As a User I can create an account so that I can add my own recipes and comment on other users recipes*
 - In the Navigation bar at the top of the page, if a User clicks on the Register link, they will be brought to the registeration page wehere they can sign up, once they sign up they will be able to access full functionality of the site.
 
#### Signin | Signout
*As a User I can Sign-in/Sign-out so that I can access all of the futures on the website when signed in and to maintain personal security by signing out*
 - When a User is not logged in the login link will be visible to the far right in the navigation bar, the same link will change to logut when the user is logged in.
 - When the User enters their login credentials they wil be able to access full fuctionality of the site. When the user is logged out they will not have full access on the site and their account will be secure.

#### View a Post
*As a User I can view the list of posts so that I can choose one to read*
- The user is able to click the post on the mail page and this will take them to the post page where they can view a list of recipes.
- If they wish to view one The user must be signed in to view the post details as if they are not signed in the Read More button will be disabled.

#### Add a Post
*As a User I can add a recipe so that other users can view it, like it and add comments to it.*
- When a user is signed in they are able to click on the Add Post button at the Post page, which will bring them to the Add Post page where they can upload their post.

#### Edit | Delete a Post
*As a User I can Edit/Delete my post so that I can update my blogpost after posting them to the website*
- When viewing a post that the User has uploaded in the top right corner they have a choice to either delete or edit the post. A user can only edit or delete a post they are the owner for.

#### Like | Unlike posts
*As a User I can like/unlike posts so that I can give other users feedback without writing a comment.*
- On the post details there is a like button below the image, it is a Love heart that is empty outline when not liked and then is filled when liked, beside it displays the number of people that like the post. A User must be logged in to access this functionality.

#### Add comments
*As a User I can comment on my own and other users posts so that I can provide feedback to other users*
- When a user is signed in and they are on the post details page for a particular post, at the bottom of the page there is a comment section where they can add a comment.

#### Edit | delete comments
*As a User I can choose to edit/delete comments so that I can update my comments after posting them to the website*
- The User is able to edit or delete any comment that they have created by clicking on the edit or delete button in the right hand side of that comment.

---
[Back to the top](#table-of-contents)

## Responsiveness Testing

The responsive design tests were carried out manually throughout the build using Google Chrome Dev Tools. As this is primarily a browser based platform I based the main design around a desktop view, adding responsive design for tablet and mobile devices as well. 

During the testing process I also used the [Responsive Design Checker](https://www.responsivedesignchecker.com/) website to simulate the website on several other devices. Here is what I found:

### Mobile Devices

||<p>iPhone 6/6s/7</p><p>375 x 667</p>|<p>Samsung Galaxy S5/6/7</p><p>360 x 640</p>|<p>Google Pixel/Nexus 5</p><p>411 x 731</p>|
| :- | :-: | :-: | :-: |
|Render|Pass |Pass|Pass|
|Images|Pass|Pass|Pass|
|Links|Pass|Pass|Pass|

### Tablet Devices

||<p>Amazon Kindle Fire</p><p>768 x 1024</p>|<p>Samsung Galaxy Tab 10</p><p>800 x 1280</p>|<p>Apple iPad Pro</p><p>1366 x 1024</p><p></p>|
| :- | :-: | :-: | :-: |
|Render|Pass|Pass|Pass |
|Images|Pass|Pass|Pass|
|Links|Pass|Pass|Pass|

### Desktop Devices

||<p>24“ Desktop</p><p>1920 x 1200</p>|<p>19” Desktop</p><p>1440 x 900</p>|<p>10” Notebook</p><p>1024 x 600</p>|
| :- | :-: | :-: | :-: |
|Render|Pass|Pass|Pass|
|Images|Pass|Pass|Pass|
|Links|Pass|Pass|Pass|

### Browser Compatibility 

Happening was tested on the following browsers:

- Google Chrome
- Mozilla Firefox

Appearance and functionality appear to be consistent throughout all browsers. 
---
[Back to the top](#table-of-contents)

## Manual Testing

#### Navigation
| Feature               | Test Performed                                                        | Result  |
|-----------------------|-----------------------------------------------------------------------|---------|
| Logo    | Clicking on the logo redirects the user to home page.                               | Pass    |
| Home    | Clicking on Home link brings user to the home page.                                 | Pass    |
| Register | When signed out clicking on the Register link, brings the user to the              |         |
Registeration page.                                                                             | Pass    |
| Login | When signed out, clicking on the Login link, brings the user to the login page.       | Pass    |
| Logout | When signed in, clicking on the logout link, brings the user to the logout page.     | Pass    |
| Correct links display | When a user is signed in or out the correct links display for both.   | Pass    |
| Responsiveness | Checked to make sure it changes to burger menu on smaller devices.           | Pass    |

#### Footer
| Feature               | Test Performed                                                        | Result  |
|-----------------------|-----------------------------------------------------------------------|---------|
| External links | Clicking on social media links opens on a new page.                          | Pass    |
| Displays correctly on all pages | Made sure it displays correctly on all pages.               | Pass    |
| Responsiveness | Checked to make sure link icons display correctly on smaller devices.        | Pass    |

#### Home
| Feature               | Test Performed                                                        | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | The page is responsive on several different devices, browsers and screen widths. | Pass      |
| Background Image | Checked to make sure background image loads correctly.                  | Pass      |
| About Us Section | Make sure section displays correctly on all device widths               | Pass      |

#### Posts
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | The page is responsive on several different devices, browsers and screen widths. | Pass      |
| Posts   | Posts cards displays as expected.                                        | Pass      |
| Read more button | Signed In users can click the read more button under each recipe.       | Pass      |
| Read more button | Signed Out users can't click the read more button under each post.    | Pass      |
| Add post Button | An Add Post button is being displayed when the user is signed in.   | Pass      |
| 6 Posts Per Page | Not more than 6 posts per page is being displayed.                  | Pass      |
| Next button | A next button at the bottom of the page is being displayed if there is more than six recipes being displayed.      | Pass      |
| Back button | A back button at the bottom of the page is being displayed if the user is on the next recipe page. | Pass      |

#### Post Details Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | The page is responsive on several different devices, browsers and screen widths. | Pass      |
| Post Content   | The post content displays as expected.                                | Pass      |
| Edit Post   | If the user is the owner of the post they can click the edit button to edit their post. | Pass      |
| Delete Post | If the user is the owner of the post they can click the delete button to delete their post. | Pass      |
| Signed in user access | Only singed in users can access the recipe details page.           | Pass      |
| Like button   | A clickable like button is being displayed below the post.               | Pass      |
| Display total number of likes   | Displays the number of users that have liked the post. | Pass      |
| Comment Section  | Displays comments added to the comment section.                         | Pass      |
| Post Comment   | Allows users to post a comment and display it in the comment section.     | Pass      |

#### Add A Post Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | The page is responsive on several different devices, browsers and screen widths. | Pass      |
| Display form  | Every input field is displaying on the add a post form.                 | Pass      |
| Submit filled out form  | A user can fill out the form and click the submit button at the bottom of the page. | Pass      |
| Leave Image field blank on submission  | If the user leaves the image field blank the place holder image displays after submitting. | Pass      |
| Leave Input fields blank | The form won't submit if the user leaves required input fields blank, warnings will be displayed for the user. | Pass      |
| Submit Button | On click it will submit the post, and bring the user to the posts page where the newly added post can be seen. | Pass      |
| Cancel Button | On click it will bring the user back to the posts list.                  | Pass      |
| Success Message | Success message is displayed at the top of the screen when a user clicks Submit.  | Pass      |

#### Update A Post Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | The page is responsive on several different devices, browsers and screen widths. | Pass      |
| Display form  | All the input fields displays with the orginal post.                                  | Pass      |
| Update form  | When a user updates a post and clicks the submit button at the bottom of the page the post updates. | Pass      |
| Update Button | On click it updates the post, and brings the user to the posts page where the updated post can be seen. | Pass      |
| Cancel Button | On click it brings the user back to the recipes list.                  | Pass      |
| Success Message | A success message is displayed at the top of the screen when a user clicks update.  | Pass      |

#### Delete A Post Modal
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | The page is responsive on several different devices, browsers and screen widths. | Pass      |
| Yes Button | When the user clicks the yes button the post will be deleted.                 | Pass      |
| Cancel Button | When the user clicks the cancel button, the delete modal will disappear and the user will be back on the posts page.     | Pass      |
| Clicking Outside The Modal | When the user clicks anywhere ouside the modal the modal will disappear.    | Pass      |
| X  | When the user clicks on the X button at the top of the modal, the modal disappears.   | Pass      |
| Success Message | Success message is displayed at the top of the screen when a user clicks yes on the delete modal.  | Pass      |

#### Register Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | The page is responsive on several different devices, browsers and screen widths. | Pass      |
| Sign In link | Under the "already have an account section", the Sign in link redirects the user to the Login Page | Pass      |
| Submit Filled Out Form  | When the user fills out the sign up form and clicks the Signup button a new account is created. | Pass      |
| Leave Email Field Blank  | When the user fills out all the fields in the form except the optional email field and clicks submit a new account is created. | Pass      |
| Leave Username Field Blank| When the user fills out the form and leaves Username field blank, a warning messages appeare saying that the field most not be left blank, Sign Up is not approved.| Pass      |
| Leave Password Field Blank| When the user fills out the form and leaves Password field blank, a warning messages appeare saying that the field most not be left blank, Sign Up is not approved.| Pass      |
| Leave Password (again) Field Blank| When the user fills out the form and leaves Password (again) field blank, a warning messages appeare saying that the field most not be left blank, Sign Up is not approved.| Pass      |
| Signup with an already taken username| When the user register an account that already has the taken username, the sign upp fails and a warning messages appeare saying that a user with that username already exists. | Pass      |
| Signup Button | On click the signup button will submit the user details, log them in and redirect them to the home page. | Pass      |
| Success Message | Success message is displayed at the top of the screen when a user enters the correct details and clicks Sign Up. | Pass      |

#### Login Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | The page is responsive on several different devices, browsers and screen widths. | Pass      |
| Sign Up link | Under the "if you do not have an account" section, the Sign up link redirects the user to the Register Page        | Pass      |
| Leave Username Field Blank| When the user fills out the form and leaves Username field blank, a warning messages appeare saying that the field most not be left blank, Sign In is not approved.| Pass      |
| Leave Password Field Blank| When the user fills out the form and leaves Password field blank, a warning messages appeare saying that the field most not be left blank, Sign In is not approved.| Pass      |
| Sign In with unregistered account | If a User tries to sign in with an account that is not registered, a warning messages appeare saying that 'the username and/or password you specified are not correct'. The sig in will not be approved. | Pass      |
| Sign In Button | On click it will sign in the user if they have entered the right credentials. The user will get redirect to the home page. | Pass      |
| Success Message | Success message is displayed at the top of the screen when a user enters the correct credentials and clicks Sign in. | Pass      |

#### Logout Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | The page is responsive on several different devices, browsers and screen widths. | Pass      |
| Sign Out Button | When clicked it Signs out the user and redirect them to the login page.  | Pass      |
| Success Message | Success message is displayed at the top of the screen after clicking Sign Out to let the user know they have logged out. | Pass      |


---
[Back to the top](#table-of-contents)