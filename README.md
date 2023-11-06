# Roblox-Discord-Group-Checker 
## It may be outdated !!!
This Python script is designed to manage and verify users within a Discord server by cross-referencing their roles with their Roblox group affiliations. The script utilizes the Discord API and Roblox API to fetch user information, group affiliations, and roles. Here's a brief overview of the script's functionality:

# Features
Deep Scan Command: This command initiates a deep scan process that may take some time. After the scan, it creates a list with the data it scanned from the roblox groups using the API.

List All Users Command: This command retrieves a list of all members in the Discord server and categorizes them based on their roles and Roblox group affiliations. It differentiates between members of the higher ranks, regular members, and those not in the group.

Check Verifications Command: This command checks if the user running the command already has a specific Discord role, such as "Hicom" If they don't have the role, it adds the role to the user.

# Usage
Before running the script, you should:

Replace the token variable with your own Discord Bot token.
Update the channel ID in the bot.get_channel(...) line with the appropriate channel.
# To use the script:

Run the script, and the bot will log in to your Discord server.

Use the provided commands within your Discord server to perform various checks and verifications.

The script will categorize and list users based on their roles and Roblox group affiliations, providing valuable information for server management.

# Disclaimer
This script is tailored for a specific use case involving Discord and Roblox integration. Ensure you have the appropriate permissions and access to the relevant APIs and channels. Modify and use this script responsibly, taking into consideration the privacy and security of your server's members.

If you have any questions or need further assistance with this script, feel free to reach out.

