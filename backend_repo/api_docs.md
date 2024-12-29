## API Documentation

### Endpoint: `/api/posts/`
- **Method**: `GET`
- **Description**: Retrieves a list of posts with up to 3 comments per post.

#### Sample Response:
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "text": "This is the first post",
            "timestamp": "2024-12-28T16:51:03.389186Z",
            "author": "testuser",
            "comment_count": 4,
            "comments": [
                {
                    "text": "Comment 1",
                    "timestamp": "2024-12-28T16:51:03.427497Z",
                    "author": "testuser"
                },
                ...
            ]
        }
    ]
}
