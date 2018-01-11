from behave import *
from Animal import Animal

@given('we have an animal which is at a happiness level of {happiness}/100')
def step_impl(context, happiness):
    context.response = {};
    context.response['animal'] = Animal('Brian', happiness)
    context.response['happiness'] = int(happiness)

@when('we pet it')
def step_impl(context):
    context.response['animal'].pet()

@when('we pet it {amount} times')
def step_impl(context, amount):
    for i in range(0, int(amount)):
        context.response['animal'].pet()

@when('we annoy it')
def step_impl(context):
    context.response['animal'].annoy()

@when('we annoy it {amount} times')
def step_impl(context, amount):
    for i in range(0, int(amount)):
        context.response['animal'].annoy()

@then('its happiness should increase')
def step_impl(context):
    assert context.response['happiness'] < context.response['animal'].happiness

@then('its happiness should decrease')
def step_impl(context):
    assert context.response['happiness'] > context.response['animal'].happiness

@then('its happiness should equal {amount}')
def step_impl(context, amount):
    print(context.response['animal'].happiness)
    assert context.response['animal'].happiness == int(amount)

@then('its happiness should be the same')
def step_impl(context):
    assert context.response['happiness'] == context.response['animal'].happiness

