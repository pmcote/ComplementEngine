%Example database so that alison can implement it anytime


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