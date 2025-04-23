#https://sdaia.gov.sa/en/Search/Pages/results.aspx?k=sdaia
#https://sdaia.gov.sa/en/default.aspx#
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL =os.getenv("BASE_URL")
MAIN_PAGE = os.getenv("MAIN_PAGE")
SEARCH_RESULT_PAGE =os.getenv("SEARCH_RESULT_PAGE")
