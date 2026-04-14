import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from supabase import create_client

SUPABASE_URL = "https://bvswdrtnvlikkdoxssle.supabase.co"
SUPABASE_KEY = "sb_publishable_SHVUrMe_SuNz-5ZgWz0q4g_CCRIASff"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)

while True:
    oled.fill(0)
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    try:
        response = supabase.table("messaggi").select("testo").eq("id", 1).execute()
        testo = response.data[0]["testo"] if response.data else "Messaggio non trovato"
    except:
        testo = "Errore connessione"

    draw.text((0, 0), testo, font=font, fill=255)
    oled.image(image)
    oled.show()

    time.sleep(1)