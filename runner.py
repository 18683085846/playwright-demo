import os
import pytest
if __name__ == '__main__':
    allure_report = r"E:\playwright-demo\TestReport\allure_report"
    allure_result = r"E:\playwright-demo\TestReport\allure_result"
    screenshot = r"E:\playwright-demo\TestReport\screenshot_path"
    os.system("del *.png")
    pytest.main(["-v", "-s", '--reruns=3', f'--alluredir={allure_result}', "--clean-alluredir"])
    os.system(f'allure generate {allure_result} -o {allure_report} --clean')
