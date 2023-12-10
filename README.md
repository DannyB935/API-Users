# API Users
This API is build using Flask. It just for testing when I want to try another front-end framework and I need some back-end info.

## Modules I've installed into my virtual env
- `Flask`
- `Flask-Cors`
- `psycopg2`: to connect to postgresql
- `pyjwt`: for handling sessions
- `python-dotenv`: env variables
- `pytz`: get timezone for tokens

I also left a .sql file to restore my DB. The module list could be expanded during the time.

Instalation
-----------
You can create a virtual enviroment or just install the packages using the `requirements.txt` file usign the next command:

```
pip install -r requirements.txt
```

Also you need to create a `.env` file to use the API with the next values:
- `DB_HOST` : Database host
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_PORT`
- `SECRET_KEY`: To create JSON Web Tokens

After that you can start the API on the port 5000 with the next command:
```
python src/app.py
```

# Routes

| Route | Method | Recieves | Returns | Performs | Error |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `/test` | GET | Nothing | String message to test | Just to test the API is working |
| `/api/users/` | GET | Bearer JWT token by Auth header | JSON list containing all users in DB | To get all the existing users in DB | ```{"status": "error", "message": "You have no access into this route"}``` |
| `/api/users/newc/` | POST | JSON containing all users data: ```{"username":'', "name":'', "lastName":'', "password":'', "age":0}``` | JSON with status "ok if the user could be created" | Route to create a new common user (not admin) | ```{"status": "error", "message": "The username already exist"}``` |
| `/api/users/newa/` | POST | Same as the previous | Same as the previous | Route to create an administrator | Same as the previous |
| `/api/users/delete/<id>` | PUT | User's id by URL | JSON indicating if the user could be deleted | Deletes a user setting its column "deleted" to true. | ```{"status": "fail", "code": 500, "message": str(e)}``` | 
| `/api/users/login/` | POST | JSON containing just User's username and password | Returns JSON containing JWT, username and role | Gets User's data and returns a JWT for Auth | ```{"status": "error", "message": "The user doesn't exist or the credentials are wrong"}``` |
| `/api/users/security/` | GET | Bearer JWT token by Auth header | JSON indicating you have access into the route | Route to test JWT auth | ```{"status": "error", "message": "You have no access into this route"}``` | 