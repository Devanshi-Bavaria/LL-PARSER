import streamlit as st
import pandas as pd
from process_input import process_user_input, print_dictionary
from left_recursion import removeLeftRecursion
from left_factoring import removeLeftFactoring
from first import computeAllFirsts
from follow import computeAllFollows
from parse_table import createParseTable
from parse_string import parsingUsingStack

print("---------------------------------------------------------------------")
st.set_page_config(layout="wide")

# Header
st.title("LL Parser Visualisation")
st.divider()
print("Loading Header....")

# Take user input
st.header("Grammar")
st.text("Starting Symbol")
start_symbol = st.text_input("Starting Symbol", label_visibility="collapsed")
st.text("Productions (Example: S -> aA | bcD)")
prods = st.text_area("Example", height=200, label_visibility="collapsed")
print("Input taken....")

# Process input
processed_input = process_user_input(prods)
print("Processed Input: ", processed_input)
print("Input processed....")

# Remove left recursion and left factoring
productions_1 = removeLeftRecursion(processed_input)
productions = removeLeftFactoring(productions_1)
print("Productions: ", productions)
print("Left recursion and factoring removed....")

# Find first and follow sets
first_set = computeAllFirsts(productions)
follow_set = computeAllFollows(start_symbol, productions)

terminals = list(first_set.keys())
first_list = [" , ".join(first_set[non_terminal]) for non_terminal in first_set]
follow_list = [" , ".join(follow_set[non_terminal]) for non_terminal in follow_set]

first_follow_df = pd.DataFrame(
    {"First": first_list, "Follow": follow_list}, index=pd.Series(terminals)
)
print("First and follow sets computed....")

# Parsing table
print("Parsing Table")

parse_table, ll_grammar, non_terminals = createParseTable(
    productions, first_set, follow_set
)

parsing_table_df = pd.DataFrame(parse_table, index=pd.Series(non_terminals))
print("Parsing table created....")

# ------------------------------------------------------------------------------

st.header("Left Recursion")
if st.button("Remove Left Recursion"):
    print = print_dictionary(productions_1)
    for line in print:
        st.text(line)

st.header("Left Factoring")
if st.button("Remove Left Factoring"):
    print = print_dictionary(productions)
    for line in print:
        st.text(line)

st.header("First Follow Set")
if st.button("Find First and Follow Sets"):
    st.table(first_follow_df)

st.header("Parsing Table")
if st.button("Generate Parsing Table"):
    st.table(parsing_table_df)
    if ll_grammar:
        st.text("Grammar is LL 1")
    else:
        st.text("Grammar is not LL 1")

# -------------------------------------------------------------------------------

# String tracing
st.header("Parse String")

st.text("String")
try:
    string = st.text_input("String", label_visibility="collapsed")
    print("Input string: ", string)
except:
    pass


if st.button("Parse String"):
    return_string, dataframe = parsingUsingStack(
        productions, parse_table, ll_grammar, string, start_symbol
    )

    st.text(return_string)
    if dataframe is not None:
        st.table(dataframe)

webpage_details = """


<h1 style="text-align: center; text-decoration: underline"> LL Parser </h1>


<p style="text-justify: inter-word"> 
An LL (Left-to-Right, Leftmost derivation) parser is a type of top-down parsing technique used in the field of compiler construction and formal language processing. It is used to analyze and parse the syntax of a programming language or any formal language described by a context-free grammar. 

1. **Predictive Parsing:** LL parsers are predictive parsers, meaning they make parsing decisions based on the next input token (or a lookahead token). The parser predicts the production rule to apply by examining the current input symbol without any backtracking.

2. **Table-Driven Approach:** LL parsing can be implemented using a table-driven approach, which simplifies the parsing process. LL parsing tables (often referred to as LL(1) tables) are precomputed for a given grammar, and these tables help the parser make decisions efficiently.

3. **Advantages:** LL parsers are typically easier to implement and more efficient in practice for LL(1) grammars. They are well-suited for languages with relatively simple syntax. Many programming languages, like Pascal and C, can be parsed efficiently using LL parsers.

4. **Challenges:** LL parsing is limited to LL(1) grammars, which means the parser can't handle ambiguous grammars or languages that require more extensive lookahead. Dealing with left-recursion in the grammar can also be challenging, although there are techniques to eliminate it.

5. **Recursive Descent Parsers:** One common way to implement an LL parser is to use a recursive descent parsing technique. In recursive descent parsing, the parser is built using a set of recursive procedures or functions, each corresponding to a non-terminal symbol in the grammar.

6. **LL(k) and LL(*) Parsers:** While LL(1) parsers are the most common, there are also LL(k) parsers and more advanced variations like LL(*) parsers that can handle more complex grammars by allowing larger lookahead.

 </p>

"""

developer_details = """
<hr>
<h3 style="text-align: center; text-decoration: underline"> Developed By </h3>
<h4 style="text-align: center"> Arunima Barik (20BCE016) <br> Gaurav Golchha (20BCE079) </h4>

"""

# Add a footer to your Streamlit app
st.sidebar.markdown(
    f"""
                {webpage_details}
            
                {developer_details}
    
    """,
    unsafe_allow_html=True,
)
