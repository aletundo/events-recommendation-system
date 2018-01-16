# events-recommendation-system

## Synopsis
This main aim of this project is to create a recommendation system for Facebook
events based on user profile preferences.

## How to use

### How to crawl
The crawler relies on [facebook-sdk](https://github.com/mobolic/facebook-sdk)
to get Facebook events given a place. It is implemented with a simple script
located within `fb-events-crawler/src` directory.

#### Preliminary steps
First, you need to install some dependencies:

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
$ cd src/
$ python3 events_crawler_by_place.py

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/aletundo/events-recommendation-system/tags).

## Authors
* **Alessandro Tundo** - [aletundo](https://github.com/aletundo)

See also the list of [contributors](https://github.com/aletundo/events-recommendation-system/contributors) who participated in this project.

## License

This project is licensed under the AGPLv3+. See the [LICENSE.md](LICENSE.md) file for details
