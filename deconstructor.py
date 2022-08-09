from datetime import datetime

DISCORD_EPOCH = 1420070400

def convert_snowflake(snowflake):
  milliseconds = int(snowflake >> 22)/1000
  return datetime.fromtimestamp(milliseconds + DISCORD_EPOCH).isoformat()

def validate_snowflake():
  while True:
    try:
      snowflake = int(input("Snowflake: ")
      if snowflake > 9999999999999999999:
        print("Error! Snowflakes have lower digits"); continue 
      if snowflake < 4194304:
        print("Error! Snowflakes are large numbers"); continue 
      print(convert_snowflake(snowflake))
    except ValueError:
      print("Snowflakes only contain numbers")

validate_snowflake()
