## Boards
For all API calls involving Boards they will start with ```boards``` in the URL.
The following API involving boards are

- ```boards/list```: Returns a list of all of the boards. Ex.
```json
[
    {
        "id": 2,
        "name": "fashion",
        "tag": "fa"
    },
    {
        "id": 3,
        "name": "general",
        "tag": "g"
    },
    {
        "id": 1,
        "name": "tech",
        "tag": "t"
    }
]
```
- ```boards/info```: Returns service info along with a list of all boards. Ex.
```json
{
    "service": {
        "service": "boards",
        "status": "online",
        "message": {
            "important": false,
            "text": "Service is Online"
        }
    },
    "boards": [
        {
            "id": 2,
            "name": "fashion",
            "tag": "fa"
        },
        {
            "id": 3,
            "name": "general",
            "tag": "g"
        },
        {
            "id": 1,
            "name": "tech",
            "tag": "t"
        }
    ]
}
```
- ```boards/board/[Tag Of Board]```: Return general info of the specific board, as well as the active threads on the site. NOTE: by adding /active, /archived or /locked, this query will automatically filter the threads within the boards. For example ```boards/board/t/active``` will return all of the active threads within the technology board. This API call is best used if we are

```json
{
    "id": 3,
    "name": "general",
    "tag": "g",
    "threads": [
        {
            "id": 1,
            "bid": 0,
            "title": "hello all",
            "blurb": "i hate k-pop",
            "views": 0,
            "replyCount": 0,
            "imageCount": 0,
            "created": "2019-08-20T23:58:12.835225Z",
            "poster": {
                "id": 1,
                "username": "mem",
                "profileImg": null,
                "location": "Nowhere",
                "bio": ""
            },
            "board": 3,
            "image": null
        },
        {
            "id": 2,
            "bid": 1,
            "title": "anyone else voting for joe biden?",
            "blurb": "i love his stance on medicare",
            "views": 0,
            "replyCount": 0,
            "imageCount": 0,
            "created": "2019-08-20T23:58:42.711575Z",
            "poster": {
                "id": 1,
                "username": "mem",
                "profileImg": null,
                "location": "Nowhere",
                "bio": ""
            },
            "board": 3,
            "image": null
        }
    ]
}
```
- ```boards/board/create``` : Only admins can use this call. The required information is as follows:
```json
{
    "name": "",
    "tag": ""
}
```
- ```boards/threads ``` : List of active threads:
```json

[
  {
      "id": 3,
      "bid": 4,
      "title": "Arch Linux is the BEST!",
      "blurb": "clearly the best OS",
      "views": 0,
      "replyCount": 1,
      "imageCount": 0,
      "created": "2019-08-26T23:48:22.817600Z",
      "poster": {
          "id": 1,
          "username": "test",
          "profileImg": null,
          "location": "",
          "bio": ""
      },
      "board": 1,
      "image": null
  },
  {
      "id": 4,
      "bid": 5,
      "title": "I really like QT Browser",
      "blurb": "I love open source",
      "views": 0,
      "replyCount": 0,
      "imageCount": 0,
      "created": "2019-08-26T23:48:00.561335Z",
      "poster": {
          "id": 1,
          "username": "test",
          "profileImg": null,
          "location": "",
          "bio": ""
      },
      "board": 1,
      "image": null
  }
]
```
- ```boards/thread/create```: API call to create a new thread. Needs the following information:
```json
{
    "title": "",
    "message": "",
    "poster": null,
    "image": null,
    "board": null
}
```
- ```boards/thread/(?P<pk>[0-9]+)``` : Call upon a specific thread, and receive all the information within it :
```json
{
  "id": 3,
  "title": "Arch Linux is the BEST!",
  "bid": 4,
  "created": "2019-08-26T23:48:22.817600Z",
  "poster": {
      "id": 1,
      "username": "test",
      "profileImg": null,
      "location": "",
      "bio": ""
  },
  "tag": "t",
  "blurb": "clearly the best OS",
  "board": 1,
  "replyCount": 1,
  "latestReplyTime": "2019-08-26T23:48:22.817624Z",
  "views": 0,
  "imageCount": 0,
  "posts": [
      {
          "id": 5,
          "bid": 4,
          "created": "2019-08-26T23:47:44.595775Z",
          "poster": {
              "id": 1,
              "username": "test",
              "profileImg": null,
              "location": "",
              "bio": ""
          },
          "message": "clearly the best OS",
          "image": null
      },
      {
          "id": 7,
          "bid": 6,
          "created": "2019-08-26T23:48:22.819355Z",
          "poster": {
              "id": 2,
              "username": "x",
              "profileImg": null,
              "location": "Nowhere",
              "bio": ""
          },
          "message": "Personally, i like Debian",
          "image": null
      }
  ],
  "image": null
}
```
- ```boards/posts``` : Receive a list of all the most recent posts
```json
[
    {
        "id": 7,
        "bid": 6,
        "created": "2019-08-26T23:48:22.819355Z",
        "poster": {
            "id": 2,
            "username": "x",
            "profileImg": null,
            "location": "Nowhere",
            "bio": ""
        },
        "message": "Personally, i like Debian",
        "image": null
    },
    {
        "id": 6,
        "bid": 5,
        "created": "2019-08-26T23:48:00.563599Z",
        "poster": {
            "id": 1,
            "username": "test",
            "profileImg": null,
            "location": "",
            "bio": ""
        },
        "message": "I love open source",
        "image": null
    },
    {
        "id": 5,
        "bid": 4,
        "created": "2019-08-26T23:47:44.595775Z",
        "poster": {
            "id": 1,
            "username": "test",
            "profileImg": null,
            "location": "",
            "bio": ""
        },
        "message": "clearly the best OS",
        "image": null
    }
]
  ```

- ```boards/post/create``` : API call to make a post
  ```json
  {
    "message": "",
    "poster": null,
    "thread": null,
    "image": null,
    "board": null
  }
  ```

- ```boards/post/(?P<pk>[0-9]+)``` : Api call that receives all the information of that specific post
```json

{
    "id": 7,
    "bid": 6,
    "created": "2019-08-26T23:48:22.819355Z",
    "poster": {
        "id": 2,
        "username": "x",
        "profileImg": null,
        "location": "Nowhere",
        "bio": ""
    },
    "message": "Personally, i like Debian",
    "image": null
}
```
