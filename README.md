# Xprosint: OSINT Twitter Account Information Tool
![Xprosint](XPROSINT.png)

Xprosint is a tool to gather publicly available information from Twitter accounts using the Twitter API v2. It provides details such as user profile information, follower count, recent tweets, and more.

## Features

- Retrieve user profile information (name, username, description, location, etc.).
- Get the number of followers, following, and tweets.
- Fetch recent tweets of the user.
- View the user's profile image and URL.
- Fetch the followers and following list of the user.

## Prerequisites

Before using this tool, you need the following:

- Python 3.x installed on your system.
- A **GitHub** account with access to the **Twitter API v2**.
- A **Personal Access Token** (PAT) for authentication.

## Installation

1. Clone the repository:

   `git clone https://github.com/Drag0nSlay/XPROSINT.git`
   
3. Navigate to the project directory:
   
    `cd XPROSINT`<br>
  
3. Create a virtual environment (recommended):

    `python -m venv venv`<br>
  
4. Activate the virtual environment:

- Windows:

    `venv\Scripts\activate`
  
- macOS/Linux:
  
    `source venv/bin/activate`

5. Install the required dependencies:
   
   `pip install -r requirements.txt`<br>

6. Set up your .env file with your Twitter API v2 credentials.
    - Get your Bearer Token from the Twitter Developer Portal.
    - Create a .env file in the root directory with the following content:<br>
    `BEARER_TOKEN=your_twitter_api_bearer_token_here`<br>

## Usage
Once the setup is complete, you can run the tool by passing a Twitter username as an argument.<br>

  `python Xprosint.py <twitter_username>`<br>
  
  For Example:<br>
  
  `python Xprosint.py jack`<br>

  This will fetch and display the following details about the user:

  - Name: Jack Dorsey
  - Username: @jack
  - Description: Just setting up my twttr
  - Followers Count: 6000000
  - Following Count: 1000
  - Tweet Count: 15000
  - Profile Image URL
  - Location<br>

##  Contributing
1. Fork the repository.
2. Create your feature branch (git checkout -b feature-name).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-name).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [MIT LICENSE](LICENSE) file for details.

## Follow Me
If you find this tool useful, feel free to follow me on GitHub:<br>
https://github.com/Drag0nSlay
