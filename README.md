nJoyPorn - Version: 0.2<br>
Date: 27.05.2022<br>
Author: Patrick Gillmann<br>
<br>
Purpose of this application:<br>
What is nJoyPorn?<br>
    Its a tool to create tubes for adult content<br>
    You can set it up in a way that it automaticly searches for new content based on user behavior<br>
    You get:<br>
        1) Webserver<br>
        2) Databases<br>
        3) Scraper<br>
<br>
1) Webserver:<br>
    Its a flask driven web server<br>
    Login page<br>
    Search page<br>
    Result page<br>
    Video-Player page<br>
<br>
2) Databases<br>
    a) Main database<br>
    b) Analytical database<br>
    c) PornHub database<br>
    d) Fapster database<br>
    e) ExPornToons database<br>
    f) User database<br>
    g) Comments<br>
<br>
    a) Main database:<br>
        This database is for managing your local content:<br>
        -Add local content to this database<br>
        -You can edit data later on<br>
        -Create Thumbnails<br>
        -data ready to use in the frontend<br>
<br>
    b) Analytical database<br>
        This database is to analyse what happens on your tube<br>
        -Actor data like charts, highscore, viewcount, ratings<br>
        -Categorie data like charts, highscore, viewcount, ratings<br>
        -Video data like charts, highscore, viewcount, ratings<br>
    <br>
    c) PornHub database<br>
        This is a module for the main database<br>
        -Fits the need for pornhub data<br>
        -Serves data management for the pornhub-webscraper<br>
    <br>
    d) Fapster database<br>
        This is a module for the main database<br>
        -Fits the need for fapster data<br>
        -Serves data management for the fapster-webscraper<br>
    <br>
    e) ExPornToons database<br>
        This is a module for the main database<br>
        -Fits the need for exPornToons data<br>
        -Serves data management for the exPornToons-webscraper <br>
    <br>
    f) User database<br>
        This is a module for the main database<br>
        -Manage users<br>
        -You can use this to serve premium and non premium content<br>
    <br>
    g) Comments<br>
        Write a comment for the content<br>
        Comments are relatet to content for analytics<br>
<br>
3) Scraper<br>
    a) Pornhub-Scraper<br>
    b) Fapster-Scraper<br>
    c) ExPornToons-Scraper<br>
    <br>
    a) Pornhub-Scraper<br>
        Its part of the pornhub database module<br>
        Scrape data and store it ready to use for your frontend<br>
        -search for keywords<br>
        -serach by dictionary<br>
        -search by combination of both<br>
        -search in different depth steps<br>
    <br>
    b) Fapster-Scraper<br>
        Its part of the fapster database module<br>
        Scrape data and store it ready to use for your frontend<br>
        -search for keywords<br>
        -serach by dictionary<br>
        -search by combination of both<br>
   <br>
    c) ExPornToons-Scraper<br>
        Its part of the pornhub database module<br>
        Scrape data and store it ready to use for your frontend<br>
        -search for keywords<br>
        -serach by dictionary<br>
        -search by combination of both<br>
        -search in different depth steps<br>
<br>
Get started

    #Install the app and downloading rquirements from requirements.txt
    python setup.py

    #Run the server
    python njoyporn.py

    #Visit your new tube
    http://localhost:5001

Set up a local database:

    #Copy the content you want to serve to your /static/storage/specials/
    #Run the main database application in terminal
    python database.py
    #Initialize the database
    --initdb
    #Add a video to the database
    --add
    #Enter data for at least:
        filename
        video-title
        create the Thumbnails
        save database
    #Check for data
    --printdb
    #Restart the server

Set up a webscraped database:

    #Chose and run a module
    python modulename.py
    #Initialize the database
    -initdb
    #Simple Search:
    -search
        enter keywords
        enter depth
        wait for it to complete
        save database
    #Check for data
    -printdb
    #Restart the server

Set up a users

    #Run the userdatabase module
    python userdatabase.py
    #Initialize the database
    -initdb
    #Add a new user
    -newUser
        enter username
        enter password
        enter email

Analytics

    #Run the analytics module
    python analytics.py
    #Initialize the database
    -initdb
    #Print data if available
    -print
        -video
        -categorie
        -actors
        -analytics
