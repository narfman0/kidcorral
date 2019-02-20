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

* Expose identification/information tags (print)
* Send notifications

* Register/sign in via phone
* Update profile by person login credentials
* Volunteer notifications
* Analytics
* Hash every id card with date to ensure no tampering has occurred

License
-------

Please see attached LICENSE file for information
