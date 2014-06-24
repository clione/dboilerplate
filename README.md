# dboilerplate

dboilerplate is a django template for setting up projects quickly. There are two options to use it:

* Install it from the repository:

Clone the repository to your computer and run afterwards this command:

    $ django-admin.py startproject --template=/path/to/the/template

* Install it from GitHub

This is the easiest way to install the template

    $ django-admin.py startproject --template=https://github.com/clione/dboilerplate/archive/master.zip myproject

## Requirements
- django 1.4.x-1.6.x
- Python 2.7.x

PLEASE NOTE: This boilerplate is still in development, the documentation
is not finished yet. You can help us if you want!

D-Boilerplate is a simple django boilerplate that we use at Havas Worldwide London to speed up our development process.

Features:

- Embedded sitemaps
- SCSS via grunt
- Automatic application creation
- Fabric scripts for deployment
- Muti environment requirements files
- Multi environment settings files
- Database data generator (for development stage, thanks Kaleidos)
- yawd-admin
- Improved logging mechanism


## Grunt Readme

You will need grunt, bower and compass installed for this boilerplate uses SCSS syntax for the CSS compiling

### Requirements

- Ruby 1.9+
- NodeJS

To install the required tools do (as root):

    # npm install -g bower grunt grunt-cli
    # gem install compass

#### After that enter the project and run

    $ npm install
    $ npm update
    $ bower install
    $ bower update
    $ grunt
    $ ./manage.py collectstatic


#### Building project

From frontend folder run...

    'grunt' - Build js and CSS files
    'watch' - Watch for changes to js or CSS files
