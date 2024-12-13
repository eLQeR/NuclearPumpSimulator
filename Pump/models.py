from django.db import models


class Pump(models.Model):
    STATUS_CHOICES = [
        ('OFF', 'Off'),
        ('ON', 'On'),
        ('ERROR', 'Error'),
    ]
    VALVE_STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
    ]
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OFF')
    pressure = models.FloatField(default=0.0)  # Тиск (бар)
    temperature = models.FloatField(default=0.0)  # Температура (°C)
    performance = models.FloatField(default=0.0)  # Продуктивність (л/с)
    power = models.FloatField(default=0.0)  # Потужність (кВт)
    rotation_speed = models.FloatField(default=0.0)  # Швидкість обертання (об/хв)
    is_wheel_rotating = models.BooleanField(default=False)  # Чи обертається колесо
    valve_status = models.CharField(max_length=10, choices=VALVE_STATUS_CHOICES, default='CLOSED')  # Стан клапана

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("start_pump", "Can start the pump"),
            ("stop_pump", "Can stop the pump"),
        ]


# Модель для зберігання логів насосів
class PumpLog(models.Model):
    pump = models.ForeignKey(Pump, related_name='logs', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"Log for {self.pump.name} at {self.timestamp}"
