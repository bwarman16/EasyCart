# Design

_Group 03 - “[Easy Cart]”\
Date and location: July 23, 2021\
Group Members: Justin Ceccarelli, Jason Gaglione, Jack Decker, Michael Nelson, Linh Nguyen, Brandon Warman, Jabril Gray_

## 1. Description:

For our application we decided to use a few different design patterns for the specific issues we had to solve. First for our search bar filter we decided to go with an Observer pattern. This was because of the interface we needed to be able to update and show the different data sets as requested while also focusing on runtime optimacy. The next big design pattern we focused on was a strategy design pattern. This seemed important because when the user searches for a recipe it should be shown in the best way possible. We wanted to make sure that it looked professional while also being user friendly so all types of people were able to use our application. The final big design pattern we used was the bridge pattern. We chose the bridge pattern because it would help us direct the extension of  the grocery store API. This was useful with the checkout function because it helped keep track of how the customers receive their products. With these design patterns in mind we also made sure we followed some of the SOLID principles. We made sure to keep everything simple, easily maintainable, and easily readable that way everyone was able to understand our code. We designed Easy Cart with functionality in mind while also making sure the interface was easy enough for the average user to use.

## 2. Architecture:

**![](https://lh3.googleusercontent.com/0vO12yxZXKdUVe7tJHDmaYlDLha02SJ9jQ4kamHRIkHQ2S3ihKs8OcxiJag7oFEmRQD_Ar7-glvmV5sxHKQa5731q5AcQm920mqDzVNFYwvfyYfVwLz6hFHwj-FALmaKYI5xsam3hY1Cxf0Z9P65LvabBbK-LFngiHJsehXuqqIr3UZc3tDJGGHkOC1WSh_--5vhP5-p-jgEYx0P8CorPJ272EYNQh0Nu9XQDsYsKf5cI5vzV4So8_f-1FRqQj_fET_tjunGvRHB4DLOgmHhRNMv0merWgelhtmu7qA63alUPzGAmB67olV1yyQ-Ogwq7-BeOVb4zpz4E341jSokShd9BaTJedKcA9c_Nlz2IO6dAMTAMrFvATorA9orePQWGTdObRtK6Z1iJv76AoR3z1aWw-h2gGnPLNZPLd-x3lHtQMZp56gOEbrprgJEqvI2jyzHZZd6VmRCs4ae8TEafYOsAECm6uZPcL9GfzpZRwJ-ByXqO3NmvRuVY9mjV9hD3H5vzplpI46aiIsAmcTZ9DVRpoOhYplTD3fBLFQHlxllpwdt_d5BkGCY9-_YeRoFhxSi_T8j70XIjrSKZJwuzFhIRIEglIRvWX5dgbUzFBWpVHWOCi9mdD6Jzwx9HxNrcTe4YlOQAuvXiAjLaT1OPylDTNijMoJdvImPhPwsG_vGAsHKtIuXq6qy1g3huNdAFGKTZM98foHbr2XDyECsxQ=w467-h328-no?authuser=0)**

My explanation of this diagram is that a group of users are able to access our site from the landing page (the index page), the search bar, the search results page, and their shopping cart. In order to receive the information found on the results page, we use the recipe information on the data layer. In order to add ingredients from the results page to their shopping cart, we use Spoonacular to access Target’s API, which includes ingredient nutritional information, and then the user can add all of the ingredients into their shopping cart. The data layer is on a separate layer due to its lack of direct access to the user.

## 3. Class diagram:

**![](https://lh3.googleusercontent.com/WgzZBMcyYDpBh2lHE8YyUr0y67wTlnIOVh9m4Oi_O-r0rzF7F5VCxReG1KwGEBGSNYDcX_8FeHQ2wuxNLrRWzX8RMgeeslp9nlAkZpa3DLLwCXjb25u0DAfJyhgvNBRCndPsuOcNPrH60oS6pgyljN9sLUAetTnccdBRB2ULch06dPv2XjimKsbFv7O-tXf6JKVrLHPsMWPITFVbGb5m3qKugHV3s84suE0G7wsDUX3Alat_udgxtlzz3kv0HkFO8Sio0NZsfitiJ7l83at3cxVIU5JumOVjsdIXpdrW5taQikG5LPETee43yWGwbDUYl3Ij3arLIqh0WrtSEFPzWcxYja2q0IZCjRcSklrSE0VFpWp9jYPhNaxapH60xe4I7cBuNm9mJno1f8pqyEfZhJLJSr71dwBsnE-VaB8MUh8-IkxHHm5JzfJOvf40mRy3yme7hJx7iue5nhHjNKcw8nlFdl7JoW2qW0u-1-cDC6W8HwpMSH04cAu9oMIiZJjJ8B7kKVG2UJcUY5oIUdvwxxUxQNrz2MlSNsv7X7-8Y9i0vyZ8mGqDCoxP2RUnjz84skjaHMOv5D8YPXlRnllibnpn93M92Pq-hzjWvDd7TVRLOLbSg0QKVz6Gt5gDBjPAu_cEegPO9XMUcQsq2-a8Vt1G-0xUx_nt7rMWhFX0F60aWLR5PJtfkFzg3uwUqUiIabCrtCOWlX8nPVijr7UEiQ=w615-h409-no?authuser=0)**

## 4. Sequence diagram:

**![](https://lh3.googleusercontent.com/5NtESYCHwTmMrKPAj-1IVBo-YqmWamlGVcfnsrGejTSsxlIp9uj2xGadGvvmrsqK9B-gT3IIUo5PyWipWl2fGNRrFthaMJ2FxWrJpiJZo38V3ACpK9AS16KyNIhTnc68ii56wqb9jqWozcztEj_frmSB3aazz6036x2WGMm09PXAJlF9_iZCWA-iRYrPol0k5ib9oJ6uZ8lWiunWiG8OMGFgk1MIUp3iX0AphZPP4Np-BuU6WOLOFHl2tXXNJwD_MB1jHr9CiZC5KVajkXc1NbQJHzrTvW20tsJlT1CH5c66_o45MfeorQPGegsklKJkQWR0W6f_Vf7HGmU7zR_zkv1m-j4dT_r7gTJqwqpK_VRHTntVjQnWpZiEHhcUreih3dVoELE3DdJtXsbAxJx4beYp9uWiPgzXuXCdV2F6l6fKgFITL8QyCMQYZARFP5sFatRef8kGrhOzWdkG3qL_ddN0OCI9mqtmyZi5Hkp7aEGoGFKCncwpI6ZzvJOpopyQNn-3DBpMW_fTUwnW2FZ0MSgozD1DrRGKKbQIxkGAkcbejCTle0T4lpbZwZH91pW7StXkbp-1XHD-WJVXSJOExTn8TqoGFOMrkjNAb8AHs-QJm7fHlJNx9SUaRfFMvZTt3I-FMAiNL8fXM5nCAyySMzFJeAmWBcpFLk1iI72ZG3wKXR4kY4RmnRvga78gylgCsQaAC3yB_P8azztZB_e9mg=w631-h771-no?authuser=0)**

**Use Case:** Search for a recipe\
**Actor:** User\
**Description:** The user can search for a recipe to see ingredients\
**Pre-conditions:** The user has internet access.\
**Post-conditions:** The recipe is shown.\
**Main flow:** 

1.  The user enters a recipe to search
2.  The system displays recipes that match the search
3.  The user selects a recipe from the displayed options
4.  The full recipe is displayed for the user

**Alternative Flows:**

*a. System can not find the requested recipe
1. System will tell the user the recipe could not be found.

## 5. Design Patterns:
**Strategy Pattern (Behavior):** Our team uses the Strategy Pattern to decide the display selections on the user's screen.\
**![](https://lh3.googleusercontent.com/eeWHqYNGC53svLp2Yq08LrxnEn9Fnv2Djl_jhP7n4AZdzGf0Lr7_15qif1kD4D8ye2rILbgMxSv0HwUSJxSW6s6k9TpTSexQ5cqDY72IM5-DU_icPGnYkEVAlU83G10yKBwxo5Yi2k-qGywECKcLb1HReeA1L41LHUrRTJZKfQMNwuOYAXkdOtG3AY1JFgxrrdUi4tulWpkchHAia7l6nFXp_N-7BLGhqJ0qovsGRlLyxN0jGztRIdHUswcJUze4G6ptUUcMn8BpwdRg2S3W2QkZMW110ebm5XE6eaOkZ-wkQurGVz8cHc8Zzm9Wfb2yvlnkshR3pFwDeFLbB8CnD4l4aUv9nqshaik3WATE6W2yi2TYRtC1C9-JNT589wA8i09tBxrR_dDJT68Fy0fGg6ZV68cO4-uC6ahW9w2D5W7YvEq7zvvDGOykVKWbAfRKWhDvG-vGJhRK1GxYDJfA_UzOC-4lPMd53SiewNnnRGKVP-AMALuQEnIdl4a-v-n1Yk9kZp32loTzXqbcBltxSwgzwRyFiwjfVtV6DGWt5BOIvvW1TA_SU6-x50X2XR9O2ON9qjvn3bJpedy2CiVER2_ctCPCE-SnJXPvr0aR94s9quw90jIjRnqRStvQXDGX1dDh7sIyck8ZCV08zllkTdZJxCeVXWDZpMhR4pp5x2NyQJBEAOrAFPgL79iTIs2TBTSYgjCpsl1YmwH-2FH4aQ=w1648-h969-no?authuser=0)**

**Bridge Pattern (Behavior):** The Bridge Pattern is the appropriate design pattern for checkout selections, because with this strategy, we are able to manage the extension of supermarkets and the way that customers receive their products. 
**![](https://lh3.googleusercontent.com/2RyFx7PZucmyEQhsFhZx4ZuIWftYVjzDYRdWi2q1LYkU7YSwea4KDJz6NeWIPF_EuLj0-wSGcLQs8rfe6jq_VSpXzFADvTVES0a-JQbRZCD3iXO_N8hoDAzvMULVl8f32-ykWQrKtR3uPCEfFLBzbJhh2epuSsmCz7Vpcym8EboFrC0OG3bHkIDPZlWY6xOgJUujVrX2mH7Z7nZslcPmoIewrSIsVoJG6beKXVEpUJuUpIpMehchMs4hZBfK6DkpZBsfWRj4bY-WYU8VZQYUamE81tPsyHNLB27BrJte-oyQGj9r9mT_HbatvReeKPgKFUYZ1BFJZtz1DSX-2ZbygxsypyWJz_op7EqidxGu9nGNC5v_9Mn_2fdqnJli2eenEJTZWbx8WlwYNmOPbUqkDZkWUQfOOKwleDday3W0Lv172KoqZwyVwOr78tHX61n898uQSoQtQtk0aobz1y89gcBkcnFr5j0iQ41pe9V2_r8oW16BK37-7EjFlfufX4rqvi06pJBIr5cd7socyCptiXtXzYOLUvtur_riKdjUtY9MHDUkXK32DeB8NE-uBzVbB590689yCGWptTu0R2nC1qQaD4MJ-F5I2J-jFzkFpBX0v-0OAOdtXhksc2LS3Zt5vSMPNz9eHF3W9VfCiumfQOTwO8JzdMs7yxqAD371j9gKCNE7L97QncmuBS2eQnFqSOuOX-n3KQwfS2GhEzlk4w=w1920-h775-no?authuser=0)**

**Observer Pattern (Behavior):** The most important feature of a shopping website is the filter in the search bar. To make this feature process, we are going to use the Observer Pattern due to the interface which is responsible for updating the data at different devices. As a result, the clients are able to access different data easily and faster on their devices.
**![](https://lh3.googleusercontent.com/QGQZiAjvvIlKHWsvftqqpZtZ947FFVaO6MI9dESj5smd5BxNSnj-FyYd8y81Bo0WgY6rfpDMK87773Op_3LbMa3EyycHfzsPqdIBZdUzbBjLsgDJs5lkEdoQa6Hg3zb7v0v_r4dlFHh6urutuVn2i7rcAfReYCg84RyU_Y4Bb1eySG1zaiNWES849Hp4cXEdf3YEqFtfBk6ToDgPt_Uxwe0i7jKtBliYI3RyfqIGVinak37xK6SWanKISCn0Kmzso0L3yGF0tnE97oV_S_ii5-BIw7Z0EX8UD9VzTOSCgcwFYz7s9osltjcDce41LrTMzReCF-JGwRCvGYVvusirGNZxeeWLmcuFCAbeyaCmyZQ02VkQDX0XP6OpmnLmEhmOErSKO0KYS-bHIrqj_ofC0Dn-by5MUyk1rfDfZ81_uAy8uNYux0a_qt6tKCwV6ESQxgcgf1qI3z_pWxm42QurkLFAQmiwhfkoi7GDRvM9coVpj1OFOk1r1mXtd5uQ5HxCqALqaOPxUxZN-FqNFEIxHNcMslLIp6RME2E0XInLnjlYvWipCQd-HTFgkHR4cF7ddnBap5LrerytIQOxIMGICdZHOB3wYOJHIktuSFUw7mUIUL1FBDrtT-WndZCsfF3aMzmE3BvB8kxcEyqd4UdsnCJM453g4lXhfKLil0XPmMZk8lDM12iUYpRgpiAfta7DjmiyQ3A7iPC7bfcrj5qM-g=w1319-h969-no?authuser=0)**

## 6. Design Principles:
**Single Responsibility Principle (SRP):**

As seen above in our design patterns, some functions of the application will have separate classes to make specific requests. For example, DisplayBehavior will work solely as a display interface, with two separate classes to decide between image/title display and title only display.

**Open Closed Principle (OCP):**

An important feature of our application is the ability to decide what supermarket the user wishes to shop at, which is where the extension of supermarkets in our Bridge pattern is useful. The Supermarket class is open for extension as we further develop the chain of stores customers are able to choose from. However, the software in Supermarket itself won’t have to be modified.

**Liskov Substitution Principle (LSP):**

In the case of LSP, the choice of any available supermarket will not affect the outcome of the program. Whether the customer picks Walmart or Target, the system will function as intended. Similarly if the customer decides to use the application via mobile instead of on a computer, it will run the same.

**Interface Segregation Principle (ISP):**

When deciding on a recipe, the customer will have the option to choose from many different recipes of the same cuisine. We made sure to implement as many options as possible to satisfy client-specific needs. Filters to cater for any food related dependency will be modified and extended as we go, with options to sort by calories, carbs, price, and more.

**Dependency Inversion Principle (DIP):**

When adding a product to the shopping list, finer details such as price, name, and amount will be determined in their own extensions of the filter interface. This makes implementing the filter system more reusable, as abstractions of Filter will make the decisions on how to sort by price or amount, and Filter can use their interface.
