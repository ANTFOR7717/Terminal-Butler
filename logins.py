class logins:
    def __init__(self, name, url, userpath, passpath, loginpath, additional):
        self.name = name
        self.url = url
        self.userpath = userpath
        self.passpath = passpath
        self.loginpath = loginpath
        self.additional = additional


example = logins(
    'example.com',                              # name       (Name of the Site)
    "https://example.com/login",  # url        (Url of the Site being logged into)
    '//*[@id="example-login-email-input"]',     # userpath   (Path needed to send email/username)
    '//*[@id="example-login-password-input"]',  # passpath   (Path needed to send password)
    '//*[@id="example-login-submit-button"]',   # loginpath  (Path needed to submit credentials)
    '//*[@id="example-additional-step"]'        # additional (Path needed to complete login)
)

github = logins(
    'github.com',  # name
    "https://github.com/login",  # url
    '//*[@id="login_field"]',  # userpath
    '//*[@id="password"]',  # passpath
    '//*[@id="login"]/form/div[3]/input[8]',  # loginpath
    ''  # additional
)

indeed = logins(
    'indeed.com',  # name       (Name of the Site)
    "https://secure.indeed.com/account/login",  # url        (Url of the Site being logged into)
    '//*[@id="login-email-input"]',  # userpath   (Path needed to send email/username)
    '//*[@id="login-password-input"]',  # passpath   (Path needed to send password)
    '//*[@id="login-submit-button"]',  # loginpath  (Path needed to submit credentials)
    ''  # additional (Path needed to complete login)
)

coinbase = logins(
    'coinbase.com',  # name
    "https://www.coinbase.com/signin",  # url
    '//*[@id="email"]',  # userpath
    '//*[@id="password"]',  # passpath
    '//*[@id="signin_button"]',  # loginpath
    ''  # additional
)

mail = logins(
    'mail.com',  # name
    "https://mail.com",  # url
    '//*[@id="login-email"]',  # userpath
    '//*[@id="login-password"]',  # passpath
    '//*[@id="login-form"]/button/span',  # loginpath
    '//*[@id="login-button"]'  # additional
)
