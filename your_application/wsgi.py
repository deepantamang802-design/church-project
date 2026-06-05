from pathlib import Path
import os
import sys

BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "church_platform.settings")

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

call_command("migrate", interactive=False, run_syncdb=True, verbosity=0)

application = get_wsgi_application()
