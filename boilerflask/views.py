from flask import Flask, render_template, request, session, redirect, url_for
from boilerflask import app, facebook
from facebook_helper import *
import requests
import urllib
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
            firstNAME = facebook_profile['first_name']
            lastNAME = facebook_profile['last_name']
            userNAME = firstNAME + lastNAME
            user = User(user_id=userID, user_token=session.get('oauth_token')[0], user_name=userNAME)
            user.save()
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

    

    res = requests.get("https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials" % (app.config['FACEBOOK_APP_ID'], app.config['FACEBOOK_APP_SECRET']))
    app_access_token = res.content.split('=')[1]
    param_string = urllib.urlencode({"access_token":app_access_token, "template":"GURL I KNOW YOU WANT THIS DICK!"}, True) #these have to be encoded in the url, urllib does this for us :-)
    print 'param_string is'
    print param_string
    user_id = '1505822341' # my user id
    res = requests.post("https://graph.facebook.com/%s/notifications?%s" % (user_id, param_string))
    print res.content

    return "TEST"









