Feature: getting the animal to speak
    In order to communicate with the animal
    As an owner
    I need to be able to have it speak.


    Scenario: Animal says it's name
        Given we have an animal named Stu
        When we tell it to speak
        Then it should say "Hello, my name is Stu"
