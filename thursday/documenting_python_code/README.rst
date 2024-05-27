DOCUMENTING PYTHON CODE
=======================

*Python documentation essentials—learn about Docstrings, Sphinx, reStructuredText, and embracing a docs-as-code approach with different markup languages.*


.. important::
    `Recording of the talk <https://www.youtube.com/live/z7icIiS50-Q?feature=shared&t=3145>`_

    `Page of the talk <https://2024.pycon.it/en/event/documenting-python-code>`_

Short conclusion of the talk is that for the time being the most efficient markup language to document your code
would be AsciiDoc. However in Python it is not well integrated with automatic documentation generation tools like Sphinx.
For this reason it would be the best choice to stick to reStructuredText.

**To try out the example shown in the talk you need to:**

1. Run ::

    pip install -r requirements.txt

2. Make *docs* directory ::

    mkdir thursday/documenting_python_code/examples/docs

3. Change directory to *docs* ::

    cd thursday/documenting_python_code/examples/docs

4. Start sphinx project ::

    sphinx-quickstart

5. Select **y** to separate source and build directories
and enter details that prompts ask on each step

6. Copy **conf.py** and **index.rst** files from *documenting_python_code/examples* directory
to *documenting_python_code/examples/docs/source* directory

7. Run ::

    sphinx-apidoc -o source/ ../sphinx_apidoc

8. Run ::

    make html

9. From directory *documenting_python_code/examples/docs/build/html* open the index.html file in your browser
to check the documentation for the **bank_account** module that was provided in the example
