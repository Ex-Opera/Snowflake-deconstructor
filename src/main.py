import sys
from snowflake_converter import validate_snowflake

def main():
  while True:
    # Parse command-line arguments or prompt user for snowflake
    if len(sys.argv) == 2:
      snowflake = sys.argv[1]
    else:
      snowflake = input("Snowflake: ")
    # Convert snowflake and print result
    date_string = validate_snowflake(snowflake)
    if isinstance(date_string, str):
      print(date_string)
    else:
      print(f"Snowflake {snowflake} corresponds to date {date_string}")
      break

if __name__ == '__main__':
  main()
