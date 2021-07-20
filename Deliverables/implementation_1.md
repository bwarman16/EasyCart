# Implementation 1

_Group 03 - “[Easy Cart]”\
Date and location: July 19, 2021\
Group Members: Justin Ceccarelli, Jason Gaglione, Jack Decker, Michael Nelson, Linh Nguyen, Brandon Warman, Jabril Gray_

## 1. Introduction

Provide a short paragraph that describes your system. This paragraph should contain the value proposition and the description of the main features of the software. At the end of the introduction, include links to your project on GitHub and Trello, which should be up-to-date. Grading (2 points): This section will be evaluated in terms of correctness, completeness, thoroughness, consistency, coherence, and adequate use of language. The description should be consistent with the current state of the project. You should include the links to GitHub and Trello, which should be up-to-date. 

EasyCart is a free, web application made to help people create nice meals without the hassle of trying to find a specific recipe and what ingredients they need to pick up. EasyCart works by using Spoonacular’s API to search through Target’s API to find the ingredients needed for a chosen recipe. First the user searches for a recipe on EasyCart’s website, they choose a recipe that is appealing to them, then they can add the ingredients to their cart. This streamlines the experience of recipe making into a few simple steps, in order to facilitate ease in creating the recipe one loves.

Github: ​​[https://github.com/bwarman16/EasyCart](​​https://github.com/bwarman16/EasyCart)

Trello: [https://trello.com/b/2TDMYnVs/project-board](https://trello.com/b/2TDMYnVs/project-board)

## 2. Implemented requirements

**Requirements:** As a user I want to be able to choose what kind of recipe I want and to get many different options back.\
**Issue:** [https://github.com/bwarman16/EasyCart/issues/15](https://github.com/bwarman16/EasyCart/issues/15)\
**Pull Request:** [https://github.com/bwarman16/EasyCart/pull/11](https://github.com/bwarman16/EasyCart/pull/11)\
**Implemented By:** Brandon Warman\
**Approved By:** Jack Decker\
**Print Screen:** Print screen not applicable

**Requirements:** As a developer we need to make it so that our API’s are working fine and having no problems.\
**Issue:** [https://github.com/bwarman16/EasyCart/issues/18](https://github.com/bwarman16/EasyCart/issues/18)\
**Pull Request:** [https://github.com/bwarman16/EasyCart/pull/11](https://github.com/bwarman16/EasyCart/pull/11)\
**Implemented By:** Jabril Gray\
**Approved By:** Jack Decker\
**Print Screen:** Print Screen not applicable

**Requirements:** As a developer we need to hook up the server that way we can send the information from the front end to the back end.\
**Issue:** [https://github.com/bwarman16/EasyCart/issues/17](https://github.com/bwarman16/EasyCart/issues/17)\
**Pull Request:** [https://github.com/bwarman16/EasyCart/pull/11](https://github.com/bwarman16/EasyCart/pull/11)\
**Implemented By:** Jack Decker\
**Approved By:** Jack Decker\
**Print Screen:** Print screen not applicable

**Requirements:** As a user I want to be able to see pictures of all the available recipes and have them formatted in a clean and professional way.\
**Issue:** [https://github.com/bwarman16/EasyCart/issues/14](https://github.com/bwarman16/EasyCart/issues/14)\
**Pull Request:** [https://github.com/bwarman16/EasyCart/pull/19](https://github.com/bwarman16/EasyCart/pull/19)\
**Implemented By:** Jason Gaglione\
**Approved By:** Jack Decker\
**Print Screen:** A print screen that shows the picture of the returned recipes and shows them well spaced out

**Requirements:** As an average computer user I want a website that looks good so it draws me into using it.\
**Issue:** [https://github.com/bwarman16/EasyCart/issues/12](https://github.com/bwarman16/EasyCart/issues/12)\
**Pull Request:** [https://github.com/bwarman16/EasyCart/pull/19](https://github.com/bwarman16/EasyCart/pull/19)\
**Implemented By:** Justin Ceccarelli\
**Approved By:** Jack Decker\
**Print Screen:** A print screen that shows the new background colors as well as font and font color

**Requirements:** As a busy college student I want a place where I can look up recipes easily.\
**Issue:** [https://github.com/bwarman16/EasyCart/issues/13](https://github.com/bwarman16/EasyCart/issues/13)\
**Pull Request:** [https://github.com/bwarman16/EasyCart/pull/19](https://github.com/bwarman16/EasyCart/pull/19)\
**Implemented By:** Linh Nguyen\
**Approved By:** Jack Decker\
**Print Screen:** Screen with search box that allows you to search for a recipe

**Requirements:** As a developer we need to be able to use the spoonacular api and take the recipes and put it into the target API so that it can show its availability.\
**Issue:** [https://github.com/bwarman16/EasyCart/issues/16](https://github.com/bwarman16/EasyCart/issues/16)\
**Pull Request:** [https://github.com/bwarman16/EasyCart/pull/11](https://github.com/bwarman16/EasyCart/pull/11)\
**Implemented By:** Michael Nelson\
**Approved By:** Jack Decker\
**Print Screen:** Print screen not applicable

## 3. Adopted technologies

**React:**

React is a framework for front-end website development, which includes many functions or features helping us to code faster and conveniently. Using React framework makes our website work without html files and we can focus on the CSS and JS parts. Moreover, this framework supports us with useful functions and connects with the back-end part.

**HTML, CSS and JavaScript:**

These languages are extremely essential in the front-end development, which helps the website look more professional and attractive with users. For the most simple feature which is showing the recipes, we use JavaScript to fetch the Spoonacular API to get the information faster.

**API:**

API is the powerful tool which helps the project to reach much more information related to the recipes, images, names and items in shopping. There are 3 APIs used in this project: Spoonacular API providing the recipes, images, names and ingredients; Target API providing the right to get the information of items related to the name and price in the supermarket Target; and Walmart API which also supports the information of shopping items related to the name, price and portion size.

**Python Requests Module:**

In this project, most of the teammates choose to use Python as the main programming language, especially the module named Requests in Python. Due to that module, we can easily reach to APIs and get the information related to the shopping items in Target and recipes, ingredients in Spoonacular website. Also, the project uses this language for the back-end development.

**Summary:**

In this implementation, we try to get familiar with these new technologies such as React, API and Back-end stuff. Thanks to React, we can easily develop the front-end part with JavaScript and CSS and the result is the fact that the landing page of a website application looks professional. Besides, the APIs play an important part which provides much more information about the food and supermarket items. As a result, getting used to these technologies makes us understand more about website application building and develop a higher-quality product.

## 4. Learning/training

Firstly, our team divided the members in each part: front-end and back-end developers. Then in each part, team members will be responsible for different new technologies and research on the Internet independently. In the process of researching, if a member has trouble understanding a concept or how to apply it, then other team members will try their best to help him by researching together.

Learning and applying the React is really challenging because it is a new technology but extremely useful. So for this technology, our team encourages all team members to research and apply it into the project. Because every team member has prior knowledge of website applications so we are able to cover this concept. Usually, because of online classes, we contact each other by Discord and have meetings online too.

## 5. Deployment (Brandon)

Describe how you are deploying your system in production. If you are using AWS, remember that AWS Educate offers free credits for students. See the tutorial at https://docker-curriculum.com/ on how to create a container and deploy it on AWS. Provide a link for the system in production. Grading (4 points): This section will be graded based on the adequate use of the technology and its adequate description.

## 6. Licensing

The license we have adopted is the Mozilla Public License Version 2.0. The license allows others to modify and add code on to source code. While still allowing them to combine our code with code under other licenses (open or proprietary) with minimal restrictions. Sharing source code with others can provide new, faster ,and updated ways to implement features.   

## 7. Readme File

**README.md:** [https://github.com/bwarman16/EasyCart/blob/main/README.md](https://github.com/bwarman16/EasyCart/blob/main/README.md)

**CONTRIBUTING.md:** [https://github.com/bwarman16/EasyCart/blob/main/CONTRIBUTING.md](https://github.com/bwarman16/EasyCart/blob/main/CONTRIBUTING.md)

**LICENSE:** [https://github.com/bwarman16/EasyCart/blob/main/LICENSE](https://github.com/bwarman16/EasyCart/blob/main/LICENSE)

**CODE_OF_CONDUCT.md:** [https://github.com/bwarman16/EasyCart/blob/main/CODE_OF_CONDUCT.md](https://github.com/bwarman16/EasyCart/blob/main/CODE_OF_CONDUCT.md)

## 8. Look & feel

When it came to designing the website for EasyCart, we decided to follow our interviewees suggestions and keep it simple. We have gone with a straightforward approach with a simple instruction, “Search your recipe”. The minimalistic design will ensure the user can get started quickly with no wasted time.\
**![](https://lh3.googleusercontent.com/8X2EM8OvSxb_1vqHLVhJVKimTqshzaFnAnDwBUo7FJYcj0Pp7EyXvbFBHuLRpnglQYv8ITqwuAAtooWJcWJpSw3fTdjeoN3bUd78_9MCoTT_EhJHLQAxXpbudUwgOPMqaWITSRJfl5WB537HrW3E7_oCMuBXlw_ehFPbkuAWeyWbqmVAmrW-J1pJ3b1BUOnjs70Jfp39K8yIeJ8tebpZB8YLD1PdegZ2FGvy6tUMXy7VJlxSshLGTlf97oP8kHAL2zwgyXe3SSgUbLKJF31Dt-J5MLyR5xJM2IDrZuhxMNHY99VLziXfehiYbb5HOHvVaWfRH-HuN30XBr26uVnalCrD9r71qJ0JCVPmWpJKOxpx4_XTjnSqdxTf-0pVWuczXvA-0HVHwiV2oqiAR2SEYnKFELo2lNcb97jVRRAj8oCRVl8khAjqlig6OybfWsO2u7p1FATQneEtSxhygf2yCUVgo0ZS0ou38wu8gelYt8b7ZcoaMOz3yyA2YpszT6gnQzPLS0xpuwwQMt2Rq-w-LWccSfte5OiagNgzbLw2c7tYrg_5GN65-FE9d3vp14y3ziLmdtkBpYwUsHd80xutOmsZshFAP0XCMjYmtVZ7UXVY8lPB7qwsWVNrtoqO4pcGTQ_KE-6_esQgT7tWSVeknJRG4akKH1LoOFBFgoVGEO1SrYT2yOSRXHcNyrB79Mc-ThKkOL9T8bcSk_BkWKdX-g=w1709-h902-no?authuser=0)**

When the user enters a recipe they want to find, they will be presented with cards with a photo and the recipe name. This, again, keeps things simple for the user so that they can search quickly for their desired recipe. The page is easy to look at and does not overwhelm the user with each recipe card organized and spaced equally, making it easy to distinguish different recipes.
**![](https://lh3.googleusercontent.com/s6kNWlq55TCfl0wFTGp7qsANhzrqmurZR73z49FYp5eM0fa_c_7vGzT4VfvXtxk01mA2I41LT22nP63C-RFwSD_mKWSwyFEYzwR-n6BRE57yaZbelW2Q11wNMv7VKD14MRSs02EOF9ChSXuCII3ZgMJQUFKPUH6PIYKWDS5Sscg0rGnMmkvHyceofDge0mbqFTPkDSHyWc_pY7R87xBqQFuUfzXvefO20pvQOUzOLQxx3ybMQ_C211NMYWaQUAYxKbE7mM56P3-VxdsLPmyl3nLqyJy2WmBuRSu4fBIYcsQYYBb9Ixjp3C6id3dWUQAiHt_mMci1lpkqoXbhEl76coLUnl0c9RLld_2lSQjahvsbwH156AXq4ugZfUmUYbVSGjGneNSte_rLKgj9OmLTDWJS3PR3Rds8TUCFTPeF47m_Jy9vSvI31m4OxUgGn5KcHlz-fG6f7mxfny-mGhM8Ad2HiNp9phShXei2QGJJ_4PYZuiuqdYGEfP1xyG6oWft29NzejGlV_JNPC9sO109rbITbxUwa0cAtzvHyEF2cFMygJSSiILpUbD-Uab1lRrcqAUTZfyd7Z9sTSM0vw0kDF4Muqx7TUDai7N-VCH7WziE_eDoMQtSD8OSBR1B37t6qL6UTx-orW21Ubj0O-zYz9u8EHTcVy0ZHkEZ2Vo9CK8wmdukyjF_mLMUN4iAd-DwsLm5Q9z9FhKWuSxMT1ouAQ=w1699-h903-no?authuser=0)**

## 9. Lessons learned

In retrospective, describe what your team learned during this first release and what you are planning to change for the second release. Grading (2 points): Adequate reflection about problems and solutions, clear description with adequate use of language.

For our first release, we learned that implementing the Spoonacular API with Target’s API was more challenging than anticipated. More testing needs to be done before using Target’s API to link it with the front end of the website and create a physical shopping list of ingredients. On the other hand, we were able to access recipes from multiple different sites so users can choose between many recipes of the same cuisine. Along the way, we became more familiar with github, updating changes to our current API files, and python itself. 

## 10. Demo

Include a link to a video showing the system working.
[https://youtu.be/yMf1BfuitSw](https://youtu.be/yMf1BfuitSw)
