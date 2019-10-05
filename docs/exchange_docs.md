## Exchange
Exchange is the buying and selling portion of the Cozy project. Here users will be able to buy and sell goods (currently only adjusted for fashion, but will later on be expanded.)

All links involving exchange will being with ```exchange/```

-```exchange/info```: Returns the information on the exchange service i.e whether it is online or not.
```json
{
    "service": {
        "service": "exchange",
        "status": "online",
        "message": {
            "important": false,
            "text": "Service is Online"
        }
    }
}
```
-```exchange/category```: Returns a list of the various different categories.
```json
[
    {
        "id": 3,
        "name": "jackets"
    },
    {
        "id": 2,
        "name": "pants"
    },
    {
        "id": 1,
        "name": "shirts"
    }
]
```

- ```exchange/category/[Primary Key for Category]```: Just returns the information regarding a specific category (NOTE, SHOULD LATER BE CHANGED TO ALSO SHOW LIST OF ITEMS THAT ACTIVELY BEING SOLD IN THIS CATEGORY)
```json
{
    "id": 1,
    "slug": "shirts"
}

-```exchange/item/``` : Returns a list of items that are currently for sale, as well as general info on the items.
```json
[
    {
        "id": 2,
        "slug": "supreme-yankee-box-logo-t-shirt",
        "name": "Supreme Yankee Box Logo T-shirt",
        "seller_name": "test",
        "images": [
            {
                "id": 2,
                "url": "http://localhost:8000/media/images/receipt.png",
                "index": 1
            }
        ],
        "category": 1,
        "category_name": "shirts",
        "lastActive": "2019-08-31T15:03:44Z",
        "visible": true,
        "stock": 1,
        "price": "150.00"
    },
    {
        "id": 1,
        "slug": "midnight-studios-arch-logo-t-shirt",
        "name": "Midnight Studios Arch Logo T-Shirt",
        "seller_name": "x",
        "images": [
            {
                "id": 1,
                "url": "http://localhost:8000/media/images/graph.png",
                "index": 1
            }
        ],
        "category": 1,
        "category_name": "shirts",
        "lastActive": "2019-08-31T15:02:08Z",
        "visible": true,
        "stock": 1,
        "price": "90.00"
    }
]
```
-```exchange/item/create``` : Post API call to create a Item. The following is the form.
```json
{
    "name": "",
    "description": "",
    "material": "",
    "category": null,
    "primaryImage": null
}
```

-```exchange/item/[ID of the Item]``` : Returns the information of a specific item .
```json
{
    "id": 1,
    "slug": "midnight-studios-arch-logo-t-shirt",
    "seller_name": "x",
    "name": "Midnight Studios Arch Logo T-Shirt",
    "images": [
        {
            "id": 1,
            "url": "http://localhost:8000/media/images/graph.png",
            "index": 1
        }
    ],
    "description": "New T-shirt, only worn once. 10/10 Condition",
    "material": "Cotton",
    "category": 1,
    "category_name": "shirts",
    "price": "90.00",
    "lastActive": "2019-08-31T15:02:08Z",
    "visible": true,
    "stock": 1
}
```

-```exchange/item/edit/[ID of the Item]``` : Lets the user create a POST request to change the information of a specific item. Here are the fields that can be changed. (NOTE with permissions, only an admin user, or the creator of the item can edit an item using this call):
```json
{
    "name": "Midnight Studios Arch Logo T-Shirt",
    "description": "New T-shirt, only worn once. 10/10 Condition",
    "material": "Cotton",
    "category": 1,
    "primaryImage": "http://localhost:8000/media/images/graph.png"
}
```

-```exchange/item/delete/[ID of the item]```: API call POST call to delete the item. (Only an admin, or the creator of the item can use this call successfully)

-```exchange/transactions``` : Returns a list of transactions

-```exchange/transactions/create``` : Returns a list of transactions

-```exchange/transactions[PRIMARY ID of Transaction]```: Returns the detailed information of a specific transaction

-```exchange/transaction/edit/[Primary ID of Transaction]```: Edits the information of a transaction, only those invovled in the transaction are allowed to edit this information or an admin.
