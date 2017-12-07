# events-recommendation-system

## Synopsis
This main aim of this project is to create a recommendation system for Facebook
events based on user profile preferences.

## How to use

### How to crawl
The `events-crawler.py` script is located within `fb-events-crawler/src` directory.
It relies on [python-facebook-bot](https://github.com/tudoanh/python-facebook-bot)
to get Facebook events given a location.

First, you need to create a Facebook App for Developer.
Then, run `export` command for CLIENT_ID and CLIENT_SECRET.

Example:  
```
 $ export CLIENT_ID="Your facebook app's ID"
 $ export CLIENT_SECRET="Your facebook app's secret key"
```

After that, just run something like:
```
$ python3 events_crawler.py -lat 45.464211 -lng 9.191383
```
Events will be stored as JSON files within `fb-events-crawler/data` directory.
Each file will contain <= 50 events.

Type
```
$ python3 events-crawler.py --help
```
to get more information about other available script parameters.


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/aletundo/events-recommendation-system/tags).

## Authors
* **Alessandro Tundo** - [aletundo](https://github.com/aletundo)

See also the list of [contributors](https://github.com/aletundo/events-recommendation-system/contributors) who participated in this project.

## License

This project is licensed under the AGPLv3+. See the [LICENSE.md](LICENSE.md) file for details
