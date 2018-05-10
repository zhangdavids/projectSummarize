Python Web Applications With Flask - Part III
=========

Welcome back to the Flask-Tracking development series! For those of you who are just joining us, we are implementing a web analytics application that conforms to [this napkin specification][series:faq:what].  For all those of you following along at home, you may check out today's code with:

```sh
$ git checkout part-3
```

or you may download it from the [releases page on Github][repository:releases]. Those of you who are just joining us may wish to read [a note on the repository structure][series:faq:repo] as well.

[In the previous segment][Part II] we made web tracker fully functional. This week we'll work on implementing a testing framework, talk a bit about why testing is important and then write some tests for our application. After we'll talk a bit about debugging errors in our application and logging.

## Why Testing

Before we actually write any of our tests lets talk about why testing is important. If you remember the Zen of Python from [Part 1][Part I], you may have noticed that "Simple is better than complex" is right above "Complex is better than complicated".  Simple is the ideal, complex is often a reality. Web applications, in particular, have many moving parts, and can very quickly move from simple to complex.

As the complexity of our application grows we want to ensure that the various moving parts we create continue to work together in a harmonious fashion.  We don't want to change the signature of a utility function and breaking a seemingly unrelated feature in production. Moreover, we want to ensure that our changes still preserve *correct* (not simply valid) functionality. A method that always returns the same ``datetime`` instance is valid and correct twice a day, but valid and *incorrect* all the rest of the time.

Tests are a great debugging aid. Writing a test that produces the invalid behavior we are seeing helps us look at our code from a different perspective. In addition, once we have the test passing we have ensured that we will not re-introduce this bug again (at least in that particular way).

Tests are also an excellent source of documentation.  Since they have to deal with expected inputs and outputs reading a test suite will clarify what the code under test is expected to do.  This will illuminate unclear segments of the documentation that we have written (or in simple cases, even substitute for it).

Finally, tests can be a wonderful exploratory aid - sketching out how we *want* to interact with our code before we write it reveals simpler APIs, and helps us paper over the internal complexity of a domain.  ["Test Driven Development"][TDD] is the ultimate commitment to this process.  In TDD we first write tests to cover our code's functionality and only then do we write that code.

Tests will make it obvious:

- When code isn't working
- What code is broken
- Why we wrote this code in the first place

Every time we go to add a feature to our application, fix a bug or change some code we should make sure our code is adequately covered by tests and that the tests all pass after we're done.

Do:

- Add tests to cover the basic functionality of your code
- Add tests to cover as many corner cases of your code that you can think of
- Add tests to cover the corner cases you didn't think of after you go back and fix them
- Remind your coding peers to adequately test their code
- Bug people about code that doesn't pass tests

Do Not:

- Commit code without tests
- Commit code that doesn't pass or breaks tests
- Change your tests so your code passes without fixing the problem

Now that we've worked out why testing is so important lets start writing some tests for our application.

## Setting up

Each chunk of functionality needs to have tests. To do this in a neat and concise way each package will get a `tests.py` module in it. This way we know where the tests for each package are and they're contained in the package if we ever need to break it out of our application.

We'll use [`Flask-Testing`][FT] extension because it has a bunch of useful testing features that we'd be setting up anyways. Go ahead and add `Flask-Testing==0.4` to the bottom of `requirements.txt` then run `pip install -r requirements.txt`.

Flask-Testing eliminates almost all of the boilerplate of setting up Flask for unit testing.  The little bit that remains we will place in a new module `bases.py`:

    from flask.ext.testing import TestCase
    from app import app, db


    class BaseTestCase(TestCase):
        """A base test case for flask-tracking."""

        def create_app(self):
            app.config.from_object('config.TestConfiguration')
            return app

        def setUp(self):
            db.create_all()

        def tearDown(self):
            db.session.remove()
            db.drop_all()

This test case doesn't do anything spectacular - it just configures the application with our test configuration, creates all of our tables at the start of every test and deletes all of our tables at the end of every test.  This way every test case starts out with a clean slate and we can spend more time writing tests and less time debugging our test cases.  Since every test case will inherit from our new `BaseTestCase` we will avoid copying and pasting this configuration into every package we create for our application.

One additional thing we have done is modularize our configurations.  The original `config.py` module supported only one configuration - we can update that to allow for differences between environments.  As a reminder, this is what `config.py` looked like in [Part 2][Part II]:

    DEBUG = False
    TESTING = False

    ADMINS = frozenset(['youremail@yourdomain.com'])
    SECRET_KEY = 'SecretKeyForSessionSigning'
    # ... etc. ...

It looks almost the same now - we simply created a class that holds all of these configuration values:

    class BaseConfiguration(object):
        DEBUG = False
        TESTING = False

        ADMINS = frozenset(['youremail@yourdomain.com'])
        SECRET_KEY = 'SecretKeyForSessionSigning'
        # ... etc. ...

which we can then inherit from:

    class TestConfiguration(BaseConfiguration):
        TESTING = True

        CSRF_ENABLED = False

        DATABASE = 'tests.db'
        DATABASE_PATH = os.path.join(_basedir, DATABASE)
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # + DATABASE_PATH

This way settings that are common to all enviroments can be easily shared, and we can easily override what we need to in our environment specific configurations.  (This pattern comes directly from [Flask's excellent documentation][config].)

We are using an in-memory SQLite database for our tests to ensure that our tests execute as quickly as possible.  We want to enjoy running our tests, and we can only do that if they execute in a reasonable amount of time.  If we really need access to the result of the test run we can override the `:memory:` setting with the calculated path to `tests.db`. (That's the commented out `+ DATABASE_PATH` in our `TestConfiguration`).

Finally, we will need to update our `app.from_object` call in `app/__init__.py`.  Before, we were loading the config using `app.from_object('config')`.  Now that we have two configurations in our config module we will want to change that to `app.from_object('config.BaseConfiguration')`.

Now we are ready to test our application.

## The Tests

We'll start with the `users` package.

From [last time][Part II] we know that the `users` package is responsible for:

- Registration
- Login
- Logout

So we need to write tests that cover users signing up, users logging in and then users logging out.  Let's start with a simple case - an existing user attempting to log in:

    from flask import url_for

    from app.bases import BaseTestCase
    from app.users.models import User


    class UserViewsTests(BaseTestCase):
        def test_users_can_login(self):
            User.create(name='Joe', email='joe@joes.com', password='12345')

            response = self.client.post('/login/',
                                        data={'name': 'Joe', 'password': '12345'})

            self.assert_redirects(response, url_for('index'))

Since every test case starts out with a completely clean database we have to create an existing user first.  We can then submit the same request that our user (Joe) would submit if he were trying to log in.  We want to ensure that if Joe logs in successfully, he will be redirected back to the home page.

We can run our tests with the [`unittest`][unit] test runner, which comes built-in with Python.  Run the following command from the root of the project:

    $ python -m unittest discover

That results in the following output:

    ----------------------------------------------------------------------
    Ran 1 test in 0.045s

    OK

Hurray, we now have a passing test! Let's also test that our integration with Flask-Login is working. `current_user` should be Joe, so we should be able to do the following:

    from flask.ext.login import current_user

    # And then inside of our test_users_can_login function: 
    self.assertTrue(current_user.name == 'Joe')
    self.assertFalse(current_user.is_anonymous())

However, if we were to try this we would get the following error:

    AttributeError: 'AnonymousUserMixin' object has no attribute 'name'

`current_user` needs to be accessed within the context of a request (it is a thread-local object, just like `flask.request`).  When `self.client.post` completes the request and every thread-local object is torn down.  We need to preserve the request context so we can test our integration with Flask-Login.  Fortunately, `Flask`'s [`test_client`][test client] is a [context manager][test context], which means that we can use it in a `with` statement and it will keep the context around as long as we need it:

    with self.client:
        response = self.client.post('/login/', data={'name': 'Joe', 'password': '12345'})

        self.assert_redirects(response, url_for('index'))
        self.assertTrue(current_user.name == 'Joe')
        self.assertFalse(current_user.is_anonymous())

Now, when we run our test again, we pass!

    ----------------------------------------------------------------------
    Ran 1 test in 0.053s

Let's ensure that when Joe is logged in, he can log out:

    def test_users_can_logout(self):
        User.create(name='Joe', email='joe@joes.com', password='12345')

        with self.client:
            self.client.post('/login/', data={'name': 'Joe', 'password': '12345'})
            self.client.get('/logout/')

            self.assertTrue(current_user.is_anonymous())

Once again, we create Joe (remember, the database is reset at the end of every test).  Then we log him in (which we know works because our first test is passing).  Finally, we log him out by requesting the logout page via `self.client.get('/logout/')` and ensure that the user we have is once again anonymous.  Run the tests again and bask in the satisfaction of having two passing tests.

A couple of other things that we will want to check:

* Can a user register and then log into the application?
* Does an anonymous user who hits the logout view get redirected to the login view?

These tests are available in [the `flask-tracking` repository][repository], should you want to review them.  Since they are similar to what we have already written, we will skip them here.

## Mocks and Integration Tests

There is one part of our application though, which is a little different from the rest - our `register_visit` endpoint in the `tracking` package not only interacts with the database and the user - it also interacts with the third-party service [Free GeoIP][freegeo].  As this is a potential source of breakage, we will want to test it thoroughly.  Since Free GeoIP is a third party service (which we might not always have access to) it also gives us a good opportunity to talk about the difference between unit and integration tests.

### Unit vs. Integration Tests

Everything that we have written so far has fallen under the heading of a unit test. A unit test is a test of the smallest possible piece of functionality of *our* code - a test of an indivisible section of code (generally a function or method).

Integration tests, on the other hand, test our application at its boundaries - does our application interact correctly with this other application (which may well be something we have written)?  Testing that our application properly calls and interacts with Free GeoIP is an integration test.  These sorts of tests are very important, as they let us know that the features that we are depending on still work the way we expect them to. (Yes, that doesn't help us if Free GeoIP changes its contract, or goes down completely while we are running our application in production but that is what logging is for - which we will cover a little later on.)

However, the issue with integration tests is that they are often more than an order of magnitude slower than unit tests.  A large number of integration tests can slow down our test suite to the point where it takes more than a minute to run - once it crosses that boundary, our test suite starts to be a hindrance rather than an assistant.  Taking the time to run our tests now breaks our flow of concentration, rather than simply verifying that we are on the right track.  Also, in the case of distributed services like Free GeoIP, it means we cannot actually run our test suite if we are offline or if Free GeoIP is down.

This leaves us in a fine quandary - on the one hand, integration tests are very important, and on the other hand, running integration tests is likely to break our flow.

The solution is simple - we can create a bare-bones local implementation of the service we are calling (which is called a mock in testing parlance) and run our unit tests using this mock.  We can separate out our integration tests into a separate file and run those before we commit changes to our code.  That way, we get the speed of good unit tests and retain the certainty that integration tests provide.

### Mocking Free GeoIP

If you remember from [Part 2][Part II] we added a `geodata` module to our `tracking` package which implemented a single function `get_geodata`.  We use this function in our `tracking.register_visit` view:

    ip_address = request.remote_addr
    geo = get_geodata(ip_address)

What we want to do in our *unit* test is ensure that when `get_geodata` works as expected we will properly record the visit in the database.  However, we don't want to call Free GeoIP (otherwise, our test will be slow in comparison to our other tests and we will not be able to run the tests when offline.)  We need to replace `get_geodata` with another function (a mock).

First, let's install [a mocking library][mock] to make this easier.  Add [`mock==1.0.1`][mock] to requirements.txt and `pip install -r requirements.txt` again. (If you are using Python 3.3 or greater, you already have mock installed as `unittest.mock`.)

Now we can write our unit test:

    from flask import url_for
    from mock import Mock, patch

    from app.bases import BaseTestCase
    from app.users.models import User
    from app.tracking.models import Site, Visit

    import app.tracking.views


    class TrackingViewsTests(BaseTestCase):
        def test_visitors_location_is_derived_from_ip(self):
            user = User.create(name='Joe', email='joe@joe.com', password='12345')
            site = Site.create(user_id=user.id)

            mock_geodata = Mock(name='get_geodata')
            mock_geodata.return_value = {
                'city': 'Los Angeles',
                'zipcode': '90001',
                'latitude': '34.05',
                'longitude': '-118.25'
            }

            url = url_for('tracking.register_visit', site_id=site.id)
            wsgi_environment = {'REMOTE_ADDR': '1.2.3.4'}

            with patch.object(app.tracking.views, 'get_geodata', mock_geodata):
                with self.client:
                    self.client.get(url, environ_overrides=wsgi_environment)

                    visits = Visit.query.all()

                    mock_geodata.assert_called_once_with('1.2.3.4')
                    self.assertEquals(1, len(visits))
                    self.assertEquals('Los Angeles, 90001', visits[0].location)
                    self.assertEquals('Los Angeles, 90001, 34.05, -118.25',
                                      visits[0].location_full)

Don't worry - the pain of testing these sorts of integrations is mitigated by the fact that you generally have fewer of them in your application than you have units of code.  Let's walk through this code section by section and break it down into digestible chunks.

#### Set up the test data and mocks

First, we set up a user and a site since the database is empty at the start of every test:

    def test_visitors_location_is_derived_from_ip(self):
        user = User.create(name='Joe', email='joe@joe.com', password='12345')
        site = Site.create(user_id=user.id)

Then, we create a mock function, and specify that it should return a dictionary containing the coordinates for Los Angeles every time it is called (we could have simply created a simple function that always returned the dictionary, but mock also provides the [`patch.*`][mock.patch] context managers, which are extremely useful, so we'll go the whole nine yards with the library):

    mock_geodata = Mock(name='get_geodata')
    mock_geodata.return_value = {
        'city': 'Los Angeles',
        'zipcode': '90001',
        'latitude': '34.05',
        'longitude': '-118.25'
    }

Finally, we set up the URL that we are going to visit and the parts of the WSGI environment that we need for `tracking.register_visit` to work (which, in this case is just the IP address of our fake end user's visitor):

    url = url_for('tracking.register_visit', site_id=site.id)
    wsgi_environment = {'REMOTE_ADDR': '1.2.3.4'}

#### Patch the mock into our tracking module

We explicitly imported the `app.tracking.views` module into our `tests` module with:

    import app.tracking.views

Now we patch that module's `get_views` name to point to our `mock_geodata` object rather than the `app.tracking.geodata.get_geodata` function:

    with patch.object(app.tracking.views, 'get_geodata', mock_geodata):

By using `patch.object` as a context manager, we ensure that after we exit this `with` block `app.tracking.views.get_geodata` will once again point to `app.tracking.geodata.get_geodata`.  We could also have used `patch.object` as a decorator:

    mock_geodata = Mock(name='get_geodata')
    # ... snip return setup ...

    class TrackingViewsTests(BaseTestCase):
        @patch.object(app.tracking.views, 'get_geodata', mock_geodata)
        def test_visitors_location_is_derived_from_ip(self):

or even a class decorator:

    @patch.object(app.tracking.views, 'get_geodata', mock_geodata)
    class TrackingViewsTests(BaseTestCase):

The only difference is the scope of the patch.  The function decorator version ensures that as long as we are inside the `test_visitors_location_is_derived_from_ip` function `get_geodata` points at our mock, while the class decorator version ensures that every function that starts with `test` inside of `TrackingViewsTests` will see the mocked version of `get_geodata`.

Personally, I prefer to keep the scope of my mocks as limited as possible. It helps ensure that I keep my testing scope in mind, and saves me from surprises where I was expecting to have access to the real object and have to de-patch it.

#### Run the test

Having set up everything we need we can now make our request:

    with self.client:
        self.client.get(url, environ_overrides=wsgi_environment)

We provide our controller with the viewer's IP address through the `wsgi_environment` dictionary we created (`wsgi_environment = {'REMOTE_ADDR': '1.2.3.4'}`).  Flask's test client is an instance of Werkzeug's test client - which supports all of the arguments that you can pass to [`EnvironmentBuilder`][werkzeug.builder].

#### Assert that everything worked

Finally, we fetch all of the visits from the `tracking_visit` table:

    visits = Visit.query.all()

and verify that:

* We used the user's IP address to lookup his geodata:

        mock_geodata.assert_called_once_with('1.2.3.4')

* The request only generated one visit:

        self.assertEquals(1, len(visits))

* The location data was properly persisted:

        self.assertEquals('Los Angeles, 90001', visits[0].location)
        self.assertEquals('Los Angeles, 90001, 34.05, -118.25',
                          visits[0].location_full)

And that completes our first test with mocks.

## Debugging

Our unit tests are very useful - but what happens when we try to test something and the test code does not do what we expect it to do? Or even worse, when a user calls us up and complains that he has encountered an error?  If it is a system-wide problem, running our unit tests might reveal the issue ... but that could only happen if we checked in *and deployed* code without running our tests (and we would never do that, now would we?)

Assume that we always run our tests before committing and deploying, then our unit tests cannot help us when something breaks in production.  Instead, we will need to ask the user to provided us with a complete example, so that we can debug it locally.

Let's say that we engaged in a little bit of refactoring of our login form:

```python
# If you can see what's broken already, give yourself a prize
# and write a test to ensure it never happens again :-)

class LoginForm(Form):
    email = fields.StringField(validators=[InputRequired(), Email()])
    password = fields.StringField(validators=[InputRequired()])

    def validate_login(form, field):
        try:
            user = User.query.filter(User.email == form.email.data).one()
        except (MultipleResultsFound, NoResultFound):
            raise ValidationError("Invalid user")
        if user is None:
            raise ValidationError("Invalid user")
        if not user.is_valid_password(form.password.data):
            raise ValidationError("Invalid password")

        # Make the current user available
        # to calling code.
        form.user = user
```

and when we push it to production our first user sends us an email to let us know that he mis-typed his password and was still logged into the system.  We verify that this is the case on our live site. Woah, Nelly, that is not at all acceptable!  So we quickly take down the login page and replace it with a message saying we are down for maintenance and we'll be back as soon as possible (Rule #0 of SaaS - always treat your customers the way you would want to be treated).

Looking at it locally, we don't see any reason that users *should* be able to log in without a password.  However, we haven't written any tests to test that a mis-typed password is rejected with an error message, so we can't be 100% sure that this isn't an error in our code.  So let's write a test case and see what happens:

    # In app.users.tests
    def test_invalid_password_is_rejected(self):
        User.create(name='Joe', email='joe@joes.com', password='12345')

        with self.client:
            self.client.post('/login/', data={'name': 'Joe', 'password': '****'})

            self.assertTrue(current_user.is_anonymous())

Running the tests results in a failure:

    .F..
    ======================================================================
    FAIL: test_invalid_password_is_rejected (app.users.tests.UserViewsTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "~/dev/flask-tracking/app/users/tests.py", line 34, in test_invalid_password_is_rejected
        self.assertTrue(current_user.is_anonymous())
    AssertionError: False is not true

Okay, so we can reproduce it locally.  And we have a test case to yell at us until we fix the problem.  Good, we're on our way!

There are several ways we could debug the problem:

* We could scatter `print` statements throughout the application until we find the source of the error.
* We could generate intentional errors in our code and look at the existing environment using Flask's built-in debugger.
* We could step through the code using a debugger.

We'll use all three techniques.  First, let's add a simple `print` statement to our `app.users.models.LoginForm#validate_login` method:

    def validate_login(self, field):
        print 'Validating login'

When we run our tests again we do not see the "Validating login" message at all.  That tells us that our method is not being called.  Let's add an intentional error to our view and make use of Flask's internal debugger to verify the state of the world.  First, we'll create a new configuration for debugging:

    # In config.py
    class DebugConfiguration(BaseConfiguration):
        DEBUG = True

Then we will update `app.__init__` to use the new debug configuration:

    app.config.from_object('config.DebugConfiguration')

And finally, we will add a Arithmetic error to our `login_view` method:

    def login_view():
        form = LoginForm(request.form)
        1 / 0  # KABOOM!

Now, if we run:

```sh
$ python run.py
```

And navigate to the login page we will see a nice traceback.  Clicking on the shell icon on the right of the last line of the traceback (`1 / 0`) will get us an interactive REPL that we can use to test our function:

    >>> form.validate_login(field=None)  # We don't use the field argument

This results in:

    Traceback (most recent call last):
        File "<debugger>", line 1, in <module>
        form.validate_login(None)
        File "~/dev/flask-tracking/app/users/forms.py", line 15, in validate_login
        raise validators.ValidationError('Invalid user')
        ValidationError: Invalid user

So now we know that our validation function *works* - it simply is not being called.  Let's remove that division by zero error from our login view and replace it with a call to [the Python debugger `pdb`][pdb].

    def login_view():
        form = LoginForm(request.form)
        import pdb; pdb.set_trace()

Now, when we run our tests again we get a debugger:

    python -m unittest discover .
    .> ~/dev/flask-tracking/app/users/views.py(18)login_view()
    -> if form.validate_on_submit():
    (Pdb)

We can step into the `validate_on_submit` method by typing "s" for "step", and step over calls we are not interested in with "n" for "next" (a full introduction to PDB is beyond the scope of this tutorial - for more information on PDB see it's [documentation][pdb] or type "h" while inside of `pdb`):

    (Pdb) s
    --Call--
    > ~/.virtualenvs/realpython/lib/python2.7/site-packages/flask_wtf/form.py(120)validate_on_submit()
    -> def validate_on_submit(self):

I won't walk you through the whole debugging session, but needless to say, the issue was with our code. WTForms allows for inline validators in the form `validate_[fieldname]`.  Our `validate_login` method is never called because we don't have a field named `login` in our form.  Let's remove the `set_trace` call from our controller and rename our `app.users.forms.LoginForm.validate_login` method to `LoginForm.validate_password` so that WTForms will pick it up as an inline validator for our `password` field. This ensures that it only gets called after both the name and password fields have been validated to contain user-supplied data.

Now, when we run our unit tests again, they pass.  Testing locally reveals that we did indeed fix the issue.  We can now safely deploy and take down our maintenance message.

## Error Handling

As we have discovered, a test suite does not guarantee that we will have no bugs in our application.  It is possible for uses to still come across errors in production.  For example, if we simply blindly accessed `request.args['some_optional_key']` in one of our controllers and we only wrote tests with that optional key set in the request, the end user would get a `400 Bad Request` response from Flask by default. We want to show a *helpful* error message to the user in such cases. We also want to avoid showing the users unbranded or out-of-date pages without much help on where to go, or what to do next.

We already know that we can register error handlers with Flask to explicitly handle these sorts of issues.  In fact, we already registered one for the most common error - a mis-typed or no-longer existing link:

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

We may want to explicitly handle other kinds of errors as well, such as the 400 Bad Request errors that Flask generates for missing keys and the 500 Internal Server errors that are generated for uncaught exceptions:

    @app.errorhandler(400)
    def key_error(e):
        return render_template('400.html'), 400


    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('generic.html'), 500

In addition to the HTTP errors that we might have to deal with, Flask also allows us to display different error pages when an uncaught exception bubbles up to its level.  For now, let's just register a generic error handler for all uncaught exceptions (but later we may want to register specific ones for more-common error conditions that we cannot do anything about):

    @app.errorhandler(Exception)
    def unhandled_exception(e):
        return render_template('generic.html'), 500

Now all the most common cases of errors should be handled gracefully by our application.  If we wanted to ensure that *every* error is nicely styled we could register the same error handler for every possible error condition:

    from flask import Markup
    from werkzeug.exceptions import default_exceptions, HTTPException

    # ... skip other code in app/__init__.py ...

    def error_handler(error):
        if isinstance(error, HTTPException):
            description = error.get_description(request.environ)
            code = error.code
            name = error.name
        else:
            description = 'We encountered an error while trying to fulfill your request'
            code = 500
            name = 'Internal Server Error'
        return render_template(['{}.html'.format(code), 'generic.html'],
                                code=code,
                                name=Markup(name),
                                description=Markup(description))

    for exception in default_exceptions:
        app.register_error_handler(exception, error_handler)

This ensures that all the HTTP error conditions that Flask knows how to handle (4XX and 5XX level errors) have the `error_handler` function registered as their handler.  Coupled with a `app.register_error_handler(Exception, error_handler)`, this will cover almost every error that our application might throw.  (There are a few exceptions, such as `SystemExit` that will not be caught this way and C-level segfaults or OS-level events will obviously not be caught and handled in this way, but those sorts of catastrophic events should be act-of-God occasions, not something that our application needs to be prepared to handle on a semi-regular basis).

## Logging

Finally, let's talk about logging. Users will not always have enough time to reach out to us with a fully fleshed-out bug report (not to mention, bad actors will be actively looking for ways to take advantage of us.)  We need a way to ensure that we can look back in time and see what happened and when.

Fortunately, both Python and Flask have logging capabilities, so we do not need to re-invent the wheel here either.  A standard Python `logging` logger is available on the Flask object at `app.logger`.

The first place where we could use some logging is in our error handlers.  We don't need to log 404s as the proxy server will do that for us if we set it up right, but we will want to log the reasons for our other exceptions (400, 500 and Exception).  Let's go ahead and add some more detailed logging to those handlers.  Since we are doing the same thing in each handler, we will only show the first here:

    @app.errorhandler(400)
    def key_error(e):
        app.logger.warning('Invalid request resulted in KeyError', exc_info=e)
        return render_template('400.html'), 400

Python's documentation on the logging module has a good breakdown of the various available [logging levels][loglevels] and what they are most appropriate for.

For those times when we don't have access to the `app` (say, inside of our `view` modules) we can use the thread-local `current_app` in the exact same way as we would use `app`.  For an example, let's also add a bit of logging to our login and logout handlers:

    from flask import current_app

    @mod.route('/logout/')
    @login_required
    def logout_view():
        current_app.debug('Attempting to log out the current user')
        logout_user()
        current_app.debug('Successfully logged out the current user')
        return redirect(url_for('index'))

This code nicely demonstrates an issue we can run into with logging - having too much of it can be as bad as having too little.  In this case, we have as much debugging code as we have application code, and it is difficult to follow the flow of the code any more.  We'll go ahead and remove this particular logging code, as it doesn't add anything above and beyond what we would see in our proxy server's access logs.

If we needed to log the entry and exit of each controller, we could add handlers for [`app.before_request`][app.before_request] and [`app.teardown_request`][app.teardown_request]. Just for fun, here's how we might log every access to our application:

    @app.before_request
    def log_entry():
        context = {
            'url': request.path,
            'method': request.method,
            'ip': request.environ.get("REMOTE_ADDR")
        }
        app.logger.debug("Handling %(method)s request from %(ip)s for %(url)s", context)

If we run our application in debug mode and access our home page then we will see:

    --------------------------------------------------------------------------------
    DEBUG in __init__ [~/dev/flask-tracking/app/__init__.py:68]:
    Handling GET request from 127.0.0.1 for /
    --------------------------------------------------------------------------------

As was said above, in production logging this sort of information would be duplicating the logs that our proxy server (Apache with mod_wsgi, ngnix with uwsgi, etc.) will be generating.  We should only do this if we are generating a unique value for each request that we absolutely need to keep track of.

### Adding context and formatting to our logs

However, it would be nice to have the context from our `log_entry` handler (above) in our exception handlers.  Let's go ahead and add a [`Filter`][logging.filter] instance to the logger to provide the url, method, IP address, and user id to all loggers that are interested in them (this is called ["contextual logging"][context.log]:

    import logging
    
    
    class ContextualFilter(logging.Filter):
        def filter(self, log_record):
            log_record.url = request.path
            log_record.method = request.method
            log_record.ip = request.environ.get("REMOTE_ADDR")
            log_record.user_id = -1 if current_user.is_anonymous() else current_user.get_id()
    
            return True

This filter doesn't actually filter any of our messages - instead, it provides some additional information that we can make use of in our logs.  Here's an example of how we might use this filter:

    # Create the filter and add it to the base application logger
    context_provider = ContextualFilter()
    app.logger.addFilter(context_provider)

    # Optionally, remove Flask's default debug handler
    # del app.logger.handlers[:]

    # Create a new handler for log messages that will send them to standard error
    handler = logging.StreamHandler()

    # Add a formatter that makes use of our new contextual information
    log_format = "%(asctime)s\t%(levelname)s\t%(user_id)s\t%(ip)s\t%(method)s\t%(url)s\t%(message)s"
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)

    # Finally, attach the handler to our logger
    app.logger.addHandler(handler)

And here's what a log message might look like:

     2013-10-12 09:22:52,764    DEBUG   1   127.0.0.1   GET / Some additional message

One thing to note is that the message we pass to `app.logger.[LOGLEVEL]` is not expanded with the values in the context.  So if we had kept our `before_request` log call and changed our before request log call to just be:

    # Note the missing context argument
    app.logger.debug("Handling %(method)s request from %(ip)s for %(url)s")

the format strings will be passed through unaltered.  But since we have them in our [`Formatter`][logging.formatter], we can remove them from our individual message, leaving just:

    @app.before_request
    def log_entry():
        app.logger.debug("Handling request")

This is the advantage of contextual logging - we can include important information in all our log entries without needing to collect it manually at the site of every log call.

### Directing logs to different places

Most of the information we will be logging is not immediately actionable.  However, there are certain kinds of errors we want to know about immediately.  A rash of 500 errors probably means that something is broken with our application, for example.  We cannot stay glued to our logs 24/7 so we need to have severe errors shipped to us.

Fortunately, adding new handlers to our application logger is easy - and since each handler can filter log entries down to only the ones it finds interesting, we can avoid getting deluged by logs, but still get alerts when something breaks horribly.

By way of an example, let's add another handler that will log ERROR and CRITICAL log messages to a special file.  This will not give us the alerting we want, but email or SMS setup depends on your host (we'll do such a setup in a later article for Heroku).  To whet your appetite see the example of how to log to email in [Flask's documentation on logging][error.mail] or [these recipes][multithreaded.logging]:

    from logging import ERROR
    from logging.handlers import TimedRotatingFileHandler

    # Only set up a file handler if we know where to put the logs
    if app.config.get("ERROR_LOG_PATH"):

        # Create one file for each day. Delete logs over 7 days old.
        file_handler = TimedRotatingFileHandler(app.config["ERROR_LOG_PATH"], when="D", backupCount=7)

        # Use a multi-line format for this logger, for easier scanning
        file_formatter = logging.Formatter('''
        Time: %(asctime)s
        Level: %(levelname)s
        Method: %(method)s
        Path: %(url)s
        IP: %(ip)s
        User ID: %(user_id)s

        Message: %(message)s

        ---------------------''')

        # Filter out all log messages that are lower than Error.
        file_handler.setLevel(ERROR)

        file_handler.addFormatter(file_formatter)
        app.logger.addHandler(file_handler)

If we use this setup ERROR and CRITICAL log messages will appear both on the console and in the file specified in our configuration.

## Wrapping Up

We have covered a great deal in this article.  Starting out with unit testing, we covered what testing is and why we need it.  We moved on to writing tests, both with and without mocks.  We briefly covered three methods of debugging errors locally (`print`, intentional errors to trigger Flask's debugger, and `pdb`.)  We covered error handling and ensured that our end users should only see styled error pages.  Finally, we went over logging setups.

Next time we'll clean up our code base, get into the Refactor portion of [Test Driven Development's][TDD] "Red, Green, Refactor" and, if we have time, we'll add some more features in a test-first manner.

As always, the code is available from [the repository][repository].  Looking forward to continuing this journey with you.

  [Part I]: http://www.realpython.com/blog/python/python-web-applications-with-flask-part-i/
  [Part II]: http://www.realpython.com/blog/python/python-web-applications-with-flask-part-ii-app-creation/
  [repository]: https://github.com/mjhea0/flask-tracking
  [TDD]: http://en.wikipedia.org/wiki/Test-driven_development
  [config]: http://flask.pocoo.org/docs/config/#development-production
  [FT]: http://pythonhosted.org/Flask-Testing/
  [unit]: http://docs.python.org/2/library/unittest.html
  [test client]: http://flask.pocoo.org/docs/api/#flask.Flask.test_client
  [test context]: http://flask.pocoo.org/docs/testing/#keeping-the-context-around
  [freegeo]: http://freegeoip.net/
  [mock]: http://mock.readthedocs.org/en/latest/
  [mock.patch]: http://mock.readthedocs.org/en/latest/patch.html
  [werkzeug.builder]: http://werkzeug.pocoo.org/docs/test/#werkzeug.test.EnvironBuilder
  [pdb]: http://docs.python.org/2/library/pdb.html
  [wtforms cv]: http://wtforms.readthedocs.org/en/latest/validators.html#custom-validators
  [loglevels]: http://docs.python.org/2/howto/logging.html#when-to-use-logging
  [app.before_request]: http://flask.pocoo.org/docs/api/#flask.Flask.before_request
  [app.teardown_request]: http://flask.pocoo.org/docs/api/#flask.Flask.teardown_request
  [logging.filter]: http://docs.python.org/2/library/logging.html#filter-objects
  [context.log]: http://docs.python.org/2/howto/logging-cookbook.html#filters-contextual
  [logging.formatter]: http://docs.python.org/2/library/logging.html#formatter-objects
  [error.mail]: http://flask.pocoo.org/docs/errorhandling/#error-mails
  [multithreaded.logging]: http://stackoverflow.com/q/8616617/135978
  [rotating.loghandler]: http://docs.python.org/2/library/logging.handlers.html#timedrotatingfilehandler
