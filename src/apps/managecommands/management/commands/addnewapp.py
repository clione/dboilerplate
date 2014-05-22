from django.core.management.base import BaseCommand, CommandError
from django.core.management.templates import TemplateCommand

class Command(BaseCommand):
	help = 'Create a new advanced app in the current location, or location provided.'

	def handle(self, app_name=None, target=None, **options):
		self.validate_name(app_name, "app")

		return