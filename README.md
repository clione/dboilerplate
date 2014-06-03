dboilerplate
============

PLEASE NOTE: This boilerplate is still in development, the documentation
is not finished yet. You can help us if you want!

D-Boilerplate is a simple django boilerplate that we use at Havas Worldwide London to speed up our development process.

Compatible with django versions: 1.4.x-1.6.x

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


Grunt Readme
============

You will need grunt, bower and compass installed for this boilerplate uses SCSS syntax for the CSS compiling

Requirements
------------

- Ruby 1.9+
- NodeJS

To install the required tools do (as root):

`# npm install -g bower grunt grunt-cli`

`# gem install compass`

After that enter the project and run
------------------------------------

`$ npm install`

`$ npm update`

`$ bower install`

`$ bower update`

`$ grunt`

`$ ./manage.py collectstatic`


----Requirements----

Git Ruby 1.9+ NodeJS


----Install----

(GLOBAL)
npm install -g bower

(PROJECT)
npm install
npm update
bower install
bower update

----Building project----

From frontend folder run...

'grunt' - Build js and CSS files
'watch' - Watch for changes to js or CSS files
