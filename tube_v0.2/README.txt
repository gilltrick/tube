nJoyPorn - Version: 0.2
Date: 27.05.2022
Author: Patrick Gillmann

Purpose of this application:
What is nJoyPorn?
    Its a tool to create tubes for adult content.
    You can set it up in a way that it automaticly searches for new content based on user behavior
    You get a full stack application.
        1) Webserver
        2) Databases
        3) Scraper

1) Webserver:
    Its a flask driven web server 
    Login page
    Search page
    Result page
    Video-Player page

2) Databases
    a) Main database
    b) Analytical database
    c) PornHub database
    d) Fapster database
    e) ExPornToons database
    f) User database
    g) Comments

    a) Main database:
        This database is for managing your local content:
        -Add local content to this database
        -You can edit data later on
        -Create Thumbnails
        -data ready to use in the frontend

    b) Analytical database
        This database is to analyse what happens on your tube
        -Pornstar data like charts, highscore, viewcount, ratings
        -Categorie data like charts, highscore, viewcount, ratings
        -Video data like charts, highscore, viewcount, ratings
    
    c) PornHub database
        This is a module for the main database
        -Fits the need for pornhub data
        -Serves data management for the pornhub-webscraper
    
    d) Fapster database
        This is a module for the main database
        -Fits the need for fapster data
        -Serves data management for the fapster-webscraper
    
    e) ExPornToons database
        This is a module for the main database
        -Fits the need for exPornToons data
        -Serves data management for the exPornToons-webscraper 
    
    f) User database
        This is a module for the main database
        -Manage users
        -You can use this to serve premium and non premium content

    g) Comments
        Write a comment for the content
        Comments are relatet to content for analytics

3) Scraper
    a) Pornhub-Scraper
    b) Fapster-Scraper
    c) ExPornToons-Scraper

    a) Pornhub-Scraper
        Its part of the pornhub database module
        Scrape data and store it ready to use for your frontend
        -search for keywords
        -serach by dictionary
        -search by combination of both
        -search in different depth steps

    b) Fapster-Scraper
        Its part of the fapster database module
        Scrape data and store it ready to use for your frontend
        -search for keywords
        -serach by dictionary
        -search by combination of both

    c) ExPornToons-Scraper
        Its part of the pornhub database module
        Scrape data and store it ready to use for your frontend
        -search for keywords
        -serach by dictionary
        -search by combination of both
        -search in different depth steps

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