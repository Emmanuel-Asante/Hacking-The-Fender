# Import csv module
import csv

# Import json module
import json

# Create a list called compromised_users
compromised_users = []

# Open the password.csv file
with open("passwords.csv") as password_file:
  # Save the parsed csv.DictReader object as password_csv
  password_csv = csv.DictReader(password_file)
  # Iterate through password_csv
  for row in password_csv:
    # Save each row of password_csv in password_row
    password_row = row
    # Add username to compromised_users list
    compromised_users.append(password_row["Username"])

# Open Compromised_users_file.txt
with open("compromised_users.txt", "w") as compromised_user_file:
  # Iterate through compromised_users data
  for compromised_user in compromised_users:
    # Write each compromised_user in compromised_users to compromised_user_file
    compromised_user_file.write(compromised_user)

# Open a json file called boss_message.json in write mode
with open("boss_message.json", "w") as boss_message:
  # Create a dictionary called boss_message_dict
  boss_message_dict = dict()
  # Update boss_message_dict with some key-value pairs
  boss_message_dict.update({
    "recipient": "The Boss",
    "message": "Mission Success"
  })
  # Write out boss_message_dict to boss_message
  json.dump(boss_message_dict, boss_message)

# Open a new csv file in write mode
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
  _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  """
  # Write slash_null_sig to new_passwords_obj
  new_passwords_obj.write(slash_null_sig)