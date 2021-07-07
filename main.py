# Baltazar Ortiz, Manuel Larios
import os
from parser import compose_message
from weather_email import send_message
from get_data import get_weather_data
from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import utc

# Load environment variables onto program
api_key = os.getenv('API_KEY')
sender_email = os.getenv('FROM_EMAIL')
receiver_email = os.getenv('SEND_EMAIL')
password = os.getenv('PASSWORD')

# Setup scheduler
task = BlockingScheduler(timezone=utc)


# Sends out an email every day at 17:30 UTC (9:30 AM Pacific time)
@task.scheduled_job('cron', hour=17, minute=30)
def send_email():
    """Composes and sends an email to the recipient"""

    weather_data = get_weather_data(api_key)
    subject_line = """Subject: Weather Update (Baltazar Ortiz)

    """
    message = compose_message(weather_data, subject_line)
    send_message(message, sender_email, receiver_email, password)


task.start()
