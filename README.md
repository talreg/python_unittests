Python unittest sample
========
This example shows how to use python unittest and the mock modules

Python version
-----
All the code was run with Python version 3.4

Running the project
-----
python app.py from the root of the app.

Running tests
---------
To run tests run `python -m unittest` from the root of the project. Run `python -m unittest -v` for a more verbal results.

About the sample classes
-----
There are 2 packages, simplemath and net. **simplemath** has a very simple module that contains one class.
This module is there in order to run a simple unittest (which is under the tests/simplemath folder) this basic object and test show how to use the unittest module basic.

In the **net** package, there are 2 classes; One that uses the other. **Title** is using **StatusCheck**.
This is to show how to use mocking, and how a mock object can replace methods in classes so it will be easier to test them. **StatusCheck** is testing a web address and also extract the title from it. **Title** is using this class just for the sake of testing. When the mock object is used, you can see that it always return the value noted there, as well as it doesn't connect anywhere, thus makes it perfect to use for remote API calls or any other method that takes too long or is too dangerous (remotely creating servers / deleting databases and so on).
