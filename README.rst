kidcorral
=========

App to manage children and their care. Will track parents emergency contacts,
list children allergies and notes, and can alert parents if there is an issue.

Will allow for parent login via web and printing tags.

Quickstart
----------

To run the app, first `migrate` to freshen the database then run app with::

    make init
    make migrate
    make run

You should have a server running on http://localhost:5000. Hurrah! A convenience
function to create a superuser::

    make su

TODO
----

* Volunteer portal
* Send notifications
* Security audit
* Tests
* Volunteer notifications
* Analytics
* Symmetric cipher (fernet?) every id card with date to ensure no tampering has occurred

License
-------

Please see attached LICENSE file for information
