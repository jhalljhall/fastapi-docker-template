# edlight-tech-challenge

Justin Hall jhalljhall[at]gmail[com]

1. Open in Codespaces
2. run: `pip install -r requirements.txt`
3. create a .env file by copying the `.env.example` to the /app directory
4. change the **OPENAI_API_KEY** value in the .env to your key
5. run: `uvicorn main:app --reload`
6. Open port 8000 up to public visibility by going to the PORTS tab and right clicking the Private visibility setting. From the context menu toggle the visibility to Public
7. Open a browser tab and go to the public URL + "/docs#/ai" to access the FastAPI Swagger UI. Modify the .env file's PUBLIC_URL to the domain provided by Codespaces. Look at the .env.example for an example domain
8. Click the "Try It Out" button for the "analyse-image" endpoint
9. Click "Choose a File" from the file input field
10. Download an image like this one: https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg
11. Choose the newly downloaded file
12. View the message from the results of the OpenAI API call. It should contain a description of the image
13. Try another image. The call to OpenAI's API is protected by several defensive try/catch throw exception safe guards.
14. Create a User by going to "/docs#/users/register_user_api_v1_users_register_post". Provide an email and easy to remember pw like "changeme".
15. See long description below about Auth.
16. Follow Step 8 - 12 but this time choose the "analyse-image-protected" endpoint. It will use your newly created authenticated User bearer token for access.


# Some possible problems:
The database PostGreSQL Server might not start up in Codespaces or locally on Docker. If you open the repo in GitPod the sql server will start, but OpenAI doesn't seem to play nice with any of the saved images on Gitpod servers. Regardless of their permissions the Gitpod subdomains do not seem to be whitelisted on OpenAI's GPT-4-Vision-Preview API endpoints.

# Auth
The authentication of your first user will need an extra permission in the database. 
1. Navigate to the **default.session.sql** file and comment in the last two lines.
2. Choose to run the SQL from the small text at the top of the file. 
    - This will give your firstly created user the "super user" access and will now allow you to run the protected routes. 
    - Protected routes in the /docs Swagger UI have a lock icon next to the carrot on the far right. 
3. In order to Authenticate you will need to navigate to the top of the /docs page and click Authenticate. 
    - Use the email (even though it says username) and password you chose for your new user.
