import os

import allure
import pytest
import shutil

current_path=os.path.dirname(os.path.abspath(__file__))
json_report_path=current_path+'\\report\\json_report'
html_report_path=current_path+'\\report\\html_report'

if __name__=="__main__":
    pytest.main(['-s','-v','-m run_case','--alluredir=%s'%json_report_path,'--clean-alluredir'])
    os.system('allure generate %s -o %s --clean' % (json_report_path, html_report_path))

    # # 压缩
    # shutil.make_archive(current_path+'\\report\\html_report','zip',html_report_path)
