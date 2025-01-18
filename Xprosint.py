import tweepy
from dotenv import load_dotenv
import os
import re
import sys

# Load environment variables
load_dotenv()

# Access Bearer Token from .env
bearer_token = os.getenv("BEARER_TOKEN")

# Initialize Tweepy Client for Twitter API v2
client = tweepy.Client(bearer_token=bearer_token)

def sanitize_username(username):
    """
    Validate and sanitize the Twitter username.
    Removes '@' if present and ensures it matches Twitter's username format.
    """
    # Remove '@' if it exists at the start
    if username.startswith("@"):
        username = username[1:]
    
    # Check if username matches Twitter's format: alphanumeric or underscores, 1-15 characters
    if not re.match(r"^[A-Za-z0-9_]{1,15}$", username):
        raise ValueError("Invalid Twitter username format. Must be 1-15 characters, alphanumeric or underscores.")
    
    return username

def osint_twitter_account(account_name):
    """
    Fetch and display Twitter user information for the given username.

    Parameters:
        account_name (str): The Twitter username to fetch information for.

    Returns:
        None
    """
    try:
        # Sanitize the username
        account_name = sanitize_username(account_name)
        
        # Fetch user information
        response = client.get_user(
            username=account_name, 
            user_fields=["created_at", "description", "location", "profile_image_url", "public_metrics", "url"]
        )
        user = response.data

        # Display user information
        print(f"\nName: {user.name}")
        print(f"Username: @{user.username}")
        print(f"Description: {user.description}")
        print(f"Location: {user.location if user.location else 'Not provided'}")
        print(f"Account Created At: {user.created_at}")
        print(f"Profile Image URL: {user.profile_image_url}")
        print(f"URL: {user.url if user.url else 'Not provided'}")

        # Public metrics like followers, following, tweets
        public_metrics = user.public_metrics
        print(f"Followers Count: {public_metrics['followers_count']}")
        print(f"Following Count: {public_metrics['following_count']}")
        print(f"Tweet Count: {public_metrics['tweet_count']}")

    except tweepy.TooManyRequests:
        print("Rate limit reached. Please try again after 15 minutes.")
        sys.exit(1)  # Exit the program
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except tweepy.TweepyException as te:
        print(f"Error fetching data for {account_name}: {te}")

def usage_info():
    """
    Display usage information for the tool.
    """
    print("\nUsage Information:")
    print("------------------")
    print("This tool fetches publicly available Twitter user information.")
    print("\nHow to use:")
    print("1. Ensure you have a valid Bearer Token in the .env file.")
    print("2. Run the script and provide a valid Twitter username as an argument.")
    print("\nExample:")
    print("   python Xprosint.py username")
    print("\nRules for Twitter Usernames:")
    print("- Only alphanumeric characters and underscores are allowed.")
    print("- Must be between 1 and 15 characters long.")
    print("\nNote: Do not include '@' in the username; the tool will handle it automatically.")
    print("\nFollow me on GitHub: https://github.com/Drag0nSlay")

# Entry point of the script
if __name__ == "__main__":
    # Check if a username is provided as an argument
    if len(sys.argv) < 2:
        usage_info()
    else:
        # Get the username from the command-line argument
        username = sys.argv[1]
        osint_twitter_account(username)