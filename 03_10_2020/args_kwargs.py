def say_hello(**kwargs):
    print("Hello,", kwargs["name"], kwargs["surname"])


say_hello(name="Ivan", surname="Ivanov")


def say_hello_to_all(*persons):
    for person in persons:
        say_hello(**person)


say_hello_to_all({"name": "Petr", "surname": "Petrov"}, {"name": "Boris", "surname": "Borisov"})