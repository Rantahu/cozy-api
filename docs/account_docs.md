## Accounts
This page holds all the various API calls involving account information.
There are two different objects within this project that hold information for accounts.
Django's built in account system, as well as Profile, which is an extension of the Django
built in account system. Account API calls are made up of two different set of URLs, the ones found in the ```accounts``` app, and URLS created by the third-party apps ```allauth```, ```rest_auth```, ```rest_auth.registration```, and ```rest_framework.authtoken```. The URLs within the accounts app are mostly used for getting user information, while the others are mostly used for authentication purposes.

-```/profile/``` : Returns a list of Profiles
```json
[
    {
        "id": 1,
        "username": "test",
        "profileImg": null
    },
    {
        "id": 2,
        "username": "x",
        "profileImg": null
    },
    {
        "id": 3,
        "username": "meme",
        "profileImg": null
    }
]
```
-```profile/USERNAME```: Returns information of a specific user
```json
{
    "id": 2,
    "username": "x",
    "profileImg": null,
    "location": "Nowhere",
    "bio": ""
}
```
-```profile/edit/USERNAME```: Allows for either an admin or the specific user able to edit their info. The following are the feilds that can be changed
```json
{
    "username": "x",
    "profileImg": null,
    "location": "Nowhere",
    "bio": ""
}
```
-```register```: API post call for people to create an account.
```json
{
    "username": [
        "This field is required."
    ],
    "email": [
        "This field is required."
    ],
    "password": [
        "This field is required."
    ]
}
```
-```api-token-auth```: POST auth for username and password and return a auth token
-```api-token-refresh```: POST a token and refresh it
-```api-token-verify```POST request to verify a token. 
