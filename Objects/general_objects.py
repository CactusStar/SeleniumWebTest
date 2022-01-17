import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage

class GeneralObjects(BasePage):
    NewRepositories = ["css", ".btn.btn-sm.btn-primary"]
    Title = ["tag", "h1"]
    red = ["css", "label#repository-owner-label:after"]
    Repositories = ["css", ".f4.hide-sm.hide-md.mb-1.f5.d-flex.flex-justify-between.flex-items-center"]
    Explore_Repositories = ["css", ".f5.text-bold.mb-1"]
    Pull_Request = ["css", ".js-selected-navigation-item.Header-link.mt-md-n3.mb-md-n3.py-2.py-md-3.mr-0.mr-md-3.border-top.border-md-top-0.border-white-fade"]
    Request = ["css", ".d-inline.d-md-none.d-lg-inline"]
    Issues = ["css", 'a[href="/issues"]']
    Marketplace = ["link_text", "Marketplace"]
    Explore = ["link_text", "Explore"]
    New_Component = ["css", 'details[class="details-overlay details-reset"]']
    New_Component_MenuList = ["css", 'details[class="details-overlay details-reset"] details-menu a']