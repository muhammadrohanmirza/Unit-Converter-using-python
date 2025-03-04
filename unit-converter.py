import streamlit as st  # Import Streamlit for creating the web-based UI
st.title("🌍Unit Converter App")
st.markdown("### Converts Length, Weight And Time Instantly")
st.write("Hi there!  Enter a value, choose a category, and receive the converted result instantly.")

category = st.selectbox("Choose a categoty", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):

    if category == "Length":
        if unit == "Kilometer to Metre":
            return value * 1000
        elif unit == "Metre to Kilometer":
            return value / 1000
        if unit == "Foot to Inch":
            return value * 12
        elif unit == "Inch to Foot":
            return value / 12
        if unit == "Metre to Centimeter":
            return value * 100
        elif unit == "Centimeter to Metre":
            return value / 100
        
    elif category == "Weight":
        if unit == "Kilogram to Gram":
            return value * 1000
        elif unit == "Gram to Kilogram":
            return value / 1000
        if unit == "Gram to Miligram":
            return value * 1000
        elif unit == "Miligram to Gram":
            return value / 1000
        if unit == "Miligram to Microgram":
            return value * 1000
        elif unit == "Microgram to Miligram":
            return value / 1000

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
    return 0
        
if category == "Length":
    unit = st.selectbox("📏 Select Conversation", ["Kilometer to Metre","Metre to Kilometer","Foot to Inch","Inch to Foot","Metre to Centimeter","Centimeter to Metre"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversation", ["Kilogram to Gram", "Gram to Kilogram","Gram to Miligram","Miligram to Gram","Miligram to Microgram","Microgram to Miligram"])
        
elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversation", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"Converted Value: {result}")
    


