# Mercury Snap 
mercury snap is a screenshot taking service for webpages. It's built primarily to serve in its parent project [Analogue Mercury](https://github.com/analogue-app/mercury) as a fast screenshot taking endpoint. 

### Endpoint
Live endpoint is running at: https://github.com/analogue-app/mercury

Pass in the parameter `url` parameter with a valid URL to get hosted link of screenshot.png.
```
GET https://mercury-snap.herokuapp.com/snap?url=https://www.google.com/
```

## Project Scope
After exploring every single python package and APIs, I didn't find a viable solution for a simple task of taking screenshots of webpages in an optimized way. I found that most python packages out there are either not working/outdated or are very slow for any webservice to use. Most APIs on the other hand are paid and none of them offers a free plan with more than 100 screenshots/month which is not suitable for any webservice. 

So, I decided to create a simple opensource python API service that can be used by our main project 'Analogue' and by anyone who has a similar need. I welcome everyone to use this service or contribute to this. 

Right now, API has a simple endpoint that's giving us a url of a screenshot. Screenshots are of only of that area that's visible on browser's screen. Current setup is using [Flask](https://flask.palletsprojects.com/) to create an API and [Selenium](https://selenium-python.readthedocs.io/) for taking screenshots. I'm also using [imgbb](https://imgbb.com/) service for hosting screenshots. Big shout out to them! 
 
