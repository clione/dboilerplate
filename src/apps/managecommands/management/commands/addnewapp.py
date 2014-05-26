import sys, os
from importlib import import_module
from django.core.management.base import BaseCommand, CommandError
from django.core.management.templates import TemplateCommand
from resource_addnewapp import _models, _views

def change_to_apps_dir():
	apps_dir = os.path.join(os.getcwd(), 'apps')
	if not os.path.exists(apps_dir):
		raise CommandError("Apps directory could not be found. Make sure apps are stored on same level as manage.py")
	os.chdir(apps_dir)
	return

def create_new_app(app_name):
	change_to_apps_dir()
	if not os.path.exists(os.path.join(os.getcwd(), app_name)):
		os.makedirs(app_name)
	else:
		raise CommandError("An app with that name already exists in this directory. Could not create app.")
	os.chdir(os.path.join(os.getcwd(), app_name))
	open('__init__.py', 'a').close()
	return

class Command(TemplateCommand):
	help = 'Create a new advanced app in the current location, or location provided.'

	def handle(self, app_name=None, target=None, **options):
		self.validate_name(app_name, "app")

		try:
			import_module(app_name)
		except ImportError:
			pass
		else:
			raise CommandError("%r conflicts with the name of an existing "
					"Python module and cannot be used as an app "
					"name. Please try another name." % app_name)

		create_new_app(app_name)

		model_created = _models.request(app_name)
		_views.request(app_name, model_created)