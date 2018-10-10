import traceback

from django.core.management.base import BaseCommand
from ffdb.models import PlayerStat

class Command(BaseCommand):
    """
        This command was intended for one-time use to migrate the data from a local Postgres database ('ffdb')
        to a Sqlite database for portability. It is included here as a reference for how to port the data
        back into a postgresql database if desired. (i.e. swap the 'using()' function, or DATABASE settings)
    """

    def handle(self, *args, **options):
        players = PlayerStat.objects.using('postg').all()
        total_players = players.count()
        current_player = 0
        for p in players:
            try:
                PlayerStat.objects.create(**p.as_dict())
            except Exception as e:
                traceback.print_exc()
                print(f'Failed to create player: {p.as_dict()}')
                break
            current_player += 1
            if current_player % 100 == 0:
                print(f'Converting Player: {current_player} of {total_players}')
