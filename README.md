# SpaceY

![SpaceY](https://cdn.discordapp.com/attachments/815007241576513549/815278835666255932/spacey.png)

A consolidation of NASA APIs into short, factual, and visually-attractive stories!

## Introduction

Welcome to SpaceY, a collection of 3 short stories all taken from 3 different perspectives, each with links to API calls that provide relevant data. Our stories include: The Perseverance Drone Landing on Mars, a Martian Astronaut, and Satellites addressing the natural disaster situation on Earth. Every story has 2-3 relevant APIs that provide statistical info from NASA, a trusted source, about specific events 

## Inspiration
For our first story, we were inspired by the recent Perseverance Drone Landing on Mars on February 18, 2021. After that, we brainstormed ideas for how to integrate more space events, and decided that we could display a collection of 3 short stories. Then, in order to increase the visually appealing portion of our website, and make it more of a challenge, we decided to use NASA APIs that would perform functions needed to fit into our stories.

## What it does
The website has 5 pages. First, there is a home page with links to the stories. Three other pages are the story pages. And finally, the last page is an API call page, which displays results from an API. On the story pages, there are links situated throughout each story, depending on the situation in the story. These links take the user to the API page mentioned before. For example, if this was an excerpt from one of our stories: "As I landed on the smooth reddish ground of Mars, I knew people depended on me... Perseverance. I decided to take some samples of the climate of the red planet." There would be a link right next to this line that would take the user to the insight API, which records weather on Mars. 


## How we built it
All four of our team members contributed in many different ways to make this possible as a team effort.

### Krishnan Shankar
I mainly created functions that request data from the NASA APIs and parse them into some displayable text and some images. I also coded the backend of the website using Flask to render the templates. I made the backend so that it uses a single template to render all the APIs, which helped with management a lot. I also helped a bit with the design of the website, including organization and HTML pages. Finally, I took care of deploying the website to Heroku, to ensure it stays up 24/7.

### Shivam Suri
I created some of the functions that request data from the NASA APIs and parse them some displayable text and images. I also wrote all 3 of the stories, and planned where each API link would be on the story. Additionally, I helped on designing our logo by brainstorming ideas, and implementing the created stories into the story pages, along with rendering the APIs on the API page with Krishnan Shankar.

### Noel Jackson
I worked as a frontend developer in this project, in charge of making it aesthetically pleasing. My job was to work on animations and perfecting the user interface. Additionally, I aided in the making of the cards and linking them to the API.

### Alex Kasprzak
I also worked as a frontend developer, working with Noel to give the website a more professional look and colorscheme. With prior writing experience I also helped to edit the existing stories. My job was to work on perfecting the user experience, showcasing it through recording a demo of our website.


## Challenges we ran into and accomplishments that we're proud of
A major challenge we ran into was using one template and one route for all the API pages. This was difficult, as we needed to specify which API we were going to use, and we needed to customize that page in order to render data from different types of APIs. We were about to give up on this strategy, when we finally figured out how to pass parameters in urls. We're glad we kept on going, as without it we would need to make 6 more templates and routes, which would become chaotic.

Another huge challenge was getting some of the APIs to work. A lot of the NASA APIs we wanted to use were lookup APIs, which meant they worked best when given certain parameters, like the coordinates and date. Although we could successfully use random numbers to accomplish this, some of the APIs didn't work with our random numbers, and we had to make adjustments or completely remove the APIs from the stories. 

Additionally, at the start, none of us had experience with NASA APIs, and even APIs in general. It took us a while to figure out how to even use the APIs. And once we figured that out, we realized that every API call will return data that is super inconsistent. If we try to access a certain field from an API, it would work on the first day, but on the second day the returned JSON would just have no value for the data we needed to access. This was a huge struggle for us, as we needed to throughly read the docs in order to figure out which fields will be present consistently. 

A final issue with the APIs was that they would store the data in a bunch of nested dictionaries, which meant that we had to use trial-and-error in order to figure out where the data that we needed was. And often times, to access the data, we would need a bunch of dictionary get methods, which would often extend past the PEP 8 line limits. This trial-and-error process took about 30 minutes per API, which made it difficult since we were working with a ton of APIs and were a bit short on time.

Finally, a major challenge we had was our teammates. In the process of finding a team for the hackathon, we came across 4 people who wanted to join the team, but who later left or decided to not contribute to the project. This uncertainty took away a lot of time for working on the project, and at the end, we finally found a team who would stick to the project and work hard.

## What we learned
All of us became a lot more experienced with handling API data and styling websites. We found out how to debug API errors, and how we can use this JSON data to convert it into text and image links. We also learned more about how to make a website look professional and appeal more to the audience, using advanced CSS and HTML, along with javascript for alerting users or tracking errors. This project was a fabulous experience to showcase our knowledge of Coding and Science, and we all look forward to doing more projects like this one!

## What's next for SpaceY
In the future, we plan to add even more stories, explore more APIs, and learn how to use some of the APIs that we didn't know how to fetch data from during our hackathon. (Earth API, SSD/CNEOS API) We are also thinking about expanding our project with other APIs not from NASA, including Google Earth API. We will continue to work on our logo and style our website more, making it look very professional and more user-friendly. There are a lot of advancements that our open to code for our project, and we will continue to improve our project in the future. 

