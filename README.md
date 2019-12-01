# Diplomacy

A web browser version of the classic strategy board game 'Diplomacy'.

### Getting started

Copy the example settings file:
`cp project/settings/local.example.py project/settings.local.py` and change the
`local.py` file as necessary for local development:

 * To make the project work without using Docker, uncomment the sections
   labelled `# NOTE non Docker setup` and comment out the corresponding
   sections (which are not commented out by default).
   
### Running the tests

There local settings disable authentication on the service by default. This
causes tests which rely on authentication to fail. Use the test settings when
running the test suite:

`./manage.py test --settings=project.settings.test`

### Loading fixtures for dev

To load the fixtures run `make load_all_fixtures` from the root directory
within service container. This builds the initial state of a game.

### Test Coverage

To generate a test coverage report test coverage, run `coverage run manage.py
test` from within the container. Then run `coverage report` to see the results.
