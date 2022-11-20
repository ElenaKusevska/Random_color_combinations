# Random_color_combinations
What makes people like a color combination? (In Progress...)

This is a fun project that I've been working on for a while now.
I come to back to it every now and then when I have some free time, which
unfortunately is not very often.

The backend is a flask application that uses templating and jinja.
It uses postgresql with SQLAlchemy and the development environment
is set up with docker-compose.

When the the main page ('127.0.0.1:5000') is loaded, a combination
of two colors is randomly selected and displayed. The user
rates this combination of colors, and the rating is stored
in the database. The idea is that after a large number
of people have given their ratings, a large enough database
of color combinations, their respective ratings, and perhaps
some information about the rater (location, etc.) will be compiled.
Once enough data is available, we can correlate the characteristics of
the relationships between the rgb values of the two colors with the
rating of the color combinations, to discover what makes people find
a color combination pleasing to look at.

For this I will have to set up a service to consume the data from the
database and process it, and display results.

