from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'This is a custom command to demonstrate usage.'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the user')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        self.stdout.write(self.style.SUCCESS(f'Hello, {name}!'))



# Location of Custom Command file is below
# "C:\Users\hello\django\first\app_one\management\commands\custom_command.py"

# Add below code in "C:\Users\hello\django\first\first\settings.py"
# INSTALLED_APPS = [
#    'app_one',

# Now run belo command to execute the custom command
# PS C:\Users\hello\django\first> python manage.py custom_command yogi

# Project Structure
# C:\Users\hello\django\first
# C:\Users\hello\django\first\manage.py
# C:\Users\hello\django\first\first
# C:\Users\hello\django\first\app_one
# C:\Users\hello\django\first\app_one\management\commands
# C:\Users\hello\django\first\app_one\management\commands\custom_command.py


