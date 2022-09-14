# Stats capture

 `Stats capture allows  some basic statistics on a collection of small positive integers`

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.

## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have installed the latest version of `python 3.6` or later
* You have a `<Linux/Mac>` machine.

## Installing Stats Capture

To install Stats capture, follow these steps:



To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

Export the directory which contains the project. 
```
export PYTHONPATH=/Users/<USER>/.../stats-capture-team-international  
```

## Test

```
$ python3 -m pytest app/tests/
```

## Run sample


```
$ python3 app/main.py
```


## Contributors

Thanks to the following people who have contributed to this project:

* [@carlos-saldarriaga](https://github.com/carlos-saldarriaga) 📖


## Contact

If you want to contact me you can reach me at <saldarriagac.montiel@gmail.com>.

