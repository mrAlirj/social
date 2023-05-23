# Social Network Project

This project is a social network developed using the Django framework. It provides various features for users to interact with each other, including adding posts, commenting on posts, replying to comments, and liking posts.

## Project Structure

The project follows the standard Django structure with the following notable components:

- `social/`: The main Django project directory.
- `posts/`: An app responsible for managing posts.
- `comments/`: An app responsible for managing comments.
- `likes/`: An app responsible for managing post likes.
- `users/`: An app responsible for user management.

## Functionality

The social network includes the following key functionalities:

- Adding a post: Users can create new posts by providing a text description.
- Adding a comment: Users can comment on posts by providing a text comment.
- Replying to a comment: Users can reply to existing comments.
- Liking a post: Users can like posts to show their appreciation.
- Displaying user posts: Users can view a list of their own posts.
- Showing liked users: Users can view a list of users who liked a specific post.
- Displaying post comments: Users can view the comments on a specific post.

## Installation and Setup

To set up the project locally, follow these steps:

1. Clone the repository:
`git clone https://github.com/mrAlirj/social.git`

2. Create a virtual environment and activate it:

```
python -m venv env
source env/bin/activate
````
3. Install the project dependencies: `pip install -r requirements.txt`

4. Apply the database migrations:

`python manage.py migrate`

5. Run the development server:

`python manage.py runserver`

6. Access the application in your web browser at `http://localhost:8000`.

## API Endpoints

The project provides the following API endpoints:

- `POST /api/posts/`: Create a new post.
- `GET /api/posts/{post_id}/`: Retrieve a specific post.
- `GET /api/posts/{post_id}/comments/`: Retrieve comments for a specific post.
- `POST /api/posts/{post_id}/comments/`: Create a comment for a specific post.
- `GET /api/posts/{post_id}/likes/`: Retrieve users who liked a specific post.
- `POST /api/posts/{post_id}/like/`: Like a specific post.
- `DELETE /api/posts/{post_id}/unlike/`: Unlike a specific post.

Refer to the project's API documentation or code for more details on the available endpoints and request/response formats.
- `api/schema/`
- `api/docs/`
- `api/redoc/`

## Testing

The project includes test cases to ensure the correctness of its functionalities. To run the tests, use the following command:

`python manage.py test`


The tests cover various scenarios, including creating posts, adding comments, liking/unliking posts, and retrieving data. Additional tests can be added as needed.

## Contributing

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
