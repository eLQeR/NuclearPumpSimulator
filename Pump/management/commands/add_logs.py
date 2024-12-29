import random
from django.core.management.base import BaseCommand
from Pump.models import Pump, PumpLog


class Command(BaseCommand):
    help = "Додати 60 рандомних логів для кожного насоса"

    def handle(self, *args, **kwargs):
        pumps = Pump.objects.all()
        for pump in pumps:
            for _ in range(60):
                PumpLog.objects.create(
                    pump=pump,
                    pressure=random.uniform(0.0, 10.0),
                    temperature=random.uniform(20.0, 100.0),
                    performance=random.uniform(0.0, 100.0),
                    power=random.uniform(0.0, 10.0),
                    rotation_speed=random.uniform(0.0, 3000.0),
                    is_wheel_rotating=random.choice([True, False]),
                    valve_status=random.choice(['OPEN', 'CLOSED']),
                )
        self.stdout.write(self.style.SUCCESS('Додано 60 логів для кожного насоса'))
