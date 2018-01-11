Feature: petting the animal
    In order to make the animal happy
    As an owner
    I need to be able to pet it.

    Scenario: Pet animal
        Given we have an animal which is at a happiness level of 50/100
        When we pet it
        Then its happiness should increase

    Scenario: Pet animal with full happiness
        Given we have an animal which is at a happiness level of 100/100
        When we pet it
        Then its happiness should be the same

    Scenario: Pet animal 5 times
        Given we have an animal which is at a happiness level of 5/100
        When we pet it 5 times
        Then its happiness should equal 30

    Scenario: Annoy animal 5 times
        Given we have an animal which is at a happiness level of 30/100
        When we annoy it
        Then its happiness should decrease

    Scenario: Annoy animal 5 times
        Given we have an animal which is at a happiness level of 30/100
        When we annoy it 5 times
        Then its happiness should equal 5


    Scenario: Over
