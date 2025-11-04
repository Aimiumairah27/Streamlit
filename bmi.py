import streamlit as st
import pandas as pd
import altair as alt


st.set_page_config(page_title="BMI Calculator",layout="centered")

st.title("💪BMI Calculator")
st.write("Lets calculate your **Body Mass Index[BMI]** and understand what is means")

st.header("Enter Your Details")

height = st.number_input("Enter your height (in cm)", min_value=50, max_value=250, value=170)
weight = st.number_input("Enter your weight (in kg)", min_value=10, max_value=300, value=70)

st.write("Your Height :",height,"cm")
st.write("Your Weight :",weight,"kg")


if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.write(f"Your BMI is **{bmi:.2f}**")

# BMI Category
    if bmi < 18.5:
        category = "Underweight 😞"
        color = "#8CC5EB"
 
    elif 18.5 <= bmi < 25:
        category = "Normal 😀"
        color = "#60D75E"
 
    elif 25 <= bmi < 30:
        category = "Overwieght 😳"
        color = "#D4D71F"
 
    else:
        category = "Obese 😵"
        color = "#F0510D"
   
    st.markdown(
        f"""
        <div style='background-color:{color};padding:15px;border-radius:10px;text-align:center'>
        <h3>Your BMI Category : {category}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )


import pandas as pd
import streamlit as st

st.header("BMI Range Chart")

bmi_table = pd.DataFrame({
    "Category": ["Underweight", "Normal", "Overweight", "Obese"],
    "Range": [18.5, 24.9, 29.9, 40]
})

st.bar_chart(bmi_table.set_index("Category"))

st.header("📊 BMI Range Chart")
 
# Data
bmi_data = pd.DataFrame({
    "Category": ["Underweight", "Normal", "Overweight", "Obese"],
    "Range": [18.5, 24.9, 29.9, 40]
})
 
# Define custom colors for each category
color_scale = alt.Scale(
    domain=["Underweight", "Normal", "Overweight", "Obese"],
    range=[ "#8CC5EB", "#60D75E","#D4D71F", "#E57373"]
)
 
# Create chart
chart = (
    alt.Chart(bmi_data)
    .mark_bar()
    .encode(
        x=alt.X("Category:N", title="BMI Category"),
        y=alt.Y("Range:Q", title="BMI Range"),
        color=alt.Color("Category:N", scale=color_scale, legend=None)
    )
    .properties(width=600, height=400)
)
 
st.altair_chart(chart, use_container_width=True)
