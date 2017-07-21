###Django Caching Middleware

This is a Django middleware that takes a list of URLs from the settings file and caches them by checking a
list `CACHE_URL` in `settings.py`, e.g. `CACHE_URL=[(r'^api/v1/test', 60*60)]`.
The Middleware should checks the requested URL and cache the page for the duration specified in `settings.py` `CACHE_URL` variable. 
If the page was found in the cache, return the cached result and don’t process the page.

In this repo code to achieve the explanation above has been written, that's my best implementation of such, 
if you have a better approach please make a PR.

#####Tech Stack
* Redis for caching
* Django as my server
* Python 2.7 as my runtime

#####How to run the project
* `brew install redis` if on a mac or `sudo apt-get install redis` on ubuntu.
* `redis-server` on your terminal.
* create a virtual environment and activate it.
* `pip install -r requirements.txt`
* `python manage.py runserver`
* then visit `/`, `/test1/`, `/test2/` to see the action.

To find the middleware code `cd pawame/core/` then open `middleware.py`.

May the python be with you.


