This code will have an attempt to display the following a list a movies, seats in the movie, booking history, and the ability to book a seat
For movies it follows the CRUD actions which means you can create read update and delete which will lead to the seating for said movie
For the seating I attempted to organize the rows and columns however html and django did not like that so its a long line for the movie but very intuative with the seating number
Before you can take a seat it is very important for you to log on as a user in the navbar 
for a premade user just use (admin) and its password is (1)
of course there is also an option to create a user with any name or password if you wish to test the booking system
After you have logged in you can now book your seat, which you can click on a spot in the movie theater, which allows one to have an option to confirm the taking of the seat
if you do take that seat, you can no longer click the button to take that seat and is grayed out showing that it is taken
If still logged in
If you would like you can also see a booking history indivuddal to the user allowing to see what they booked, what time itll happen, and when they booked it

you can use the api to change the information as well
for example adding a movie is
/api/movies will allow to see the whole list of movies and can add a movie this way
/api/movies/1 will edit the first movie allowing to update or delete

this works with other things like seats and bookings in similar ways

In order to launch the web application, after launching devedu

1. source CS4300/bin/activate
2. cd ./CS4300
3. cd ./Homework2 
4. cd ./movie_theater_booking
5. python manage.py runserver 0.0.0.0:3000

I just would like to inform that I did use some assitance like for example I used old code to create forms and views and urls from projects I have done in the past
I also had used A.I (chatgpt) for small things that did not affect quality of the code for example the button that changes color and disables it, I also used for the api in views and url mainly for the import function, I followed along the reading to ensure
understanding of what to do and how to do it. 
The main use I had for A.I however was the debugging process for various mistakes I made along the way. I had fun with implementing views, and had done the reading with the RESTful of course I didn't fully understand it but majority of my code is my work 
that either I have done now, or in the past, I would definetly say that 92% of my code is something I achieved by my own thoughts and experiences, the hardest one was getting the seats displayed that were already taken

