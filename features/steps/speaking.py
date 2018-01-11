from behave import *
from Animal import Animal

@given('we have an animal named {name}')
def step_impl(context, name):
    context.response = {}
    context.response['animal'] = Animal(name, 50)

@when('we tell it to speak')
def step_impl(context):
    context.response['says'] = context.response['animal'].speak()

@then('it should say "{says}"')
def step_impl(context, says):
    assert says == context.response['says']
