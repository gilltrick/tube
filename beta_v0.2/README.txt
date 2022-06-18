nJoyPorn - Version: 0.4
Date: 09.06.2022
Author: Patrick Gillmann

Purpose of this application:
What is nJoyPorn?
    Its a tool to create tubes for adult content.
    You can set it up in a way that it automaticly searches for new content based on user behavior
    User can create an account, create a page to present them self, they can upload videos and choose if they want to sell them*
    User can buy ohter users videos and watch or download them
    You get a full stack application.
        1) Webserver
        2) Databases
        3) Scraper
        4) Web-GUI
        5) Cryptopayment

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

4 Web-GUI
    a) AdminPanle
       Here can the admin manage the users and content
    b) UserPanel
       Here can the user manage their page, favorites, purchased videos etc
       Create a user page:
        The user page is a landing page the user can create to summarize their content and present themselfs
        Other user will search on the main page click on a video. Your landing page is connected to that video
        If the user gets to your page he can search through your content you have for sale
       Upload content as, free, trailer or for sale (If you want to create a sale item you have to create a trailer first)

5) Cryptopayment
    You implement your btc-pay server
    create an client with the api
    run the api -loopListen for automated payment processing 

Get started (from Web-GUI)

    #Install the app and downloading rquirements from requirements.txt
    python setup.py
    Follow instructions and create a user (the default admin user)

    #Run the server
    python njoyporn.py

    #Visit your new tube
    http://localhost:7676

Login to access the Web-GUI:
    http://localhost:7676/login
    http://localhost:7676/webgui

    Here can you upload videos to the server
    Manage the videos*
    Manage users*

Get started [Terminal / basic]

    #Install the app and downloading rquirements from requirements.txt
    python setup.py

    #Run the server
    python njoyporn.py

    #Visit your new tube
    http://localhost:7676

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
        enter nickname
        enter role

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

Advanced terminal functions:

#USERDATABASE
you can create a user or admin with -newUser
you can print info about the user and the data uploaded -printUsers, -printVideos

#DATABASE
you can update the whole content in /static/storage/specials with -addall
this will skipp data in the database and add new stuff
you can edit video data in detail
you can edit comments
you can print a details data list

#ANALYTICS
you can print data like poplular categories or actors
you can easy modify the print function to access all data

*You can easy build the frontend for those functions. I run them from the terminal so feel free to help me to update this app