# Bohemian Estates International Client repoting system
![BES](https://res.cloudinary.com/dontkrfjd/image/upload/v1654698504/responsive_akitqp.png)

# Table of content



# Background
Given the area of business the company, Bohemian Estates International s.r.o. is in. There is a strong demand for renting, opose to owning. Because of rising prices and rates on mortgages, there is a strong expectations that business growth will continue and may even speed up. Therefore there is a demand for CRM for the company to keep track of new incoming clients and for growing team and its' staff members.

# Mission statement
Provide a system which will help to easily keep track of a lead communications and making closing easier.

# Target audience
There is a small team of 5 people right now, will be most likely doubling within a year period.

# Interviews
I carried out short interviews with the staff members. Expecially with members of saleforce. All people interviewed will be *Users*.

# Staff members
There are details of staff members interviewed.

| Name | Age | position | experience |
| -- | -- | -- | -- |
| Yury Vachugov | 35 | real-estate broker | 3.5 years |
| Robert Poppl | 38 | sale manager | 18 years |
| Katerina Hanzlik | 45 | real-estate broker | 6 months |
| Lukas Pohorsky | 42 | real-esate broker | 2 years |

## staff member goals
From the resulting interviews, the user goals have been defined:


# staff member stories


## staff member requirements and expectations
### Requirements
* Simple and well laid out
* Visually appealing
* Clean and modern looking
* Easy to create a lead in just a few clicks
* Responsive desing is required, mobile first, as users will be viewing the site mostly on mobile phones outside the office.

### Expextations
* I expect to use the application on any size device without the experience affected
* I expect that when I created a lead I can see it has been created.

# Wireframes

Design was created with mobile focus first

* Landing page mobile - created with very simple design, with a feature of changing heading.
![landing-page mobile](https://res.cloudinary.com/dontkrfjd/image/upload/v1654698505/mobile_phone_landing_page_cid5ef.png)

 * Landing page big screen
![landing-page big screen](https://res.cloudinary.com/dontkrfjd/image/upload/v1654698504/big_screen_landing_page_rl8f92.png)

* login page mobile - login page was created with a form and a button
![login page mobile](https://res.cloudinary.com/dontkrfjd/image/upload/v1654698504/mobile_login_tknllh.png)

* login page - big screen
![login page big screen](https://res.cloudinary.com/dontkrfjd/image/upload/v1654698504/big_screen_login_cse0e8.png)

* Lead list mobile- created with simple rows of leads with links to get to lead detail, update and deleting
![lead list mobile](https://res.cloudinary.com/dontkrfjd/image/upload/v1654698505/mobile_lead_detail_rm23rb.png)

* Lead list big screen
![lead list big screen](https://res.cloudinary.com/dontkrfjd/image/upload/v1654698505/big_screen_lead_list_twhhod.png)

* forms 
all forms are created with the same design forms are used in this project to make changes to everything (leads, agents etc...)
![form mobile](https://res.cloudinary.com/dontkrfjd/image/upload/v1654698505/mobile-form_qyfjzl.png)

* form big screen
![form mobile](https://res.cloudinary.com/dontkrfjd/image/upload/v1654698504/big_screen_login_cse0e8.png)




## Design choices
Because this project is being created for Bohemian Estates International and the requirements include the need for it to be the same as existing design, following design choices will be based on this.

### Fonts
As always, with Bohemian Estates International projects, I will be using Ubuntu which I used from [Google Fonts](https://fonts.google.com/specimen/Ubuntu)

#### Content
Using font weight of 400.

#### Headings
I used color #242f62 with various font sizes. As an example shown on a picture below.
![heading](https://res.cloudinary.com/dontkrfjd/image/upload/v1654699275/leads-heading_v0kqmc.png)

### Colors
![colors](https://res.cloudinary.com/dontkrfjd/image/upload/v1654698505/palet_color_uu8gtm.png)

# Structure
## App flow
The flow of the application is following.
When a user creates an account (signs up), is considered an organiser (manager) who is supposed to manage his team as well as leads. 

The organiser is the only user that can see unassigned leads, can assign them to each agent.
![unassigned-leads](https://res.cloudinary.com/dontkrfjd/image/upload/v1654701439/assigned_lead_dzj4bc.png) 

The organiser is the only user can create and delete a lead.
![lead create](https://res.cloudinary.com/dontkrfjd/image/upload/v1654701659/lead-create_kmgyak.png)
![lead delete](https://res.cloudinary.com/dontkrfjd/image/upload/v1654707280/lead-delete_z5h0mt.png)


The organiser is the only user who can see agent - navbar link, agent list and can create or delete an agent
![navbar organiser](https://res.cloudinary.com/dontkrfjd/image/upload/v1654701439/unassigned-leads_oshsxp.png)
![agent create](https://res.cloudinary.com/dontkrfjd/image/upload/v1654701658/agent_create_lfg4bf.png)
![agent delete](https://res.cloudinary.com/dontkrfjd/image/upload/v1654707280/agent-delete_kqtnsv.png)



## Models

### Users
predefined AbstracUser - added:

| Name | Type | Other Details |
|--|--|--|
| is organiser | BooleanField | True |
| is agent | BooleanField | False |


### USerProfile
| Name | Type | Other details |
|--|--|--|
| user | OneToOneField | on delete CASCADE |


### Lead
| Name | Type | Other Details |
|--|--|--|
| first name | Charfield | max length 20 |
| last name| Charfield | max length 20 |
| age | Intergerfield | deafault 0 |
| address | Charfield | max length 20 |
| phone | Charfield | max length 20 |
| organisation | ForeignKey | on delete CASCADE |
| agent | ForeignKey | on delete SET NULL |
| category | ForeignKEy | on delete SET NULL |
| email | Emailfield |  |
| description | textfield|  | 


### Agent
| Name | Type | Other Details |
|--|--|--|
| user | OneToOneField | on delete CASCADE |
| organisation | ForeignKey | on delete CASCADE |


### Category
| Name | Type | Other Details |
|--|--|--|
| name | CharField | max length 30 |
| organisation | ForeginKey | on delete CASCADE |

# Features
Landing page - created with very simple design, with feature of changing heading.
## Heading
![landing-page](https://res.cloudinary.com/dontkrfjd/image/upload/v1654707277/Animation_mbvv0j.gif)


## Empty leads
 if there are no leads available, message is displayed to inform, there are currently no leads available
![no-leads](https://res.cloudinary.com/dontkrfjd/image/upload/v1654761203/no_leads_xchens.png)


## Links
Navigation links are created to navigate a user thru updating, creating and deleting processes
![links](https://res.cloudinary.com/dontkrfjd/image/upload/v1654707277/lead-detail-links_gii2r8.png)


## Messages
Messages are displayed for continual feedback to the user on their interactions and follow the same layout for both mobile and desktop designs. These interactions include:

* Sign up
![sign-up-message](https://res.cloudinary.com/dontkrfjd/image/upload/v1654761204/message-signup_cn0l1e.png)

* Create a lead
![lead-create-message](https://res.cloudinary.com/dontkrfjd/image/upload/v1654761203/messages-lead-created_qn4rtr.png)

* Create an agent
![create-agent-message](https://res.cloudinary.com/dontkrfjd/image/upload/v1654761203/message-agent-created_kagobs.png)



## Authentication

The authentication process for the application has three parts.

* Sign Up
* Sign In
* Log out

### Sign Up
The signup process requests three required fields from the user:

* Username
* Password
* Password confirmation

![Sign Up Form](https://res.cloudinary.com/dontkrfjd/image/upload/v1654709117/SignUp_bytmsk.png)


### Sign In
The sign-in form requires only two fields to be entered. 

* Username
* Password

![Login Form](https://res.cloudinary.com/dontkrfjd/image/upload/v1654709117/login_bdrkyz.png)

### Log out

![Logout](https://res.cloudinary.com/dontkrfjd/image/upload/v1654709117/Logout_qzjcjf.png)


## buttons
I used four types buttons to navigate the site 

![Logout](https://res.cloudinary.com/dontkrfjd/image/upload/v1654709684/logout-btn_jj3u5s.png)
![red](https://res.cloudinary.com/dontkrfjd/image/upload/v1654709684/red_btn_dhz6ro.png)
![blue](https://res.cloudinary.com/dontkrfjd/image/upload/v1654709684/blue-btn_pnbtn0.png)




## Features to be implemented
* FollowUp
     * this feature would allow users to update what is going with a lead easire then just thrue Categories

* Unassigned lead delete
    * the button allowing unassigned lead to delete stright away should be implemented

* email communication
    * I wasnt able to finish email communication and process for password reset



# Technologies used

## Languages
| Languages | Description | Link |
|--|--|--|
|HTML|[HTML](https://en.wikipedia.org/wiki/HTML5 "HTML") | for the structure of the site
|CSS|[CSS](https://en.wikipedia.org/wiki/CSS "CSS") | for the design of the site
|JavaScript|[JavaScript](https://en.wikipedia.org/wiki/JavaScript "JS") | for the design of the site
|jQuery|[jQuery](https://jquery.com/ "jQuery") | for animations in the site
|Python|[Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python") | for the backend interactions
|Markdown|[Markdown](https://en.wikipedia.org/wiki/Markdown) | for the content in my README file


## Libraries and Frameworks
| Libraries / Frameworks | Description | Link |
|--|--|--|
|Django|Database Driven Framework| [django](https://en.wikipedia.org/wiki/Django_(web_framework) "django")|
|gunicorn|HTTP Interface Server|[gunicorn](https://en.wikipedia.org/wiki/Gunicorn "gunicorn")|
|psycopg2| Database adaptor | [psycopg2](https://wiki.postgresql.org/wiki/Psycopg "psycogg2")
|cloudinary |Image management|[cloudinary](https://cloudinary.com/ "cloudinary")|
|django auth|User authentication|[auth](https://docs.djangoproject.com/en/3.2/topics/auth/ "auth")|


## Tools
| Tools | Description | Link |
|--|--|--|
| Google Fonts| Fonts |[Google Fonts](https://fonts.google.com/ "Fonts")|
| ColorMind|Colour pallet| [coolors](http://colormind.io/ "colormind")|
| GitPod | Development environment |[Gitpod](https://www.gitpod.io/ "Gitpod")|
| Balsamic | Wireframes |[Balsamic](https://balsamiq.com/wireframes/ "Balsamic")|
| Font Awesome | Icons |[Font Awesome library](https://fontawesome.com/ "Font Awesome")|
| W3C | Markup Validation | [W3C Markup Validation Service](https://validator.w3.org/ "W3C")|
| W3C | CSS Validation | [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C")|
| PEP8 | Python Validation | [PEP8](http://pep8online.com/ "PEP8")|
| JSHint | JavaScript and JQuery Validation | [JSHint](https://jshint.com/ "JSHint")|



## Bugs



# Deployment

This project was created using GitHub and the code was written using Gitpod. This project is also deployed to Heroku with Heroku deployment set to *Enable Automatic Deploys*. This means that every time that the repository was pushed to, Heroku was updated also.

The live link to the application can be found [here]()

## Local Deployment

As Gitpod was the IDE that was used to create the project, the following local deployment steps are specific to Gitpod.

### Cloudinary
* Visit Cloudinary by following this [link]()
* Click on the *Sign Up For Free* button
* When the account is created, you should see the *API Environment variable*, we will need this for a later process.

### GitHub
* Visit Github by following this [link]()
* Create an account or log in


* In the terminal run
```
pip3 install -r requirements.txt
```
* In the root directory create a file called **env.py** and add the following content, the content of these, must match the Config Vars in the Heroku deployment section

```py
import os

os.environ['DATABASE_URL'] = "FROM HEROKU DEPLOYMENT SECTION, DATABASE_URL CONFIG VAR"
os.environ['SECRET_KEY'] = "FROM HEROKU DEPLOYMENT SECTION SECRET_KEY CONFIG VAR"
os.environ['CLOUDINARY_URL'] = "API ENVIRONMENT VARIABLE REMOVE 'CLOUDINARY_URL=' FROM BEGINING"
os.environ['DEVELOP'] = '1'


* Add the env.py file to the .gitignore file to ensure that its contents are not made public

* Migrate the database models with the following command in the terminal

* Create a superuser and set up the credentials with the following command
```
python3 manage.py createsuperuser
```

* Run the application locally with the command
```
python3 manage.py runserver



### Deployment via Heroku
* Visit [heroku.com]()
* Create a new account or sign in
* From the dashboard, select **New** and then **Create new app**
* Enter an individual app name into the text box, select a region from the dropdown and then press **Create app**
* A Heroku app has now been created and the **Deploy** tab is opened. 
* Open the *Resources* tab and in the search bar for *Add-ons* type *Postgres*
* Select *Heroku Postgres*, on the popup, ensure the dropdown is set to *Hobby Dev - Free* and then *Submit Order Form*
* Open the *Settings* tab and then click on the *Reveal Config Vars* button and the database_url should be populated.
* Fill out the rest of the config vars with the content of the table below by filling out the *Key* and *Value* and clicking on *Add* for each entry 


* In the buildpacks section of the settings tab, click on **Add Buildpack**, select **python** and then save changes
* Open the **Deploy** tab
* In the deployment method section, select **GitHub** and confirm the connection.
* Enter the repo-name into the text box and click **Search**. When the correct repo appears below, click **Connect**
* Return to the Gitpod workspace and in the root directory create a file called *Procfile*
* In the *Procfile* enter the following line including your project name
```
web: gunicorn YOUR_PROJECT_NAME.wsgi
```
* Add and commit to GitHub
```
git add .
git commit -m "commit message goes here"
git push
```
* Add your Heroku app URL to ALLOWED_HOSTS in your settings.py file
```
ALLOWED_HOSTS = ['YOUR_PROJECT_NAME.herokuapp.com', 'localhost']
```


## Code Validation

### HTML
The HTML code within the application has been validated by [W3C Markup Validation Service](https://validator.w3.org/ "W3C"). Pages were put through the validator seperatly and the results can be seen below.

* Landing page  
![validator html landing](https://res.cloudinary.com/dontkrfjd/image/upload/v1654867236/w3c-validator-landing-page_hqr5hp.png)

* Lead List
![validator html lead list](https://res.cloudinary.com/dontkrfjd/image/upload/v1654867236/w3c-validator-lead-list_rmj2yw.png)


### CSS
The CSS code within the application has been validated by [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C"), and the results can be seen below.
![css validator](https://res.cloudinary.com/dontkrfjd/image/upload/v1654867236/css_validator_zzfgur.png)


### Python
The Python code within the application has been validated by [PEP* Validation Service](http://pep8online.com/ "PEP*"). Files were put through the validator separately and the results can be seen below.
![Sign Up Form](https://res.cloudinary.com/dontkrfjd/image/upload/v1654709117/SignUp_bytmsk.png)

#### lead application

* views
![leads views pep8](https://res.cloudinary.com/dontkrfjd/image/upload/v1654867236/pep8-wiews-leads_imkfcj.png)
* Models
![models pep8](https://res.cloudinary.com/dontkrfjd/image/upload/v1654867236/pep8-models-views_uuaglm.png)
* forms
![leads forms pep8](https://res.cloudinary.com/dontkrfjd/image/upload/v1654867236/pep8-forms-leads_ueuvo4.png)

#### agents application

* views
![agents views pep8](https://res.cloudinary.com/dontkrfjd/image/upload/v1654867236/pep8-views-agents_npwvrc.png)
* forms 
![agent forms pep8](https://res.cloudinary.com/dontkrfjd/image/upload/v1654867237/pep8-forms-agents_tyd5hf.png)












