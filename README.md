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

| URL | Description | More Information |
| --- | --- | --- |
| ```/``` | Home page. List of latest posts, paginated (6 items per page) | Shows only  recent published posts (pub date <= current date), ordered by last modification date descending. The page include a filter by category |
| ```/login``` | Login | |
| ```/signup``` | Register a new user | |
| ```/logout``` | Logout | |
| ```/users``` | List of Users, paginated (15 items per page) | |
| ```/users/<username>``` | List of blogs belonging to the user selected, paginated  (15 items per page) | |
| ```/blogs``` | List of all blogs, paginated (15 items per page)  | |
| ```/blogs/<blog_name>``` | List of posts in the blog selected, order by last modification date descending | Shows all posts (published/not published) if logged user is the blog author or a super user, otherwise only published posts. The page includes a filter by category |
| ```/blogs/<blog_name>/<post_id>``` | Shows post detail | |
| ```/postsbyCat/<category_id>``` | Shows all posts ordered by last modification date descending that belongs to this category |  |

---

## API REST

### Users

| URL | Operation | Description |
| --- | --- | --- |
| ```/api/1.0/users/``` | GET | List of users. Allowed only to superusers |
| ```/api/1.0/users/``` | POST | Register a new user. Register a new user with the following data: name, surnames, username, email and password  |
| ```/api/1.0/users/<id>/``` | GET | Obtain user detail. Authentication required. Only allowed if authenticated user is a superuser or is the same that we are trying to obtain. |
| ```/api/1.0/users/<id>/``` | PUT | Update user detail. Authentication required. Only allowed if authenticated user is a superuser or is the same that we are trying to modify. |
| ```/api/1.0/users/<id>/``` | DELETE | Delete a user. Authentication required. Only allowed if authenticated user is a superuser or is the same that we are trying to delete. |

#### Categories

| URL | Operation | Description | 
| --- | --- | --- |
| ```/api/1.0/categories/``` | GET | List of categories. |
| ```/api/1.0/categories/``` | POST | Add a new category. Only allowed to superusers. |
| ```/api/1.0/categories/<id>/``` | GET | Obtain category data.|
| ```/api/1.0/categories/<id>/``` | PUT | Update category given. Only allowed to superusers. |
| ```/api/1.0/categories/<id>/``` | DELETE | Delete the category given. Only allowed to superusers. |

###### Examples:

GET http://localhost:8000/api/1.0/categories/

```html
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

```json
[
    {
        "id": 3,
        "name": "Social Media"
    },
    {
        "id": 4,
        "name": "Diseño Web"
    },
    {
        "id": 5,
        "name": "UX"
    },
    {
        "id": 6,
        "name": "Analítica"
    },
    {
        "id": 7,
        "name": "Inbound Marketing"
    }
]
```

GET http://localhost:8000/api/1.0/categories/3/

```html
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

```json
{
    "id": 3,
    "name": "Social Media",
    "description": "Social Media",
    "creation_date": "2019-01-20T20:07:47.280137Z",
    "last_modification": "2019-01-20T20:07:47.280137Z"
}
```

### Blogs

| URL | Operation | Description | Search fields | Ordering fields |
| --- | --- | --- | --- | --- |
| ```/api/1.0/blogs/``` | GET | List of blogs, paginated, with post count of every blog included. | author's username | name |
| ```/api/1.0/blogs/``` | POST | Add a new blog. Authentication required. Blog author will be the authenticated user. |
| ```/api/1.0/blogs/<id>/``` | GET | Obtain the detail of the blog given. |
| ```/api/1.0/blogs/<id>/``` | PUT | Update the blog given by parameter. Authentication required. Only allowed if authenticated user is the blog author or a superuser. |
| ```/api/1.0/blogs/<id>/``` | DELETE | Delete the blog given by paremeter. Authentication required. Only allowed if authenticated user is the blog author or a superuser. |

###### Examples

GET http://localhost:8000/api/1.0/blogs/?ordering=name

```html
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

```json
[
    {
        "id": 4,
        "url": "http://localhost:8000/api/1.0/blogs/4/",
        "name": "Blog Instagraming",
        "author": {
            "id": 2,
            "username": "chewbacca"
        },
        "post_count": 2
    },
    {
        "id": 3,
        "url": "http://localhost:8000/api/1.0/blogs/3/",
        "name": "Blog New Technologies",
        "author": {
            "id": 1,
            "username": "admin"
        },
        "post_count": 3
    }
]
```
GET http://localhost:8000/api/1.0/blogs/3/

```html
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

```json
{
    "id": 3,
    "name": "Blog New Technologies",
    "description": "Blog about several themes related with new thecnological topics",
    "author": {
        "id": 1,
        "username": "admin"
    }
}
```

### Posts

| URL | Operation | Description | Search fields | Ordering fields | Filter fields |
| --- | --- | --- | --- | --- | --- |
| ```/api/1.0/posts/``` | GET | List of all posts, paginated. Only published posts will be returned | title, resume, body | pub_date | categories |
| ```/api/1.0/blogs/<blog_id>/posts/``` | GET | Post list of the specified blog passed by parameter, paginated. If user is authenticated and is the blog owner or superuser, all posts will be returned. Otherwise, only published posts | title, resume, body | pub_date | categories
| ```/api/1.0/blogs/<blog_id>/posts/``` | POST | Add a new post in the specified blog passed by parameter. Authentication required. Only allowed if authenticated user is the blog author or a superuser |
| ```/api/1.0/blogs/<blog_id>/posts/<post_id>/``` | GET | Obtain the detail of the post given. If the post is not published, it only will be returned if authenticated user is the author of the post or a superuser |
| ```/api/1.0/blogs/<blog_id>/posts/<post_id>/``` | PUT | Update the post given. Authentication required. Only allowed if authenticated user is the post author or a superuser. |
| ```/api/1.0/blogs/<blod_id>/posts/<post_id>/``` | DELETE | Delete the post given. Authentication required. Only allowed if authenticated user is the post author or a superuser. |

###### Examples

GET http://localhost:8000/api/1.0/blogs/3/posts/?category=1&ordering=-pub_date

```html
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

```json
[
    {
        "id": 8,
        "title": "Tendencias en diseño web 2019: lo que viene para quedarse",
        "image": "http://localhost:8000/mediauploads/tendencias-design-1200x600.png",
        "resume": "¿Qué tendencias en diseño web lo van a petar este próximo año? Hacemos un rápido repaso de las más importantes para estar al día.",
        "pub_date": "2019-01-20T00:00:00Z",
        "author": "Noelia Muñiz Menendez",
        "blog_name": "Blog New Technologies"
    },
    {
        "id": 9,
        "title": "Lenguaje inclusivo en redes sociales (de marcas)",
        "image": "http://localhost:8000/mediauploads/lenguaje-inclusivo-marcas-1200x554.png",
        "resume": "El lenguaje inclusivo es un recurso bastante sencillo que consiste en sustituir o transformar las palabras sensibles de excluir a las mujeres, en otras que las incluyen",
        "pub_date": "2019-01-20T00:00:00Z",
        "author": "Noelia Muñiz Menendez",
        "blog_name": "Blog New Technologies"
    },
    {
        "id": 10,
        "title": "Cómo y por qué despedirte de un suscriptor que se da de baja",
        "image": "http://localhost:8000/mediauploads/engagement-1200x480.png",
        "resume": "¿Qué tendrán las despedidas que tanto nos cuestan? Y más si nos toca decir adiós a uno de esos suscriptores que tantísimo nos ha costado conseguir.",
        "pub_date": "2019-01-20T00:00:00Z",
        "author": "Noelia Muñiz Menendez",
        "blog_name": "Blog New Technologies"
    }
]
```

GET http://localhost:8000/api/1.0/blogs/3/posts/9/

```html
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

```json
{
    "id": 9,
    "author": "Noelia Muñiz Menendez",
    "blog_name": "Blog New Technologies",
    "blog": {
        "id": 3,
        "name": "Blog New Technologies"
    },
    "title": "Lenguaje inclusivo en redes sociales (de marcas)",
    "resume": "El lenguaje inclusivo es un recurso bastante sencillo que consiste en sustituir o transformar las palabras sensibles de excluir a las mujeres, en otras que las incluyen",
    "body": "La ortografía y las redes sociales nunca han sido lo que se dice mejores amigas. En los últimos años muchas personas se han unido a la guerrilla ortográfica de internet, señalando cada b o v mal puesta en Twitter; pero la mayoría sigue haciendo más o menos lo que le da la gana. Y muy bien que hacen.\r\nPor eso, si alguien ha dejado internet durante los últimos dos años (no le culpamos), probablemente no le sorprenda a su vuelta que haya un montón de gente joven escribiendo ‘chic@s’, ‘amigues’ o ‘trabajadorxs’. Será una de esas modas ortográficas, como las maYúsCuLaS iNteRcalADas, ¿no? Pero en el momento en que vea que personas ya con canas e incluso empresas reconocidas están hablando así de raro, comenzará a pensar que aquí está pasando algo.",
    "image": "http://localhost:8000/mediauploads/lenguaje-inclusivo-marcas-1200x554.png",
    "creation_date": "2019-01-20T20:23:54.241112Z",
    "pub_date": "2019-01-20T00:00:00Z",
    "last_modification": "2019-01-20T20:23:54.241112Z",
    "status": "PUB",
    "categories": [
        {
            "id": 5,
            "name": "UX"
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

###### Examples

GET http://localhost:8000/api/1.0/image_upload/

```html
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

```json
[
    {
        "id": 1,
        "image": "http://localhost:8000/mediauploads/co_segamdII_u43_1.jpg",
        "author": 1
    }
]
```



---

## Models

#### Category

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

#### Blog

    name = models.CharField(max_length=50)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#### Post

    PUBLISHED = 'PUB'
    NO_PUBLISHED = 'NPUB'

    STATUS = (
        (PUBLISHED, 'Published'),
        (NO_PUBLISHED, 'No Published')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    resume = models.TextField()
    body = models.TextField()
    image = models.FileField()
    creation_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField()
    last_modification = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=4, choices=STATUS)

#### Image

    image = models.ImageField(upload_to='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
