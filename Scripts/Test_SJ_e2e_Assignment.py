import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time
from Page_Object_Model.Launch_page_object import SJOrangeHRM


@pytest.mark.usefixtures("browser_cbt")
class Test_SJ_Assignment1_e2e:

    def test_sj_validation(self, readJson):
        
        obj = SJOrangeHRM(self.driver)  # Activating the driver which we have created in supporting file (qualitrix_page_object.py).
        obj.launch_the_app(readJson['url_assessment1'])
        obj.update_info()
        obj.Leave_flow()
        obj.Recruitment_flow()
        
        