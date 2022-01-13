import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage


class PopupObjects (BasePage):
    
    User_Dropdown = ["css", '[data-feature-preview-indicator-src="/users/CactusStar/feature_preview/indicator_check"]']
    Profile_status = ["css", '.btn-link.btn-block.Link--secondary.no-underline.js-toggle-user-status-edit.toggle-user-status-edit']
    Edit_Dialog = ["css", '[aria-label="Edit status"]']