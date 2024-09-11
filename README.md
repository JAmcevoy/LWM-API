# Learn With Me API Documentation

## Welcome to the Learn With Me API
This API allows users to interact with a platform where they can manage profiles, posts, likes, followers, and more.

### API URL
- Access The Live App: [Learn With Me](https://learn-with-me-593ba116ca81.herokuapp.com)
- The Full Design ReadMe [Learn With Me: Readme ](https://github.com/JAmcevoy/learnwithme?tab=readme-ov-file#learn-with-me)

## Overview
The Learn With Me API provides endpoints to manage various aspects of a user’s experience on the platform. This includes handling profiles, posts, likes, followers, and user authentication.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 3.x or higher
- Django REST Framework
- Django Filter
- dj-rest-auth

### Setup

1. Clone the repository:

    ```bash
    ~~git clone https://github.com/yourusername/yourrepository.git~~
    cd yourrepository
    ```

2. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

---

## API Endpoints

### Authentication
- **Login**: `/dj-rest-auth/login/`
- **Logout**: `/logout/`
- **Current User**: `/dj-rest-auth/user/`

### Profiles

#### List Profiles

- **Endpoint**: `/profiles/`
- **Method**: `GET`
- **Description**: Retrieve a list of all profiles with options for filtering and ordering.

**Filters**:
- `owner__following__followed__profile`: Filter profiles based on who the owner is following.
- `owner__followed__owner__profile`: Filter profiles based on who follows the owner.

**Ordering**:
- `posts_count`: Order profiles by the number of posts.
- `followers_count`: Order profiles by the number of followers.
- `following_count`: Order profiles by the number of profiles the owner is following.
- `owner__following__created_at`: Order profiles by the creation date of following relationships.
- `owner__followed__created_at`: Order profiles by the creation date of follower relationships.

#### Profile Detail

- **Endpoint**: `/profiles/{id}/`
- **Method**: `GET`, `PUT/PATCH`, `DELETE`
- **Description**: Retrieve or update a specific profile. Only the profile owner can update or delete the profile.

---

### Posts

#### List Posts

- **Endpoint**: `/posts/`
- **Method**: `GET`, `POST`
- **Description**: Retrieve a list of posts or create a new post.

**Filters**:
- `owner__followed__owner__profile`: Filter posts based on who follows the owner.
- `likes__owner__profile`: Filter posts based on who liked the post.
- `owner__profile`: Filter posts based on the owner's profile.

**Ordering**:
- `likes_count`: Order posts by the number of likes.
- `likes__created_at`: Order posts by the creation date of likes.

#### Post Detail

- **Endpoint**: `/posts/{id}/`
- **Method**: `GET`, `PUT/PATCH`, `DELETE`
- **Description**: Retrieve, update, or delete a specific post.

---

### Likes

#### List Likes

- **Endpoint**: `/likes/`
- **Method**: `GET`, `POST`
- **Description**: Retrieve a list of likes or create a new like.

#### Like Detail

- **Endpoint**: `/likes/{id}/`
- **Method**: `GET`, `DELETE`
- **Description**: Retrieve or delete a specific like.

---

### Followers

#### List Followers

- **Endpoint**: `/followers/`
- **Method**: `GET`, `POST`
- **Description**: Retrieve a list of followers or create a new follower relationship.

#### Follower Detail

- **Endpoint**: `/followers/{id}/`
- **Method**: `GET`, `DELETE`
- **Description**: Retrieve or delete a specific follower relationship.

---

## Models and Serializers

- **Profile**: Represents a user profile with fields for username, interests, and counts for posts, followers, and following.
- **Post**: Represents a post created by a user, including fields for title, content, media, and counts for likes.
- **Like**: Represents a like on a post, associated with a user and a post.
- **Follower**: Represents a follower relationship between users.

---

## Permissions

- **IsOwnerOrReadOnly**: Custom permission to ensure that only the owner of an object can edit or delete it, while others can only view it.

---
