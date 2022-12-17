import sys

from snowflake_converter import validate_snowflake

def main():
  # Parse command-line arguments or prompt user for snowflake
  if len(sys.argv) == 2:
    snowflake = sys.argv[1]
  else:
    snowflake = input("Enter a snowflake: ")

  # Convert snowflake and print result
  date_string = validate_snowflake(snowflake)
  if isinstance(date_string, str):
    print(date_string)
  else:
    print(f"Snowflake {snowflake} corresponds to date {date_string}")

if __name__ == '__main__':
  main()
