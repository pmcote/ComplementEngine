from flask import Flask, render_template, request, session, redirect, url_for
from boilerflask import app, facebook
from facebook_helper import *
from boilerflask.models import *

@app.route('/', methods=['GET'] )
def index():
    if not 'oauth_token' in session:
        return redirect(url_for('login'))
    else:

        facebook_profile = facebook.get('/me')
        userID = facebook_profile['id']
        firstNAME = facebook_profile['first_name']
        lastNAME = facebook_profile['last_name']
        userNAME = firstNAME + lastNAME
        user = User(user_id=userID, usertoken=oauth_token, user_name=userNAME)
        user.save()

        ex = User.objects(username = 'Alisoniscute').first() #Also .all
        print ex.username


        if facebook_profile.status == 200: #200 means success
            facebook_profile =  facebook_profile.data
        else:
            print "get facebook/me failed"


        notifications = facebook.get("me/notifications")
        
        if notifications.status == 200: #200 means success
            notifications =  notifications.data
        else:
            print "get facebook/me/notifications failed"

    print "Profile:%s" % facebook_profile
    print "Notifications:%s" % notifications

    return render_template('index.html', facebook_profile=facebook_profile, notifications=notifications)

@app.route('/notifier', methods=['GET'] )
def notifier():
    if not 'oauth_token' in session:
        return redirect(url_for('login'))
    notifications = facebook.get("me/notifications")
    
    if notifications.status == 200: #200 means success
        notifications =  notifications.data
    else:
        print "get facebook/me/notifications failed"

    return '%s' % notifications


