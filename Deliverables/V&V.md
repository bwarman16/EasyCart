# Verification & Validation

<p>Group 03 - “[Easy Cart]”<br>
Date and location: July 29, 2021
Group Members: Justin Ceccarelli, Jason Gaglione, Jack Decker, Michael Nelson, Linh Nguyen, Brandon Warman, Jabril Gray</p>

## 1. Description 
Our application is a grocery list generator for a given recipe you can get at Target. You look up the recipe you desire and through our application it returns possible recipes you may like and then gives you the grocery list with the price per ingredient. We did this through building a good front end application that makes it incredibly easy to search up the recipes then through the backend we have the logic that helps return the grocery list and price through the spoonacular API and the target API. We then used a flask framework to be able to connect our front end logic with our backend logic. The front end is completely built with javascript, html, and css for styling. Our backend is completely built by python and certain API’s. The reason we chose to use the Flask framework is because it’s a really powerful python framework that makes it super easy to be able to connect to our html and javascript files.

## 2. Verification (tests)
### 2.1 Unit test
The framework I chose to use was unittest which allowed for preset functions for testing the results of our API calls.

2.1.1 https://github.com/bwarman16/EasyCart/blob/main/UnitTest.py

2.1.2 https://github.com/bwarman16/EasyCart/blob/main/UnitTest.py

2.1.3 https://github.com/bwarman16/EasyCart/blob/main/TargetAPI.py

2.1.4 

![V V_214](https://user-images.githubusercontent.com/87092092/127618718-1fc94ff5-f904-441a-adef-20486467bb64.png)

### 2.2 Integration test
2.2.1 We conduct our integration testing using the PyTest framework which supports testing Python very well and easy to set up the environment for testing files. 

![V V_221](https://user-images.githubusercontent.com/87092092/127618777-b66ae940-7383-420e-8247-ac4335c59861.png)

2.2.2 Link GitHub:
https://github.com/bwarman16/EasyCart/tree/main/Integration_Test
https://github.com/bwarman16/EasyCart/blob/main/Integration_Test/integration_test.py

2.2.3	There are 5 cases for testing in the Integration Test code file. One of examples is the connection between 2 API modules, especially the price of a Spoonacular ingredient from the Target API.

2.2.4.

![V V_224](https://user-images.githubusercontent.com/87092092/127618880-4f849126-cf72-47e3-a81a-9a57fd3c5f3c.png)

## 3. Validation (user evaluation)
### Script:
- What are your initial thoughts of the web page?
- How does it feel compared to similar web pages?
- What do you like about the web page?
- What do you dislike/feel needs improvement?
- Do you think you will use it in the near future?
- If not, what might change your mind?
- Overall, how would you rate the application? (1-10)
- Why did you give it a (insert rating here) out of 10?
- Is there anything else you would like to discuss about the web page?

### Specific follow-ups:
- Do you think the web page is simple/user friendly?
- Do you feel you are given enough options when choosing a recipe?
- Is there enough information on the recipe you're looking for?
- What other features would make this web application more usable?

### Interview Results:
Interviewee - Kevin Lindbloom

- What are your initial thoughts of the web page?  
  Looks simple and effective.  
  
- How does it feel compared to similar web pages?  
  Different from most recipe websites, but contains what is needed.  
- What do you like about the web page?  
  Easy to use, the font is nice, nothing pops up in my face and I can find many recipes.  
- What do you dislike/feel needs improvement?  
  Could work more on the design, pictures of recipes look stretched when searching for them and the list of ingredients is kind of weird.  
- Do you think you will use it in the near future?  
  Definitely, especially since I’m starting to cook more often and I’m running out of ideas.  
- If not, what might change your mind?  
  N/A. 
- Overall, how would you rate the application? (1-10)  
  7.  
- Why did you give it a (insert rating here) out of 10?  
  The design and look is not the best I’ve seen, but it works as intended and finds any recipe I’m looking for. Looks is a personal preference anyways, as long as I can use it.  
- Is there anything else you would like to discuss about the web page?  
  If there was a way I could make an account and save some of my favorite recipes, that would be nice. I think this could be very useful for some people.  
- Do you think the web page is simple/user friendly?  
  Yes.  
- Do you feel you are given enough options when choosing a recipe?  
  Yes, more than I’ll probably need.  
- Is there enough information on the recipe you're looking for?  
  For the most part, if the pricing and ingredient list were clearer, then definitely.  
- What other features would make this web application more usable?  
  System that saves favorite/recently searched recipes to an account.  

Interviewee - Corbin Strycker

- What are your initial thoughts of the web page?  
  Simple design and easy to locate all of the features.  
  
- How does it feel compared to similar web pages?  
  Feels normal to me, but minimalistic and not cluttered with text.  
- What do you like about the web page?  
  The simplicity makes it look somewhat professional and it's very easy to find what I need, along with the price of ingredients.  
- What do you dislike/feel needs improvement?  
  The color scheme feels off to me, and I’m not sure what some of the text in the ingredient list means.  
- Do you think you will use it in the near future?  
  Probably not since I don’t cook often, but I’m sure my girlfriend would use something like this.  
- If not, what might change your mind?  
  If I ever start cooking and meal prepping again, I’ll consider finding some recipes here.  
- Overall, how would you rate the application? (1-10)  
  8.  
- Why did you give it a (insert rating here) out of 10?  
  I like websites with functionality, and the general idea of this one does catch my interest. The only thing that I think could be better is the design and color scheme.  
- Is there anything else you would like to discuss about the web page?  
  I think this website feels different from most, but in a good way. There’s a lot of things that could be added, but the functionality is there.  

Interviewee - Delanie Williams 

- What are your initial thoughts of the web page?  
  Simple and needs more colors that represented food.  
  
- How does it feel compared to similar web pages?  
  It is normal and very simple compare to others.  
- What do you like about the web page?  
  The simplicity makes it fast and it's very easy to find what I need, along with the price of ingredients.  
- What do you dislike/feel needs improvement?  
  The color scheme could be revise for bright and attractive views.  
- Do you think you will use it in the near future?  
  Probably I like to try new recipes and this would be a great tool to find them.  
- Overall, how would you rate the application? (1-10)  
  7.  
- Why did you give it a (insert rating here) out of 10?  
  I like websites, and the general idea of this one does catch my interest. The color scheme would have to look better and I would like more features.  
- Is there anything else you would like to discuss about the web page?  
  It is a great website, it provides a lot of information and could be a future success as long as it keep improving.  
