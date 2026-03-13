import streamlit as st
import pandas as pd

st.title("N-1 Contingency: Supply Chain Logistics")

# Sliders moved to the sidebar
st.sidebar.header("System Variables")
st.sidebar.write("Adjust the sliders to test the system.")
n_trucks = st.sidebar.slider("Number of Trucks (N)", min_value=2, max_value=20, value=5)
capacity = st.sidebar.slider("Capacity per Truck (C)", min_value=10, max_value=100, value=50)
demand = st.sidebar.slider("Total Daily Demand (D)", min_value=10, max_value=1000, value=180)

# Mathematical calculations
normal_capacity = n_trucks * capacity
n_minus_1_capacity = (n_trucks - 1) * capacity

st.header("The Math")

# General Equations (Static)
st.write("General Formula:")
st.latex(r"C_{normal} = N \times C")
st.latex(r"C_{N-1} = (N - 1) \times C")
st.latex(r"\text{Condition for Success: } C_{N-1} \ge D")

# Substituted Equations (Dynamic)
st.write("Applied to these specific Variables:")
st.latex(r"C_{normal} = " + f"{n_trucks} \\times {capacity} = {normal_capacity}")
st.latex(r"C_{N-1} = " + f"({n_trucks} - 1) \\times {capacity} = {n_minus_1_capacity}")

# Conditional logic for N-1 status
if n_minus_1_capacity >= demand:
    st.latex(f"{n_minus_1_capacity} \ge {demand}")
    st.success(f"PASS: The remaining {n_trucks - 1} trucks can carry the {demand} units of demand.")
else:
    st.latex(f"{n_minus_1_capacity} < {demand}")
    deficit = demand - n_minus_1_capacity
    st.error(f"FAIL: The remaining {n_trucks - 1} trucks fall short. You will fail to deliver {deficit} units.")

# Visual Representation
st.header("Visual Representation")
# Simplified chart removing irrelevant "Normal Capacity" data
chart_data = pd.DataFrame(
    {
        "Units": [demand, n_minus_1_capacity]
    },
    index=["1. Required Demand", "2. Surviving N-1 Capacity"]
)

st.bar_chart(chart_data)

# ELI5 Explanation
st.header("ELI5: Understanding the Chart")
st.write("The 'Required Demand' bar shows the exact amount of work you MUST finish today. The 'Surviving N-1 Capacity' bar shows the maximum amount of work your trucks can actually do after one truck breaks down.")
st.write("For an N-1 system to succeed, the Capacity bar must be taller than (or exactly equal to) the Demand bar. If the Capacity bar is shorter, you do not have enough space left to carry all your boxes, and the system fails.")
