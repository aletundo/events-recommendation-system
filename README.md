# events-recommendation-system

## Synopsis
This main aim of this project is to create a recommendation system for Facebook
events based on user profile preferences.

## How to use
Minimum requirements:
 * python 3.5+
 * pip for python3
 * Docker Engine 17.09.0+
 * Docker Compose

__N.B.:__ Every command below assumes you are located into the root directory of the project.
### How to crawl
The crawler relies on [facebook-sdk](https://github.com/mobolic/facebook-sdk) to get Facebook events given a place.
It is implemented with a simple script located within `fb-events-crawler/src` directory.

#### Preliminary steps

First, you need to install some dependencies with [pip](https://pypi.python.org/pypi/pip):
```
$ cd fb-events-crawler/
$ pip3 install -r requirements.txt
```

Since facebook-sdk last release available is too old you need to install it manually
how explained here: https://facebook-sdk.readthedocs.io/en/latest/install.html#installing-from-git

Second, you need to create a Facebook App for Developer.
Then, run `export` command for CLIENT_ID and CLIENT_SECRET.

Example:  
```
 $ export CLIENT_ID="Your facebook app's ID"
 $ export CLIENT_SECRET="Your facebook app's secret key"
```
#### Run the crawler
Running the crawler is very simple, you need to run the following command:
```
$ cd fb-events-crawler/src/
$ python3 events_crawler_by_place.py
```

### How to run the engine and the application

#### Preliminary steps
You need to install some PHP dependencies for the application:

```
$ cd recommendation-system-app/
$ docker run --rm -v $(pwd):/app composer/composer install
```

#### Run the system with Docker Compose
```
$ docker-compose up --build
```
Now you can type `localhost:8080` in your browser and use the application.
The engine API is available at `localhost:5000`.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/aletundo/events-recommendation-system/tags).

## Authors
* **Alessandro Tundo** - [aletundo](https://github.com/aletundo)
* **Matteo Vaghi** - [oet93](https://github.com/oet93)

See also the list of [contributors](https://github.com/aletundo/events-recommendation-system/contributors) who participated in this project.

## License

This project is licensed under the AGPLv3+. See the [LICENSE.md](LICENSE.md) file for details
