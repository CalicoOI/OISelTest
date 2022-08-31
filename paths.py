DRIVER_PATH = r"C:\Users\hlsmirn\PycharmProjects\OISelTest\WebDrivers\chromedriver.exe"
CV_PATH = r"C:\Users\hlsmirn\PycharmProjects\OISelTest\InputFiles\tmp.doc"
MAIN_PAGE_LINK = 'https://www.orioninc.com'
KILL_PROC_CMD = 'taskkill /f /im chromedriver.exe'

# cookie policy dialog window
COOKIE_CONFIRM_BUTTON = '/html/body/div[1]/div/div[2]/div/a[1]'

# careers page
NAV_BAR_PATH = '/html/body/header/div/nav'
COMPANY_SUBMENU = '/html/body/header/div/nav/div[2]/ul/li[5]/a'
COMPANY_CAREERS_SUBMENU = '/html/body/header/div/nav/div[2]/ul/li[5]/div/div/div/div[1]/a[6]'

# regions
REGIONS_BLOCK = '/html/body/main/article/div/div/div[2]/div/div[3]'
LATIN_AMERICA_IMG = '/html/body/main/article/div/div/div[2]/div/div[3]/div[2]/figure/a/img'

# search vacancy
SEARCH_FIELD = '/html/body/main/div[2]/div/div/div[2]/div[1]/form/input[1]'
SEARCH_REQUEST_BODY = "Robot+Python"
SEARCH_ERROR_MSG = 'no "Robot+Python" vacancy were found'

# apply
APPLY_BUTTON = '/html/body/main/article/div/div[3]/div[2]/div/div[1]/a'
FIRSTNAME = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[2]/div/div/input'
LASTNAME = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[3]/div/div/input'
EMAIL = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[4]/div/div/input'
PHONE = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[5]/div/div/input'
STATE = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[7]/div/div/input'
CITY = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[8]/div/div/input'
ZIP = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[9]/div/div/input'
SKILL_SUMMARY = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[11]/div/textarea'
ABOUT_US = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[14]/div/div/textarea'
SAVE_INFO_CHECKBOX = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[13]/div/ul/li/label'
SUBMIT_APPLICATION_BUTTON = '/html/body/main/article/div/div/div/div/div/div/form/div[3]/input[1]'
FILE_LOAD_ZONE = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[12]/div[1]/input[2]'
FILE_ERROR_MSG = 'error during file upload'
COUNTRY_BTN = '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[6]/div/div/div[2]/b'
