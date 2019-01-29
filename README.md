# WordPlease

Django / REST Framework API Exercise



---

## Installation

You need [Python 3](https://www.python.org) to be installed on your computer.
Once you have Python installed in your computer, open a terminal and execute the
following commands:

###### 1) Clone repository
```shell
https://github.com/noemenend/WordPlease.git
cd WordPlease
```
###### 2) Setup and activate the python virtual env

```shell
virtualenv env -p python3
source env/bin/activate
```

###### 3) Install the modules required:

```shell
pip install -r requirements.txt
```

###### 4) Create the Database:

```shell
python manage.py migrate
```

###### 5) Create a superuser:
```shell
python manage.py createsuperuser
```

### Execute development server

```shell
python manage.py runserver
```

---

## Web site

http://127.0.0.1:8000 or http://localhost:8000

URLS:

| URL | Description | Notes |
| ------- | --- | --- |
| ```/``` | Home page. List of latest posts, paginated | Shows only published posts (pub date <= current date), ordered by pub date descending |
| ```/login``` | Login | |
| ```/signup``` | Register a new user | |
| ```/logout``` | Logout | |
| ```/users``` | List of Users, paginated | |
| ```/users/<username>``` | List of blogs belonging to the user, paginated | |
| ```/blogs``` | List of all blogs, paginated | |
| ```/blogs/<blog_name>``` | List of posts in that blog, order by pub date descending | Shows all posts if logged user is the blog author or a super user, otherwise only published posts. The page includes a filter by category |
| ```/blogs/<blog_name>/<post_id>``` | Shows post detail | |

---

## API REST

### Users

| URL | Operation | Description |
| --- | --- | --- |
| ```/api/1.0/users/``` | GET | List of users. Allowed only to superusers |
| ```/api/1.0/users/``` | POST | Register a new user |
| ```/api/1.0/users/<id>/``` | GET | Obtain user detail. Authentication required. Only allowed if authenticated user is a superuser or is the same that we are trying to obtain. |
| ```/api/1.0/users/<id>/``` | PUT | Update user data. Authentication required. Only allowed if authenticated user is a superuser or is the same that we are trying to modify. |
| ```/api/1.0/users/<id>/``` | DELETE | Delete a user. Authentication required. Only allowed if authenticated user is a superuser or is the same that we are trying to delete. |

#### Categories

| URL | Operation | Description | 
| --- | --- | --- |
| ```/api/1.0/categories/``` | GET | List of categories. |
| ```/api/1.0/categories/``` | POST | Add a new category. Only allowed to superusers. |
| ```/api/1.0/categories/<id>/``` | GET | Obtain category detail.|
| ```/api/1.0/categories/<id>/``` | PUT | Update category. Only allowed to superusers. |
| ```/api/1.0/categories/<id>/``` | DELETE | Delete a category. Only allowed to superusers. |

###### Examples:

GET http://127.0.0.1:8000/api/1.0/categories/

```json
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Science"
        },
        {
            "id": 2,
            "name": "Art"
        },
        {
            "id": 3,
            "name": "Computers"
        },
        {
            "id": 4,
            "name": "Work"
        },
        {
            "id": 5,
            "name": "Music"
        }
    ]
}
```

GET http://127.0.0.1:8000/api/1.0/categories/1/

```json
{
    "id": 1,
    "name": "Science",
    "description": "Science",
    "creation_date": "2018-11-17T20:07:13.117927Z",
    "last_modification": "2018-11-25T18:12:58.780230Z"
}
```

### Blogs

| URL | Operation | Description | Search fields | Ordering fields |
| --- | --- | --- | --- | --- |
| ```/api/1.0/blogs/``` | GET | List of blogs, paginated, with post count of every one included. | author's username | name |
| ```/api/1.0/blogs/``` | POST | Add a new blog. Authentication required. Blog author will be the authenticated user. |
| ```/api/1.0/blogs/<id>/``` | GET | Obtain blog detail. |
| ```/api/1.0/blogs/<id>/``` | PUT | Update a blog. Authentication required. Only allowed if authenticated user is the blog author or a superuser. |
| ```/api/1.0/blogs/<id>/``` | DELETE | Delete a blog. Authentication required. Only allowed if authenticated user is the blog author or a superuser. |

###### Examples

GET http://localhost:8000/api/1.0/blogs/?ordering=-name

```json
{
    "count": 2,
    "next": "http://localhost:8000/api/1.0/blogs/?page=2",
    "previous": null,
    "results": [
        {
            "id": 9,
            "url": "http://localhost:8000/api/1.0/blogs/1/",
            "name": "Un blog sobre música",
            "author": {
                "id": 2,
                "username": "miguel"
            },
            "post_count": 5
        },
        {
            "id": 2,
            "url": "http://localhost:8000/api/1.0/blogs/2/",
            "name": "El Blog de Manolo",
            "author": {
                "id": 3,
                "username": "manolo"
            },
            "post_count": 15
        }
    ]
}
```
GET http://localhost:8000/api/1.0/blogs/1/

```json
{
    "id": 1,
    "name": "Un blog sobre música",
    "description": "Últimas noticias, piniones y comentarios sobre música",
    "author": {
        "id": 2,
        "username": "miguel"
    }
}
```

### Posts

| URL | Operation | Description | Search fields | Ordering fields | Filter fields |
| --- | --- | --- | --- | --- | --- |
| ```/api/1.0/posts/``` | GET | List of all posts, paginated. Only published posts will be returned | title, summary, body | pub_date, title | categories |
| ```/api/1.0/blogs/<blog_id>/posts/``` | GET | Post list of the specified blog, paginated. If user is authenticated and is the blog owner or superuser, all posts will be returned. Otherwise, only published posts | title, summary, body | pud_date, title | categories
| ```/api/1.0/blogs/<blog_id>/posts/``` | POST | Add a new post in the specified blog. Authentication required. Only allowed if authenticated user is the blog author or a superuser |
| ```/api/1.0/blogs/<blog_id>/posts/<post_id>/``` | GET | Obtain post detail. If the post is not published, it only will be returned if authenticated user is the author of the post or a superuser |
| ```/api/1.0/blogs/<blog_id>/posts/<post_id>/``` | PUT | Update a post. Authentication required. Only allowed if authenticated user is the post author or a superuser. |
| ```/api/1.0/blogs/<blod_id>/posts/<post_id>/``` | DELETE | Delete a post. Authentication required. Only allowed if authenticated user is the post author or a superuser. |

###### Examples

GET http://localhost:8000/api/1.0/blogs/1/posts/?category=1&ordering=-pub_date

```json
{
    "count": 3,
    "next": "http://localhost:8000/api/1.0/blogs/18/posts/?category=1&ordering=-pub_date&page=2",
    "previous": null,
    "results": [
        {
            "id": 3,
            "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "http://localhost:8000/uploads/women_redhead_3CieMmS.jpg",
            "summary": "Nullam porta nunc vel pulvinar malesuada. Maecenas ultricies, neque quis auctor tincidunt, quam turpis lobortis orci, a cursus dolor augue a lacus. Ut tincidunt nisl et massa iaculis imperdiet. Integer rhoncus porttitor lorem, sit amet viverra ante ullamcorper sed",
            "pub_date": "2018-11-25T13:45:00Z",
            "author": "Miguel Otero",
            "blog_name": "Un blog sobre música"
        },
        {
            "id": 2,
            "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "http://localhost:8000/uploads/women_redhead_3CieMmS.jpg",
            "summary": "Nullam porta nunc vel pulvinar malesuada. Maecenas ultricies, neque quis auctor tincidunt, quam turpis lobortis orci, a cursus dolor augue a lacus. Ut tincidunt nisl et massa iaculis imperdiet. Integer rhoncus porttitor lorem, sit amet viverra ante ullamcorper sed",
            "pub_date": "2018-11-25T11:23:00Z",
            "author": "Miguel Otero",
            "blog_name": "Un blog sobre música"
        },
        {
            "id": 5,
            "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "http://localhost:8000/uploads/women_redhead_3CieMmS.jpg",
            "summary": "Nullam porta nunc vel pulvinar malesuada. Maecenas ultricies, neque quis auctor tincidunt, quam turpis lobortis orci, a cursus dolor augue a lacus. Ut tincidunt nisl et massa iaculis imperdiet. Integer rhoncus porttitor lorem, sit amet viverra ante ullamcorper sed",
            "pub_date": "2018-11-25T08:17:00Z",
            "author": "Miguel Otero",
            "blog_name": "Un blog sobre música"
        }
    ]
}
```

GET http://localhost:8000/api/1.0/blogs/1/posts/3/

```json
{
    "id": 3,
    "author": "Miguel Otero",
    "blog": {
        "id": 1,
        "name": "Un blog sobre músicaL"
    },
    "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "summary": "Nullam porta nunc vel pulvinar malesuada. Maecenas ultricies, neque quis auctor tincidunt, quam turpis lobortis orci, a cursus dolor augue a lacus. Ut tincidunt nisl et massa iaculis imperdiet. Integer rhoncus porttitor lorem, sit amet viverra ante ullamcorper sed",
    "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam porta nunc vel pulvinar malesuada. Maecenas ultricies, neque quis auctor tincidunt, quam turpis lobortis orci, a cursus dolor augue a lacus. Ut tincidunt nisl et massa iaculis imperdiet. Integer rhoncus porttitor lorem, sit amet viverra ante ullamcorper sed. Vivamus enim elit, imperdiet nec porta vitae, gravida et tellus. In interdum in purus ut cursus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur dignissim non nibh ut tincidunt. Duis nec massa vitae magna rutrum pulvinar in in massa. Vivamus sit amet ex lobortis, consequat enim id, pharetra leo. Proin vel fringilla libero, vel commodo ligula. Quisque quis tortor nec diam ornare placerat. Quisque nibh quam, eleifend et convallis vel, bibendum vitae est. Donec vestibulum urna vitae imperdiet auctor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent eget arcu pharetra, egestas ligula sit amet, viverra tellus. Donec a cursus felis. Morbi fermentum diam enim, quis placerat sem blandit vitae.",
    "image": "http://localhost:8000/uploads/imagen_sobre_musica.jpg",
    "video": "https://youtu.be/gmHrHQEmp2Q",
    "creation_date": "2018-11-25T14:45:00Z",
    "pub_date": "2018-11-25T13:45:00Z",
    "last_modification": "2018-11-25T14:45:00Z",
    "categories": [
        {
            "id": 2,
            "name": "Art"
        },
        {
            "id": 5,
            "name": "Music"
        }
    ]
}
```

### Images

| URL | Operation | Description | 
| --- | --- | --- |
| ```/api/1.0/image_upload/``` | GET | List of uploaded images. |
| ```/api/1.0/image_upload/``` | POST | Upload a new image. Authentication required. The image owner will be the authenticated user. |
| ```/api/1.0/image_upload/<id>/``` | GET | Obtain image detail. |
| ```/api/1.0/image_upload/<id>/``` | PUT | Update an image. Authentication required. Only allowed if authenticated user if the image owner or a superuser. |
| ```/api/1.0/image_upload/<id>/``` | DELETE | Delete an image. Authentication required. Only allowed if authenticated user if the image owner or a superuser. |

---

## Models

#### Category

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

#### Blog

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

#### Post

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    body = models.TextField()
    image = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    creation_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField()
    last_modification = models.DateTimeField(auto_now=True)

#### Image

    image = models.ImageField(upload_to='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)