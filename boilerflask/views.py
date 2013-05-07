from flask import Flask, render_template, request, session, redirect, url_for
from boilerflask import app, facebook
from facebook_helper import *
import requests
import urllib
import random
from boilerflask.models import *


@app.route('/', methods=['GET'] )
def index():
    if not 'oauth_token' in session:
        return redirect(url_for('login'))
    else:

        facebook_profile = facebook.get('/me')
        

        # ex = User.objects(username = 'Alisoniscute').first() #Also .all
        # print ex.username

        if facebook_profile.status == 200: #200 means success
            facebook_profile =  facebook_profile.data
            userID = facebook_profile['id']
            # firstNAME = facebook_profile['first_name']
            # lastNAME = facebook_profile['last_name']
            # userNAME = firstNAME + lastNAME

            user = User(user_id=userID, user_token=session.get('oauth_token')[0])
            user.save()


            for user in User.objects:
                print user.user_id
        else:
            print "get facebook/me failed"

        notifications = facebook.get("me/notifications")
        
        if notifications.status == 200: #200 means success
            notifications =  notifications.data
            #if you don't have notifications, run the notifier
            if notifications['data'] == []:
                notifier()
        else:
            print "get facebook/me/notifications failed"

    print "Profile:%s" % facebook_profile
    print "Notifications:%s" % notifications

    return render_template('index.html', facebook_profile=facebook_profile, notifications=notifications)

@app.route('/notifier', methods=['GET'] )
def notifier():
    if not 'oauth_token' in session:
        return redirect(url_for('login'))

    compliments_list = ["Baby, somebody better call God, cuz he's missing an angel!", 
                "Are you a tamale? Cause you're hot.", 
                "Apart from being sexy, what do you do for a living?",
                "Did it hurt? when you fell from heaven.",
                "Damn, if being sexy was a crime, you'd be guilty as charged!",
                "Baby, if you were words on a page, you'd be what they call fine print.",
                "Baby, you must be a broom, cause you just swept me off my feet.",
                "Did the sun come out or did you just smile at me?"]

    #Getting the access token to send notifications
    res = requests.get("https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials" % (app.config['FACEBOOK_APP_ID'], app.config['FACEBOOK_APP_SECRET']))
    app_access_token = res.content.split('=')[1]
    param_string = urllib.urlencode({"access_token":app_access_token, "template":random.choice(compliments_list)}, True) #these have to be encoded in the url, urllib does this for us :-)
    
    for user in User.objects:
        userId = user.user_id

        #sending a notification
        #user_id = '1505822341' # Paige's user id
        # userId = '1336202596' # Alison's user id

        res = requests.post("https://graph.facebook.com/%s/notifications?%s" % (userId, param_string))
        #print res.content

    return "HAVE MY BABIES"









