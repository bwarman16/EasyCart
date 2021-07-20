import requests


class TargetCart:
    # initialize variables and sets store ID to default to 935 (flagstaff)
    def __init__(self, zipCode):
        self.storeInfo = {}
        self.storeID = "935"
        self.storeAddress = {}
        self.shoppingCart = {}
        self.getLocalStore(zipCode)
        self.getLocalStoreID()
        self.getLocalStoreAddress()

    # Uses zip code to find the closest target to you.
    def getLocalStore(self, zipCode):
        url = "https://target1.p.rapidapi.com/stores/list"

        querystring = {"zipcode": str(zipCode)}

        headers = {
            'x-rapidapi-key': "25c9120b91mshda2f6434b6ba640p12800cjsn7e5efc1cb1b3",
            'x-rapidapi-host': "target1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        self.storeInfo = response.json()[0]

    # Not sure if we will ever need the address but this saves a dictionary with address info
    def getLocalStoreAddress(self):
        self.storeAddress = self.storeInfo.get("locations")[0].get("address")

    # Local store ID is used to query your local store, will default to 935(flagstaff) if no store found
    def getLocalStoreID(self):
        self.storeID = str(self.storeInfo.get("locations")[0].get("location_id"))

    # Adds item to theoretical shopping cart.  Keyword as key and QueryTarget object as value
    def addItemToCart(self, query):
        self.shoppingCart[query.keyword] = query


class QueryTarget:
    def __init__(self, targetID, keyword):
        self.keyword = keyword
        self.targetID = targetID
        self.queryResult = {}
        self.itemPrice = 0
        self.itemName = ""
        self.itemTCIN = ""
        self.queryStore()
        self.getItemPrice()
        self.getItemTCIN()
        self.getItemName()

    # Query local target and saves list of products related to keyword searched.
    # Adds the most relevant option to a dictionary with keyword as key and API result as value
    def queryStore(self):
        url = "https://target1.p.rapidapi.com/products/v2/list"

        querystring = {"store_id": self.targetID, "category": "5xt1a", "keyword": self.keyword, "count": "5",
                       "offset": "0",
                       "default_purchasability_filter": "true", "sort_by": "relevance"}

        headers = {
            'x-rapidapi-key': "25c9120b91mshda2f6434b6ba640p12800cjsn7e5efc1cb1b3",
            'x-rapidapi-host': "target1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        self.queryResult = response.json()

    # Helper function to get the price of an item.
    def getItemPrice(self):
        tempResult = self.queryResult.get("data").get("search").get("products")
        if len(tempResult) != 0:
            self.itemPrice = tempResult[0].get("price").get("current_retail")
        else:
            self.itemPrice = None

    def getItemTCIN(self):
        tempResult = self.queryResult.get("data").get("search").get("products")
        if len(tempResult) != 0:
            self.itemTCIN = tempResult[0].get("item").get("tcin")
        else:
            self.itemTCIN = None

    def getItemName(self):
        tempResult = self.queryResult.get("data").get("search").get("products")
        if len(tempResult) != 0:
            self.itemName = tempResult[0].get("item").get("product_description").get("title")
        else:
            self.itemName: None


target = TargetCart(85255)
print(target.storeID)

result = QueryTarget(target.storeID, "bacon")
target.addItemToCart(result)

print(target.shoppingCart)

result = QueryTarget(target.storeID, "eggs")

target.addItemToCart(result)

print(target.shoppingCart)
