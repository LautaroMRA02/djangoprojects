import datetime
from django.utils import timezone
from  django.core.management.base import BaseCommand
from pastebin.models import Paste

class Command(BaseCommand):
    help = """
            deletes pastes not updated in last 24 hours

            Use this subcommand in a cron job
            to clear older pastes
    """

    def handle(self, **options):
        now = timezone.now()
        yesterday =  now - timezone.timedelta(1)
        old_pastes = Paste.objects.filter(updated_on__lte=yesterday)
        print(f"pastes eliminados: {len(old_pastes)}")
        old_pastes.delete()