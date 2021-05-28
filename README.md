# API Documentation


### Auth Routes
<details>
<summary>
1. Get Auth Token and Refresh Token
</summary>

<br>

**POST :**  `/api/token/`

Accepts a JSON object containing 'username' and 'password'.
Example :
```json
{
    "username": "abc",
    "password": "password"
}
```

#### Responses :
**On success** 
**Status** = 200
If the user exists, the route returns a JSON object containing auth token and refresh token

**Sample Response**
```json
{
  "refresh": "auth.token.here",
  "access": "refresh.token.here"
}
```

**On Failure**
**Status** = 401 Unauthorized
If the user does not exist in the User table, returns a JSON object containing a single item 'detail'

```json
{
  "detail": "No active account found with the given credentials"
}
```
</details>


<details>
<summary>2. Get new access token using refresh token</summary>

<br>

**POST :** `/api/token/refresh/`

Accepts a JSON object with refresh token

**Sample request**
```json
{
    "refresh": "some.refresh.token"
}
``` 

#### Responses
**Success Response**
**Status** = 200 OK
<br>Returns a new access token
```json
{
  "access": "new.access.token"
}
```

**Failure Response**
**Status** = 401 Unauthorized
<br>In case the refresh token is invalid
```json
{
  "detail": "Token is invalid or expired",
  "code": "token_not_valid"
}
```
</details>


### Products

<details>
<summary>1. Fetch all products</summary>

**Type:** GET

`/api/products/`

**Sample Response**
Returns an array of JSON objects containing products.
Status = 200 OK
```json
[
  {
    "id": 1,
    "title": "Lenovo Legion 5",
    "description": "4th Gen AMD Ryzen 5 (4600H) | Speed: 3.0 GHz (Base) - 4.0 GHz (Max) | 6 Cores | 8MB Cache",
    "price": 67990,
    "createdAt": "2021-05-28T12:00:00.800172Z",
    "stock": 100,
    "rating": 5,
    "imageUrl": "http://localhost:8000/61ItfhQmaFL._SL1000_.jpg",
    "seller": 3
  }
]
```

</details>


<details>
<summary>2. Create a new product</summary>

**Type:** POST

`/api/product/create/`

**Note:** This is a protected route i.e. user must be authorized. Provide your Auth Token in the 'Authorization' header as 'Bearer ${token_here}'.

**Sample Request**
```json
{
    "title": "ThinkPad E14",
    "description": "AMD Ryzen 5 4650U Professional processor, 2.1Ghz base speed, 4.0Ghz max speed, 6Cores, 8Mb Smart Cache",
    "price": 53990,
    "stock": 50,
    "rating": 4,
    "seller": 3
  }
```

**Sample Success Response**
Returns a JSON object of the newly added product
**Status** = 201 Created
```json
{
  "id": 2,
  "title": "ThinkPad E14",
  "description": "AMD Ryzen 5 4650U Professional processor, 2.1Ghz base speed, 4.0Ghz max speed, 6Cores, 8Mb Smart Cache",
  "price": 53990,
  "createdAt": "2021-05-28T13:50:52.337692Z",
  "stock": 50,
  "rating": 4,
  "imageUrl": null,
  "seller": 3
}
```


**Failure Responses**
- If the auth token is invalid
**Status** = 401 Unauthorized
```json
{
  "detail": "Given token not valid for any token type",
  "code": "token_not_valid",
  "messages": [
    {
      "token_class": "AccessToken",
      "token_type": "access",
      "message": "Token is invalid or expired"
    }
  ]
}
```
</details>