# -*- coding: utf-8 -*-
from lettuce import *
from lettuce import step
from dou_site import *


@step('Particular browser ([^"]*)')
def have_login_data(step, browser):
    world.brwsr = browser
    world.dou = Dou(world.brwsr)


@step('I input my login ([^"]*) and password ([^"]*) into the input fields')
def input_login_data(step, login, password):
    world.login = login[1:-1]
    world.pswd = password[1:-1]
    world.dou.login(world.login, world.pswd)


@step('I see my user icon in top right corner')
def check_icon(step):
    assert world.dou.am_i_logged(), "Login with: \'"+world.login+"\' and: \'"+world.pswd+"\' faild."


@step('After test browser must be closed')
def close_browser(step):
    world.dou.close_brwsr()

@step('I input wrong data, I\'m not logged in:')
def input_wrong_login_and_psw(step):
    for login_dict in step.hashes:
        input_login_data(step, login_dict['login'], login_dict['password'])
        assert world.dou.login_ban(), "Login with wrong data: \'"+world.login+"\' and: \'"+world.pswd+"\' accepted."
    close_browser(step)



