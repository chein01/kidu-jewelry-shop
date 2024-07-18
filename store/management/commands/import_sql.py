# your_app/management/commands/import_sql.py

from django.core.management.base import BaseCommand
from django.db import connection
import os


class Command(BaseCommand):
    help = "Import SQL file into database"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the SQL file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File '{file_path}' does not exist"))
            return

        with open(file_path, "r") as sql_file:
            cursor = connection.cursor()
            try:
                cursor.execute(sql_file.read())
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Failed to import SQL file: {str(e)}")
                )
                return

        self.stdout.write(
            self.style.SUCCESS(f"Successfully imported SQL file '{file_path}'")
        )
