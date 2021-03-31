# Youtube Table of Content Generator

## Project Description

Small Python script to create a Youtube Table of Contents from Adobe Premiere Pro 2021 marker extract CSV file.

## Installation and execution

### Prerequisites

* Python 3.9.2 - here is the download [link](https://python.org/downloads)
* Git - here is the download [link](https://git-scm.com/downloads)

### Installation
```bash
# download the repository
git clone https://github.com/liotrusy/youtube_table_of_content_generator

# navigate to the new repository
cd youtube_table_of_content_generator
```

#### Only for testing purposes 

Do this only if you want to run unit test on the components and further develop the project.

```bash
# (only for testing and development) install the dependencies
pip install -r requirements.txt
```

### Execution
```bash
# run the application
python generate_table_of_contents.py [path to the file]

# for example - if file is in the same folder/directory
python generate_table_of_contents.py name_of_your_file.csv

# for example - if file is in desktop directory
python generate_table_of_contents.py "C:/users/youruser/desktop/name_of_your_file.csv"

```

## Development Notes

Project was developed and tested on a machine with Windows 10 operating system.



