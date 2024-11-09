from datetime import datetime, timedelta
import random

# Obtener la hora actual
current_date = datetime.now()

# Calcular las 9 AM de hoy y las 9 AM de ayer
today_at_9am = current_date.replace(hour=9, minute=0, second=0, microsecond=0)
yesterday_at_9am = today_at_9am - timedelta(days=1)

# Generar una fecha aleatoria entre las 9 AM de ayer y las 9 AM de hoy
random_date = yesterday_at_9am + (today_at_9am - yesterday_at_9am) * random.random()

# Mostrar la fecha en formato ISO
print(random_date.isoformat())
