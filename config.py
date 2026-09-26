import os

TRUECALLER_API_KEY = os.getenv('TRUECALLER_API_KEY')
NUMBERBOOK_API_KEY = os.getenv('NUMBERBOOK_API_KEY')
NUMVERIFY_API_KEY = os.getenv('NUMVERIFY_API_KEY')
OPENCNAM_API_KEY = os.getenv('OPENCNAM_API_KEY')

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = int(os.getenv('REDIS_DB', 0))

TELEGRAM_BOT_TOKEN = os.getenv('8790067022:AAEQXzvxc4jUL7ETAkM9p9TjwjPpxpJSQUY')

ADMIN_USER_ID = os.getenv('8809385256','your_telegram_id')

AUTHORIZED_USERS = ['@Saju_404']
