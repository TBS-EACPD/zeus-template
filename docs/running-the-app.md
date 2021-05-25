# Running the app

### `./manage.py runserver`

The standard djanngo way to run your app. It will watch files for changes, including yaml files, and reload the app. 


### `./manage.py rs`  ?

This is an alternative runserver command that refreshes the app much faster. On the other hand, it skips [migration and system checks](https://docs.djangoproject.com/en/3.0/topics/checks/). If you're using `rs` over `runserver` and run into bugs, try reverting to `runserver` in case system checks can help you out. They're there for a reason! 



### Running without `runserver` for production parity

in production, we don't use `runserver`, instead we use `gunicorn`. You can use gunicorn directly by running `gunicorn -t 1200 -b :8000 results.wsgi`. 

If the app is ugly because CSS doesn't load, don't worry about it. 

_**Why would you ever need to test this?**_ 

Sometimes `runserver` is more lenient than the gunicorn layer with certain things. One time, we got a bug because a PDF file had accents in the response file-name. These bugs could not be reproduced using `runserver`, but only showed up using gunicorn. 


### Killing the app

sometimes it freezes and does not respond to ctrl-C, use `pkill -f "manage.py runserver"` to kill the app.


## Debugging

You can place `import IPython; IPython.embed()` anywhere in the app and get placed in an interactive REPL.


Note that the `./manage.py shell` also uses IPython. If you'd like to debug without running the entire app, one useful trick is to paste 

```
%load_ext autoreload
%autoreload 2
```

into a `./manage.py shell` session. This will automatically reload imports anytime you run a new command. This can make developing non-views (e.g. working with models) easier.