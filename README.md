# Notine

Notine is a note-taking application built with DRF.

## Features

- CRUD operations for managing notes.
- Token-based authentication for secure access.
- Customizable permissions for different user roles.

## Technologies Used

- Django
- Django REST Framework
- Postgres (or your preferred database)
- Other dependencies specified in `requirements.txt`

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended):

    ```
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```
    source venv/bin/activate
    ```

5. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```
    python manage.py migrate
    ```

7. Create a superuser (for admin access):

    ```
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```
    python manage.py runserver
    ```

9. Access the API at `http://localhost:8000/`.

## API Endpoints

- `/notes/`: List and create notes.
- `/notes/<id>/`: Retrieve, update, or delete a specific note.
- `/auth/`: Authentication endpoints for Djoser.
- `/admin/`: Django admin panel.
- `/swagger/`: Swagger documentation.
- `/redoc/`: ReDoc documentation.
- `/__debug__/`: Django Debug Toolbar (in development mode).
- `/category/`: Endpoints for managing categories.
- `/note/colors/`: Endpoint for listing available note colors.

## Authentication

- Token-based authentication is used for accessing protected endpoints.
- Obtain a token by sending a POST request to `/auth/jwt/create/` with valid credentials.

## Usage

- Use tools like Postman or curl to interact with the API endpoints.
- Authenticate using the obtained token for accessing protected endpoints.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/my-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, feel free to contact me at [nimiologyy@gmail.com](mailto:nimiologyy@gmail.com).
