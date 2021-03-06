# qlink

## Description
URL Shortener

### Installation
1. Create and activate a virtual environment and Clone the project `https://github.com/peterwade153/qlink.git`

2. Move into the project folder
   ```
   $ cd qlink
   ```

3. Install dependencies 
   ```
   $ pip install -r requirements.txt
   ```

4. Create a postgres database.

5. Create a `.env` file from the `.env_sample` file. 

6. Replace the variables in the sample file with the actual variables, such the database credentials and secret key.

7. Run migrations
   ```
   python manage.py migrate
   ```

8. To start server
   ```
   python manage.py runserver
   ```

8. To run tests
   ```
   pytest
   ```

### Endpoints

Request             | Endpoints                    |       Functionality 
--------------------|------------------------------|--------------------------------
POST                |  `/auth/login/ `             |  Login User. `payload`-`{"email:"new email", "password1":"password"}`
POST                |  `/auth/registration/`       |  Creates a new user. `payload`-`{"email:"new email", "password1":"password", "password2": "password" }` 
POST                |  `/auth/logout/`             |  Logout user
POST                |  `/api/shortner/`            |  Create shortened link `payload`-`{"original_url:"url" }` 
GET                 |  `/api/shortner/`            |  List short links for user
