# DjangoApi
Django api for user authentication

# Routes:
1.  /register : Post user data (name,email,password,username,mobile)
2.  /login :  Post email and password (api returns the user details after authentication)

# install dependencies
pip3 install -r requirements.txt

# start server
python manage.py runserver


# EXAMPLES


## REGISTER REQUEST AND RESPONSE

{
    "name": "jojo",
    "email": "abcde@gmail.com",
    "mobile": "9876543216",
    "password": "abcd1234",
    "username":"eliotte"
}

{
    "status": "REGISTRATION SUCCESS"
}


## LOGIN REQUEST AND RESPONSE

{
    "username":"eliotte",
    "password": "abcd1234"
}

{
    "status": "OK",
    "name": "jojo",
    "mobile": 9876543216,
    "email": "abcde@gmail.com"
}
