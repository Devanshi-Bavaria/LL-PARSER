# LL Parser

LL Parser is a web application that demonstrates the LL Parsing technique used by compilers to perform top-down non-recursive parsing. This project is implemented using Python for the main logic and Streamlit for the web interface.

## About LL Parsing

LL Parsing, or LL(1) Parsing, is a parsing strategy used in compiler design. It reads input from Left to Right, and constructs a Leftmost derivation of the sentence (hence LL). The (1) indicates that there is a one-symbol look-ahead in the parsing process. For more details, refer to this [GeeksforGeeks article](https://www.geeksforgeeks.org/construction-of-ll1-parsing-table/).

## Tech Stack

- Python: Used for implementing the main logic of the application.
- Streamlit: Used for creating the web interface of the application.

## Local Development

Follow these steps to set up the project for local development:

1. Clone the repository:
   ```bash
   git clone https://github.com/arunimabarik75/LL-Parser.git
   ```
2. Create a virtual environment inside the cloned repository:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:

   For Windows:
   ```bash
   venv\Scripts\activate
   ```
   For Linux:
   ```bash
   source venv/bin/activate
   ```
4. Install the required libraries:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
5. Run the Streamlit application:
   ```bash
   streamlit run home.py
   ```

## Deployment

The application is deployed using Streamlit Community Cloud and can be accessed [here](https://ll-parsing.streamlit.app/).
