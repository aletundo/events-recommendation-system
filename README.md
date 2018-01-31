# events-recommendation-system

## Synopsis
This main aim of this project is to create a recommendation system for Facebook
events based on user profile preferences.

## How to use
Minimum requirements:
 * Docker Engine 17.09.0+
 * Docker Compose

__N.B.:__ Every command below assumes you are located into the root directory of the project.
### How to crawl
The crawler relies on [facebook-sdk](https://github.com/mobolic/facebook-sdk) to get Facebook events given a place.
It is implemented with a simple script located within `fb-events-crawler/src` directory.

#### Preliminary steps

First, you need to build the crawler Docker image:
```
$ cd fb-events-crawler/
$ docker build -t fb-events-crawler:0.1.0 .
```

Second, you need to create a Facebook App for Developer in order to get your CLIENT_ID and CLIENT_SECRET which made your API token.

#### Run the crawler
Running the crawler is very simple, you need to run the following commands substituting CLIENT_ID and CLIENT_SECRET values accordingly:
```
$ cd fb-events-crawler/
$ docker run --rm -it -v $(pwd):/srv/fb-events-crawler -u $(id -u):$(id -g) -e CLIENT_ID="Your client id" -e CLIENT_SECRET="Your client secret" fb-events-crawler:0.1.0
```
Two JSON files will be created within `fb-events-crawler/data` directory.
Copy the `data` directory into `recommendation-system-engine`:
```
$ cp -r fb-events-crawler/data recommendation-system-engine
```

### How to run the engine and the application

#### Preliminary steps
You need to install some PHP dependencies for the application:

```
$ cd recommendation-system-app/
$ docker run --rm -v $(pwd):/app -u $(id -u):$(id -g) composer/composer install
```

#### Run the system with Docker Compose
```
$ docker-compose up --build
```
Now you can type `localhost:8080` in your browser and use the application.
The engine initializes the databases and simulates the users going to event action before to serve the first request.
Therefore, the application may require some time to show up the first time.

The engine API is available at `localhost:5000` for debug purposes.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/aletundo/events-recommendation-system/tags).

## Authors
* **Alessandro Tundo** - [aletundo](https://github.com/aletundo)
* **Matteo Vaghi** - [oet93](https://github.com/oet93)

See also the list of [contributors](https://github.com/aletundo/events-recommendation-system/contributors) who participated in this project.

## License

This project is licensed under the AGPLv3+. See the [LICENSE.md](LICENSE.md) file for details
