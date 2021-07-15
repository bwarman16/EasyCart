# Requirements

Group 03 - “[Easy Cart]”\
Date and location: July 14, 2021\
Group Members: Justin Ceccarelli, Jason Gaglione, Jack Decker, Michael Nelson, Linh Nguyen, Brandon Warman, Jabril Gray

## 1. Positioning
### 1.1. Problem statement
The problem of shopping for the cooking meal affects everyone who just wants to cook and fill them up and the impact of which is the time-consuming or possibly having unhealthy meals.
### 1.2. Product Position Statement
For anyone who is a cooking lover and healthy-oriented person, EasyCart is a web application that makes shopping for meals even easier than before. Unlike others, our product is simple to use and generates a shopping list based on users’ number of grams of fats, carbs or proteins.
### 1.3. Value proposition and customer segment
**Value proposition:** EasyCart is a recipe planning app that allows busy people who like to cook to find recipes that are available at Target, it saves people time of trying to brainstorm and find a recipe, it also takes the guesswork out of if the store will have all the ingredients to make it.\
**Consumer Segment:** People with a lot on their plates who like to cook.

## 2. Stakeholders
- Parents - be able to find healthy, cheap, and new recipes for dinner, lunch and breakfast, and snack time.\
- College Students - these user can use the websites to slowly learn to cook and a budget.\
- Chefs - these clients will be able to add professional recipes for restaurants menu and be able to find quality ingredients.\
- Trainers - this user/client will help others keep track of other users' food intake and be able to help change people's diets for better health.\
- Back End Developers - their roles and responsibilities are to program and build features for the website.\
- Front End Developers - their roles and responsibilities are to build what the user will see and use to find recipe and ingredients.\
- Slimfast Keto - A competitor that has a similar design and, but focuses more on workout base diets.

## 3. Functional requirements(features)
- Recipe suggestions
- Nutritional values available
- Access from phone and computer
- Shopping list
- Substitution for health reasons
- Filter for price and brand
- Track calories
- Price comparisons
- Macro calculations
- Dietary restrictions
- List different store availability 
- Order online
- Check off items

## 4. Non-functional requirements
- Usability: Users may find themselves in situations where time is not in their favor. Quick accessibility and a user-friendly interface will allow for efficiency and memorability.
- Portability/Compatibility: Users like the convenience of planning a recipe on their phone as well as, if not more than, on the computer. Availability across all hardware, operating systems, and browsers is important for product compatibility.
- Performance: One of the main goals of this product is to save time for people who cook often and prepare meals ahead of time. Fast delivery of price listings, item descriptions, and creation of a recipe and shopping list (in one web service) will ensure this product makes the most of everyone’s time.
- Availability: We understand that many users will rely on our service to deliver their food-related needs in a timely manner with utmost accuracy. The goal is for there to be as minimal downtime as possible. If and when there are updates in progress, users will be notified of any issues and maintenance in advance.

## 5. MVP
- Our first feature will be the ability to search for recipes in a certain category such as Italian, Mexican, etc.  Only give the user results that are available at Target.
- First getting a recipe from spoonacular API and then checking to see if the items are available through Target API.
- Displaying the expected nutrition value of recipes.
- From our interviews people desired an easy to use UI that looks nice so we will work on making a nice design for the website.

## 6. Use cases

### 6.1. Use case diagram
![alt text](https://lh3.googleusercontent.com/pPjei6rtoyUuKI_qjI2-4j2Xi8T9F6OcajwOOIUk-pGLlDCyIAGOq4zuCRgqcAnnb7_hJulU_dh3uNNK2grfoMV0IaznKNZHBeHz89XwdnjZmGqydzzfxZZSSPMszzEXhXKTMcdad66xc6rPnHYOIMymqdXYX0pOGKAybub_wijDFYuytG0gsEc_n1dFP44B-YGwrS93L9p8xj0a-e5EGsK6FncSEgl464rcZMz1PmEayWM-euQi6ufYNkW9ZteMXYcezFlGbotSYpCpKOCgheEsq5jT2UokyKE9jGA1BnRvc9bal9Utun_KhnGoQVKC1LRSg69aliuAA0CHNH6fA_ynu0ZSqQwq_TAhDzDPkoszovMSSqIgNznJrMn467TfCDThSxliCKw_YCYX8kSkOUTK-kCTxKagklMoR7IrtQXKBs2AG8e7rTcXkLYxpW94CD3YWDekN3oyjuxc8Q7wgEw2Kf8un3OvxRP9G7BOzMl2vYXdCYbL9fQ4_aTZhGHLmCALLQ1d2uWaUOlkovo88ErhO1Pz4X0u3vFMIpde-M9liReovopGnBd0kpU4rOF4hV5yzowigT26nfChFOOY9LRkCbGSPrsaudYA3iigxVoZUKUxLduOL0zho9XUO6xX0-xzmlirpRxtmKRwTrl6OFLBbKPwKBEL7_rC4WPdazkGvhV8pd5XH35tdHw-4q0yfn4L5W0Q60JP04XAKKSLNQ=w603-h414-no?authuser=0)

### 6.2. Use case descriptions and interface sketch
- A user accesses EasyCart via phone access, uses the price filter to find recipe suggestions, checks store availability, adds to shopping list, and checks off items when bought in store.\
![alt text](https://lh3.googleusercontent.com/io-pNHZu_XFM-FGTeGsBS14KHNpJeSY9fhlGrdcJz5OHOcpX5DrRWttToPrx-f81c20PTgj8CoiKnE49WywnuYMRexB_mV3I-x0ZI5OgiT5lUNR4eYaJMuZw3zkneF5F-HkBVLpewRpWbrAB8szn4X4fgiA2lOosojHIYPA9uQYnw4kiAmoc1r5kdM97dMrXRrhKPdngjcKw9qF4Bxakm1RNsSr-Mfc6sqgsRvCLTkhsHwUpj2u5v9nLqzlHj32oTWWB09SEu3gUPNn2SIjIyFWK-fuzw_10F23tcoh91FPV29d85JF9oldGNfDD3WdCV4ElkUZJvXtsDQp0ulz7V44oTAqoqbQ_23-Qt0n07VqfNqJAjgsMcRv7J_mm1IPsU3RKvccnRNYytty5eYm84njMF-uFZy6G9nAwyl7d49swXo8zP_ezBQeNI7ENUxBI-vRUCzhAQH-gMOCjRKgHNnWCZ2fj0gDlBBxKDJSFaINTq6asN1iniBVxpFof9CE1MUS-NRmS-05OV9rXHzc7KyeZ-lOKcTBcuCBjY9ZfY7aBiLOVEYTIzuJzu1KLmGduwCCr7svTEp9w7-3pBSmHRNmZzJlxswy8lU1L8RNEdr_fpzKFsRkAKCO2Xb2kMEZQRVd16P0JOrXBcpcXXcPZYvOo85PKfBUiFXhOl71QNJskaGNoC5c4xpVJP3oFz2KZvxyXbcOGtn_SYGfwCVXZnw=w200-h173-no?authuser=0)

- A user accesses EasyCart via computer access, uses the health filter to enter health restrictions and find recipe suggestions, checks store availability and nutritional values, adds to shopping list, and orders items online.\
![alt text](https://lh3.googleusercontent.com/mKCWpsmtos5mvJlyYh72f9vWeA0n-ZVFfd1oO1UlrIfUpU8kTVhT6AIxnK8VWsgt0loE4C3nnFEPPGNm-oQddkw132FwLydwQni1XfMOAypqhgDC0BZmUgNIA8mHf5b2Ll8yoWOxqjeA9BqD64cbPSoI0tNnzbtceb-xgFFTsbQstA2q1hZqouna0aDAziOiouUSPEk4v_Yh6hvb1kCKaOBwrWFObiyX5U2s8aKJY7VvUAyp7ayNi-QzS63mFu12a86MCMdqxG9RJzbIMS66E-RYLIMEClD0I27-PPFDm-3owJnDGaLslxNtqz44sZNJAr7YPhmKazGIYssYGT_w3_H5mNdA0Ll2I7tAov0A_NYNV7FXuHT5BrTRKj0Q8KfEXg0p8TGhueEvM0qhb0AXbEG5SxDJVnPiwQY5nTXmjMosL12oOz-emGdeZUWItYV3QQLUiv07VH1j8e4gAVYhRgAPMdZWdqb_ZzglKH8ukt2Pfh2Ce_dVlaDlNfKRDJ_L8CuMacl0GLToObmL9bMbBRj2N0MYC7JHx4pF_2yylL7x5xqUDPVv67wVIe_OH_i-YJo6CVcYieYY7oUP5sj892qSaDjEDSpbDqXG-gsp0CZco_H0OfOV08rjiY8_2YrzZkpDXeluwUUwVR1N2xbQ9yLnXM2e3P5T6q7zue-nqw1VrlrSwcbzKD3VxEF6onKHbryik8V_hdE4AeKSRQ-IPw=w206-h188-no?authuser=0)

- A user accesses EasyCart via computer access, uses the health filter to enter health restrictions and find recipe suggestions, checks store availability and nutritional values, adds to shopping list, and checks off items when bought in store.\
![alt text](https://lh3.googleusercontent.com/v4ecmRkmyroQmgzYavWhjDR8fVFremVLsRf0lKs9ygf1LSUxC0OAsf5TWsxlkQPLP5yOx41hF2nOCYd3nnS1LOZ1hnshyNbHdB6t0-pcMQs1NJ78uSS7cIXEy-3CI32wDjE66OBJp5UnHjuA0j6uE6JMj_rj96IJbFKr0EkexFTJ0Rxvq9DR6wH5OrTQWYyAAXx5vuY8wf6Ag0aPkMxEMCW6oIQfQQg4dq9yXmRlXlh0b45blx_juI8iTI4b7qKexhr9WdlD87cHWbRLT6d5QzA3i5H6O1KIkUGVFXNbhAsi91mtnoS5__G6eGFV3J12Ry_FuW0hzt89If9trbb-kVUkrkwHMk2bEu98eoEeWol6ofOJykHPmLcfS6m3pdtlEm-MRYWSEgKIRbne3gDNAOvOh1OvCLsRi-p0NqCQjGvUsiVh9_y28JeUpf4cWujQHzx8yCArU67vFx50csAJ_0ccjxW1QlMxp_muzRoUhgKJicfXi8403Cxi86WoMVYAyuajF210lyguXO2WhHJwPlBDWz0Sm4tGsaLp0oHtHTrTxM7BIVow0kOG-8CJzkDVgjvWakmGC0xyQIgi2xzF8SErkPAuJqCDHztMizwg1y-UwbJ3AmON1AhVZExvgNh35qSHuwjRmZ6RB3yBQPK0bbmPZTj0syAvstRJ-B2kotoGjBFn8MFqCCacGQeTqlfRJNEVAWEQXhr_0fmIUgeVGg=w186-h171-no?authuser=0)

- A user accesses EasyCart via computer access, uses the health filter to enter health restrictions and find recipe suggestions, checks store availability, adds to shopping list, and orders items online.\
![alt text](https://lh3.googleusercontent.com/oL1PgEpx9xXD4RwR4d3XZizx-PZA8DgSZpRYxYglNtOcx1XvdBAsmP8VM0UUYb0pWbq3AxLsGgGPMSep5NpKaD-O82iMF_xJrgSkvuzPfSClN1FjUvwhIjZhnSQHDxHUUk3cfh9XxELgCQ3m_ME92bCJFm0fVzqJBR8oPw9Z7uB6Js0uDJCFKnWhd27nia7y2plYdvf_5mr53l6vNuv_9tAxOLQgytBklgxFDo2bWeebRTYSd0f-qE3Jnsu8ih-s4kBqKQEv-Dh8PsutjLjN6P9jMQG7xk2XIZA6809r8vyRt82JotgT4qyRWle7c3QgufId8_Wc5yxMDto5BNQXGWRKq0q81L3As833sY1BMH10qLl3sBLtix8sotiBRLE9II6-MsT0QVD57_1Cl2wiZceZpi_kQV8YwIwYDczPU2AcMH_Vb1iAdGgrz_RA3ud9ARxjTyu5vDC2Wj9NvOzrKX2DB1uTF-c0KyIUE4K_LbsbJkr9_B-EtRNSq2DPAe82Pjt8QGbgDGEQTdi_S0Ns5dcfE2XDc-9jmIVT6mKc6b7GSey76IBLxUrb7VyYbhTjHmRXxuTBLYrUO0ZqULxF0eyX4kyy49HSOFSBpU1s11BJeZ-RxLc6a7gfOb7eii1Te0gLv5SyQlKEylvLFeh06TmU8xz4Bl6uPTgGMHMiRO93VQ5pywT9H1b3M0NdaPORIHH17kctp-rLJm6Wjmnouw=w214-h199-no?authuser=0)

- A user accesses EasyCart via computer access, uses the price filter to find recipe suggestions, checks store availability and nutritional values, adds to shopping list, and checks off items when bought in store.\
![alt text](https://lh3.googleusercontent.com/NUsONj_D4JLziLIBNb6IXTTIyz9cMAnvNuRumvfrPaVszJW6Y6vSWMvElXpz8eanQIYW0XIcf4Ryk5y2lLu63qziauBQgRbnGVjEER-2hY6B5GHqz2g_unSJyyJFiIvdgN92jlwqn1H8uzXNSI9xWVYd4vcBgHkZzFhupFZpNl-ehULncRaT3O7qTxyyASTYKOodTJxJecf43crP4wjh7xskOrYiozxzveJ9jRI863Oeh3tIWrgB3lC2MoEQ_v4KvWeKYD9L0q-Lp0kVvZIibA5OQ8X3xsyKAtF9gBx_7A3JDWrPb98nTPaedlW5Z-rY8wHF_D5yGAsn_Eii_1jqWyQAQnUauKcbMkfQQfBuHmKDYEEm4TgvAbeVnjTcWyuV4OSx3yUlk3ll43-vJ-L1mMOfDjA2asWZsOPmPjMmtS6sk-r99sXtkkrvJC1eaIW0PkRInQM75QcouSxOauW0SQPqRMdi0eLSwVaAIR1Dlnwlis8DS4LjKlc-Lz6dBYeeYMKzGNWSc4xqozEE2polKo4g86IoU6UCnY_zakh1OMOwEIE4QeIOu-AjK0ahtmMyoMeOLBj9mgGcmQDARbuBk3S5gMkC6Lv-B-ND5tAraG0SK59JDKBF9Vw0qyDsaVEw1fbxWARv9hE6TvFyYuhWKgSUFQANKrCpjCXd2aSKh6P53FJaIhBP5M9sjd25eOrvSBXDd8smT7i4JgmJgmwhBQ=w233-h210-no?authuser=0)

- A user accesses EasyCart via phone access, uses the health filter to enter health restrictions and find recipe suggestions, checks store availability, adds to shopping list, and orders items online.\
![alt text](https://lh3.googleusercontent.com/xj8WtnbrsyeivwE-dxjNEp_8ff9G8R5X6YWT26Tp7xWZs9WIpbz14gr2xXpraeEQ1MudbPRjS5H4DVM99Mchlwld0PHCfbRsiyXTsACk9CzcYhPU1P0vkleC3RzHzC7ahIKU_nP9OrTNSn8m5zNYovm83AfeGjXudXD7sUq3e_uJ1O_4fwBpDbPXlBNYbyzHEEfBCVqfKW6KNoJNwG5p5uEVIfiu-jwVsS24pdnebPNQVPwqp7NP3MLX2q7UDRfxeYyu_FUelwWpZtiYKOnx4w9ugrZk28_ezyNaUQcXoaL6rsG9imPLar_5SF9YE5-hg7Y3e4WDmEXBBl4yxeDI_ew3hdQKLFCBr4eJXSdm3kHuHAEja6zL8bTgmEI5tATIPbPSP1-aSuCeBerJdNUloDafiJkJBbAsJjlB8mWYK4dbMWy7JPb1xRY_De_M-1ifER859heP_yCJhBsmIQdyQAZsfqckblvQqWlqcteGV8TZEcht3rAywqtj7Xq-s8q_baZ9k2qNhEIafzADU85CUV8Tz6K_b-EfsQnRjPwlbmUbLyqH45k7RF0Xy5YtzLbjuO2KL23koPrJkMywwL3xeJd95e-XSDORGQQMLim0DETqeLQpobaD6JVQq_RzeBq2vB_QgWGXOwoYIuFnkoMaQW2sXqJ1-O18IoZvopts-NkQBo93eWew1uAPojRIzEb7WRZNWPCqWZZfQOJsu2AKpQ=w274-h254-no?authuser=0)

- A user accesses EasyCart via phone access, uses the price filter to find recipe suggestions, checks store availability and nutritional values, adds to shopping list, and orders items online.\
![alt text](https://lh3.googleusercontent.com/blvIveWnRtuzFa4p8yybEkcRtPswptTiu0wto1o-95VCYX3I6RlBNnhEejGDlYVh1DdyIl3Y4VLENi0ZmZ2xehxQfCOKga708UbbvU7QgQZLfsiIQ3fCbyKpTx--1RbSxEOQ91lJ9Sg_4ZidWy2q_IrlIUHOvBq3t9_zf787ClDz9j1J0Lv0x8_dMfVKTrDq9Hdb780IUwfXKgpvcc3Qn_cwKa9Fti-s-KJyt9Ha-L7Iyt07T9TEE5xDUuf2p6C75aLP6tw9AmAxt_RiDXW3rhS5CFnk7kobrovAO7cocaVNMUi01ulmGEh8E0NkeHQy4flVQtwy8LtWZ1WisouXzZR2FJxvaYnpQhHuMy-wuF0EV9LicbpTiyDEqRgTaFm6oynYFhXhZlrYbFvQtz1aR4a1hLEgUPdTSBTDV_qK662oY3IU5JGkuMatppg0xGbNbGCBMaRtU_JfVzOhzCvgL3bbSe3X0WoCanaOxe3t7Qr0o6y58ZCdGlyFHrlfhhfwiZg_l4l2adhL6721keb73jvDwCo6QNrXCihVEWlUOgM9PFigFvVH_2MXFCUoAaP5nsMvcnhwtfXUl4pRcjRXD8klUcdllpOT3WBOyWk6dJ34PMlPQjTV0s00UGhsCf49HU6e9yCtJ9bZz6rWE8Wou9H3ICUJGIB_FMFcaifCX4H_cAuBD6s4pUUZV9YjGzfE9olx8iPspIzzxrDvnNjqJw=w298-h258-no?authuser=0)

## 7. User stories
- “As a fitness wellness major, I want an application to find new recipes so that I can stay in shape”
- “As a college student, I want a program to recommend different recipes so that I can shop quicker and smarter.”
- “As a college student who has a lot to do, I want an app that will give me available recipe recommendations”
- “As a user who loves cooking, I want the interface of the application to be simple so that I can easily navigate it.”
- “As a user, I want to receive the email notifications so that I can stay informed.”
- “As a user who eats a lot I want to be able count my calories and lost weight”
- “As a developer, I want to be able keep adding features so it will become mainstream” 
- “As a user, I want to see only gluten free options so I can avoid seeing options that I cannot eat.”
- “As a user, I would like to have it schedule a pickup order for me so I don’t have to spend time shopping.”
- “As a user, I want to be able to sort by brands so that I can pick the brand that I like the most.”
- “As a user, I want to be able to sort by price in order to save money on recipes I enjoy.”
- “As a user I want to be able to enter my health restrictions and be able to find recipes and ingredients nearby that are suitable to my needs.”
- “As a user, I want to save my favourite recipes so that I can easily go shopping for my favourite food”
- “As a user, I want to share my location with the application so that I can easily know where the nearest supermarkets locate”

## 8. Issue Track
	Trello URL: https://trello.com/b/2TDMYnVs/project-board
![alt text](https://lh3.googleusercontent.com/6zZZ5ivobtx3iLPH_og2GPKYyaT0EzhWSUWnWSJIqr2nTDPIIfC4DL7QqLvSy_szh-qa24Vgi78pqoQFkSCZFxZ4bI95h4CVO_dfUNPStrNvMdbtbS9wTa5Frpjm9wQyZLdhWJnxUJfbDNUZSTQNZj-bXGEqLoo_XLc9eNFvADK6hdT5RUhjq9HnIJpew4TGzr-aLXYBUZP0HvQ0NeDW_cOs81qLXcqM0o5d0d6Yyqkrd7f705224lPoJMmG46aA9nhRDd_GGbRMR7p0LpwO_l9JOj-c2yYU-qX4utpUdloLkWa6Vz7hOVkUeo1soFTBrBKnv_xKOZQirY8OUXkIkEAkrQAuYkucd1e_GIdvplHYPErTqUsphkJ0mqpw4EoRxvtG7tY_RLzcBrDv2D5Ye2sB_lD2nPtPxEfmq_LemHga2WgkHes9MkW5HhcdxHKwgh1mrlaf8431bCkVMEZTznex-rL9H00YEgbmocc5VrjrdGe5ZQMwjamWcJj9rAZHtg7nezURni4e1WdYyDfMzsrYm9Gdrw-pd6rBoDHfFF1E8NIc-oeMRmCyEX-RtwTSJ4gT4mNmNMxOC9UuthpHPeeqWJBodObEWozOZ5kUK40Ugx0BvwXr0xUu0AdJ9xPDoOhPLM1IOByO9VaxOfFlmUQFTQ82_jJiQ44vtEgcQDw4ORMesgL4DCOoX-r4auTqRkcwJLOAVXSubYnnzQDBUw=w1407-h642-no?authuser=0)
