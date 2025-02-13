# Note Module Server Api

## Revision

|Date|Remark|
|--|--|
|`2019/08/02`|Complete note module|
|`2019/08/03`|Add `ImgBlue`|
|`2019/08/07`|Add `PushNote` and `PushGroup` route|
|`2019/08/09`|Add `DeleteImg` route|

## URI

|Method|Uri|Description|
|--|--|--|
|`GET`|`/note/all`|Get user all notes|
|`GET`|`/note/one`|Get user one notes \*|
|`POST`|`/note/update`|Update note content \*\*|
|`PUT`|`/note/insert`|Add a new note \*\*|
|`DELETE`|`/note/delete`|Delete an old note \*\*|
|`POST`|`/note/push`|Through log update notes \*\*|
|`GET`|`/group/all`|Get user all groups|
|`GET`|`/group/one`|Get user one groups \*|
|`POST`|`/group/update`|Update group content \*\*|
|`PUT`|`/group/insert`|Add a new group \*\*|
|`DELETE`|`/group/delete`|Delete an old group \*\*|
|`POST`|`/group/push`|Through log update groups \*\*|
|`POST`|`/note/img/upload`|Upload user note image \*\*|
|`GET`|`/note/img/blob/<usr>/<img>`|Download user note image|
|`DELETE`|`/note/img/delete`|Delete user note image \*\*|

[\* Need request query param](https://github.com/Aoi-hosizora/Biji_BackEnd/blob/master/app/Modules/Note/readme.md#request-query-param)

[\*\* Need request body](https://github.com/Aoi-hosizora/Biji_BackEnd/blob/master/app/Modules/Note/readme.md#request-body)

## Request Header

+ Global (Except `GET /note/img/blob/<usr>/<img>`)

|Key|Is Required|Description|
|--|--|--|
|`Authorization`|Required|User Login Token|

## Request Query Param

+ `GET /note/all?`

|Field|Type|Is Required|Description|Remark|
|--|--|--|--|--|
|`id`|`int`|Required|Queried note id||

+ `GET /group/all?`

|Field|Type|Is Required|Description|Remark|
|--|--|--|--|--|
|`id`|`int`|Required|Queried group id||

## Request Body

+ `POST /note/update`
+ `PUT /note/insert`
+ `DELETE /note/delete`

|Field|Type|Is Required|Description|Remark|
|--|--|--|--|--|
|`id`|`int`|Required|Note ID|Primary key|
|`title`|`string`|Required|Note Title|Max length 100|
|`content`|`string`|Not Required|Note Content||
|`group_id`|`int`|Required|Note Group||
|`create_time`|`datetime`|Required|Note Create Time|Format like `%Y-%m-%d %H:%M:%S`|
|`update_time`|`datetime`|Required|Note Update Time|Format like `%Y-%m-%d %H:%M:%S`|

Example:

```json
{
    "id": 1,
    "title": "New Title",
    "content": "New Content",
    "group_id": 1,
    "create_time": "2019-08-02 17:00:00",
    "update_time": "2019-08-02 17:00:00"
}
```

+ `POST /group/update`
+ `PUT /group/insert`
+ `DELETE /group/delete`

|Field|Type|Is Required|Description|Remark|
|--|--|--|--|--|
|`id`|`int`|Required|Group ID|Primary|
|`name`|`string`|Required|Group Name|Max length 100|
|`order`|`int`|Required|Group Order||
|`color`|`int`|Required|Group Color|Fromat like `#FFFFFF`|

Example:

```json
{
    "id": 1,
    "name": "G1",
    "order": 1,
    "color": "#FFFFFF"
}
```

+ `POST /note/push`
    + Array
    + Same with `PUT /note/insert` Request Body

+ `POST /group/push`
    + Array
    + Same with `PUT /group/insert` Request Body

+ `POST /note/img/upload`

|Field|Type|Is Required|Description|Remark|
|--|--|--|--|--|
|`noteimg`|`File`|Required|Image File|Only support `jpg, png, 'jpeg, bmp`|

+ `DELETE /note/img/delete`
    + Array

|Field|Type|Is Required|Description|Remark|
|--|--|--|--|--|
|`username`|`string`|Required|Deleted Image Username||
|`filename`|`string`|Required|Deleted Image Filename|Contain Img extension|

Example:
```json
[
    {
        "usernsme": "aoihosizora",
        "filename": "2019080920071958.jpg"
    }
]
```

## Response Header

+ `GET /note/img/blob/<usr>/<img>`

|Key|Description|
|--|--|
|`Content-Type`|`image/png`|


## Response Body

+ `GET /note/all`
+ `GET /group/all`
    + Array
    + Content is same as [request body](https://github.com/Aoi-hosizora/Biji_BackEnd/blob/master/app/Modules/Note/readme.md#request-body)

+ `POST /note/update`
+ `PUT /note/insert`
+ `DELETE /note/delete`
+ `POST /group/update`
+ `PUT /group/insert`
+ `DELETE /group/delete`
    + Same as [request Body](https://github.com/Aoi-hosizora/Biji_BackEnd/blob/master/app/Modules/Note/readme.md#request-body)

+ `POST /note/push`
+ `POST /group/push`

|Field|Type|Description|Remark|
|--|--|--|--|
|`message`|`string`|Push status||
|`detail`|`string`|Push items length||

+ `POST /note/img/upload`

|Field|Type|Description|Remark|
|--|--|--|--|
|`message`|`string`|Upload status||
|`detail`|`string`|Group Name|New filename, please update note content|

Example:

```json
{
    "message": "Image upload success",
    "detail": "2019080223044764.png"
}
```

+ `GET /note/img/blob/<usr>/<img>`
    + Response `Content-Type: image/png`

Example: `GET /note/img/blob/aoihosizora/2019080223044764.png`

+ `DELETE /note/img/delete`

|Field|Type|Description|Remark|
|--|--|--|--|
|`message`|`string`|Delete status||
|`detail`|`int`|Deleted items count||

Example:

```json
{
    "message": "Images delete success",
    "detail": 3
}
```

## Error Message Type

+ Public error code and error message type see [Modules](https://github.com/Aoi-hosizora/Biji_BackEnd/blob/master/app/Modules/readme.md)

|Message|Description|
|--|--|
|`Not Exist Error`|Delete/Update an unexist note or group|
|`Exist Error`|Insert an exist note or group|
|`Insert Error`|Insert into database error|
|`Update Error`|Update database error|
|`Delete Error`|Delete from database error|
|`Image Upload Error`|Image not exist or upload error|
|`Image Type Error`|Image type is not supported|
|`Image Not Exist Error`|Image type not exist|