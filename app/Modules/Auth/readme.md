# Auth Module Server Api

## Revision

|Date|Remark|
|--|--|
|`2019/08/02`|Complete Auth Module|
|`2019/08/07`|Add logout route|

## URI

|Method|Uri|Description|
|--|--|--|
|POST|`/auth/register`|Register an unexisting user \*|
|POST|`/auth/login`|Login as an existing user \*|
|POST|`/auth/logout`|Logout the current user \*|

[\* Need request body](https://github.com/Aoi-hosizora/Biji_BackEnd/blob/master/app/Modules/Auth/readme.md#request-body)

## Request Header

+ `POST /auth/logout`

|Key|Is Required|Description|
|--|--|--|
|`Authorization`|Required|User Login Token|

## Request Query Param

+ Nothing

## Request Body

+ `POST /auth/register`

|Field|Type|Is Required|Description|
|--|--|--|--|
|`username`|`string`|Required|Registered Username|
|`password`|`string`|Required|Registered Password|

Example:

```json
{
    "username": "aaaaaaaa",
    "password": "aaaaaaaa"
} 
```

+ `POST /auth/login`

|Field|Type|Is Required|Description|
|--|--|--|--|
|`username`|`string`|Required|Login Username|
|`password`|`string`|Required|Login Password|
|`expiration`|`int`|Not Required \*|Token Timeout Expiration (second)|

\* Expiration default for 30 days

Example:

```json
{
    "username": "aaaaaaaa",
    "password": "aaaaaaaa",
    "expiration": 500
} 
```

## Response Header

+ `POST /auth/login`

|Key|Description|
|--|--|
|`Authorization`|Return User Login Token|

## Response Body

+ `POST /auth/login`
+ `POST /auth/register`

|Field|Type|Description|
|--|--|--|
|`username`|`string`|Login Username|
|`message`|`string`|Login Success Or Register Success|

Example:

```json
{
    "username": "aoihosizora",
    "status": "Login Success"
}
```

+ `POST /auth/logout`

|Field|Type|Description|
|--|--|--|
|`title`|`string`|Logout Success|

Example:

```json
{
    "title": "User \"aoihosizora\" logout success"
}
```

## Error Message Type

+ Public error code and error message type see [Modules](https://github.com/Aoi-hosizora/Biji_BackEnd/blob/master/app/Modules/readme.md)

|Message|Description|
|--|--|
|`Register Error`|(Something wrong with the server)|
|`Login Error`|Password error or use a wrong token|
|`User Exist Error`|Register an exist username|
|`User Not Exist Error`|Login as an unexist username|
|`Username Format Error`|Username length should be in `[5, 30)`|
|`Password Format Error`|Password length should be in `[8, 20)`|