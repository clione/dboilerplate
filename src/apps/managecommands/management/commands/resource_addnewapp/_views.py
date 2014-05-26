import string
from _commons import validate_yes_no, return_template, is_class_based
import _urls

def create_view(views_name, views_type, model_name = False):

	with open('views.py', 'a+b') as view_file:

		# If a model was previously created, add it as an import line
		if model_name:
			view_file.write('from models import %s \n' % model_name)

		# Change template used depending on class or function based view
		if is_class_based(views_type):
			temp_id = 'cbv_views'
		else:
			temp_id = 'views'

		template = string.Template(open(return_template(temp_id)).read())
		variables = {'VIEWNAME':views_name}
		result = template.substitute(variables)

		view_file.write(result)
		
		view_file.close()

	return

def request(app_name, model_name = False):
	while True:
		views_required = validate_yes_no(raw_input('Does your app require a views.py [y/n]: '))
		if views_required:
			
			# Request name of view
			views_name = raw_input('Enter the name of your view: ')
			if not views_name:
				views_name = 'MyView'

			# Request whether view should be classed based or function 
			views_type = raw_input('Is your view a) class based or b) a function [a/b]: ')

			create_view(views_name, views_type, model_name)

			_urls.request(views_type, views_name)

			return

		elif views_required is None:
			pass
		elif not views_required:
			return