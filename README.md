Compliment Engine
A Spring 2013 Software Design project by Paige Cote, Alison Berkowitz, and Jessica Diller
============

Our App:
Our Compliment Engine is designed to help ease the loneliness of the social web. Have you  ever logged in to Facebook and been dismayed that you have no notifications and nobody loves you? Do you feel like you have no friends on the internet? Well the Compliment Engine is here to help. The app periodically checks to see if you have any unread notifications, and if you are currently unloved it will send you a loving notification to boost your Web 2.0 ego.

App Design:
Our App has two main functions set that take care of the business that is boosting your ego. The first function set is initiated under our index page, which then has a cascade of functions that take care of registration and user-app authentication. Once a user has registered, the rest of the interactions are automated by a webscript that runs the notifier function periodically. The notifier function checks to see if each user has an unread notification, and if they don't (nobody loves them), the app sends them a random ego-boosting notification from our carefully researched list of compliments. 
The rest of our app is composed of HTML and Twitter Bootstrap CSS. Webscripts.io currently provides our webscripts service and our web domain is provided by heroku. 

To install requirements and use our code locally:
$pip install requirements.txt
And then clone our repository. Simple as that!

Self Feedback:
We are currently working on improving our web design. In a dream world we would add other automated social networking services on sites such as Twitter and Tumblr. We are most proud that we did not have to make any compromises to our project goals despite plenty of configuration challenges throughout the project.

We would like to thank our Professor, Dr. Jeffrey Carruthers, our NINJA Hannah B. Sarver, and Cory Dolphin for helping us through rough parts and answering our various questions.


