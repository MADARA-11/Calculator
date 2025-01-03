import streamlit as st

st.title("The calculator")
# st.subheader("surya know no math")

num1 = st.number_input("Enter a number : ",value= 0)
num2 = st.number_input ("Enter a number:",value= 0)


# var = st.button('Calculate') # returns boolean value : TRue/False
#
#  st.write(var)


# if the user clicks on the button : true
# if the user does not click on the button : false

# if st.button("Calculate"):
#     ans = num1 + num2
#     st.write(f"The addition of {num1} and {num2} is {ans}") 

symbol = st.selectbox("Choose the operation ",("Add +", "sub -","mulp *","div /","floor div //","modulus %","exponents**"))

if st.button("Calculate"):
    if symbol == "Add +":
        ans = num1 + num2
        st.write(f"The addition of {num1} and {num2} is {ans}")
    elif symbol == "sub -":
            ans = num1 - num2
            st.write(f"The subtraction of {num1} and {num2} is {ans}")
    elif symbol == "mulp *":
            ans = num1 * num2
            st.write(f"The mulp of {num1} and {num2} is {ans}")
    elif symbol == "div /":
            ans = num1 / num2
            st.write(f"The div of {num1} and {num2} is {ans}")
    elif symbol == "exponents**":
            ans = num1 ** num2
            st.write(f"The exponents of {num1} and {num2} is {ans}")
    elif symbol == "floor div //":
            ans = num1 // num2
            st.write(f"The floordiv of {num1} and {num2} is {ans}")
    

# if st.button('Calculate'):
#     if symbol == "Add +" :
#         ans = num1 + num2
#         st.write(f"The addition of {num1} and {num2} is {ans}") 

# if st.button("subtraction"):
#     if symbol == "sub -":
#         ans = num1 + num2
#         st.write(f"the subtration of {num1} and {num2} is {ans}")

# if st.button("multiplication"):
#     if symbol == "mulp *":
#         ans = num1 * num2
#         st.write(f"The multiplication of {num1} and {num2}is {ans}")

# if st.button("division"):
#     if symbol == "div /":
#         ans = num1 / num2
#         st.write(f"The division of {num1} and {num2} is {ans} ")
# if st.button ("floor division"):
#     if symbol == "floor div //":
#         ans = num1 // num2
#         st.write(f"The floor division of {num1} and {num2} is {ans}")

# if st.button ("modulus"):
#     if symbol == "modulus %":
#         ans = num1 % num2
#         st.write(f"The modulus of {num1} and {num2} is {ans}")

# if st.button ("Exponente"):
#     if symbol == "exponents**":
#         ans = num1 ** num2
#         st.write(f"The exponents of {num1} ans {num2} is {ans}")

        # complete for the rest operators : sub,mult,div,floor div,modulus,exponents