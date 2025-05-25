import streamlit as st

st.title('Unit Converter by Yusra')

# Conversion types
conversion_types = ['Temperature', 'Length', 'Weight']
conversion_type = st.selectbox('Select the conversion type', conversion_types)

# Length conversion
if conversion_type == 'Length':
    length_units = ['meters', 'kilometers', 'feet', 'inches', 'centimeters', 'millimeters']
    input_value = st.number_input('Enter the value to convert', min_value=0.0, format='%.2f')
    from_unit = st.selectbox('From unit', length_units)
    to_unit = st.selectbox('To unit', length_units)

    # Conversion dictionary
    length_conversion = {
        'meters': 1,
        'kilometers': 1000,
        'feet': 0.3048,
        'inches': 0.0254,
        'centimeters': 0.01,
        'millimeters': 0.001  # Fixed: was 1000, should be 0.001
    }

    if st.button('Convert'):
        result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')

# Weight conversion
elif conversion_type == 'Weight':
    weight_units = ['kilograms', 'grams', 'pounds', 'ounces']
    input_value = st.number_input('Enter the value to convert', min_value=0.0, format='%.2f')
    from_unit = st.selectbox('From unit', weight_units)
    to_unit = st.selectbox('To unit', weight_units)

    # Conversion dictionary
    weight_conversion = {
        'kilograms': 1,
        'grams': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }

    if st.button('Convert'):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')

# Temperature conversion
elif conversion_type == 'Temperature':
    temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']
    input_value = st.number_input('Enter the value to convert', format='%.2f')  # Removed min_value to allow negative temperatures
    from_unit = st.selectbox('From unit', temperature_units)
    to_unit = st.selectbox('To unit', temperature_units)

    def convert_temperature(value, from_u, to_u):
        # Convert to Celsius first
        if from_u == 'Celsius':
            celsius = value
        elif from_u == 'Fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_u == 'Kelvin':
            celsius = value - 273.15

        # Convert from Celsius to target unit
        if to_u == 'Celsius':
            result = celsius
        elif to_u == 'Fahrenheit':
            result = (celsius * 9/5) + 32
        elif to_u == 'Kelvin':
            result = celsius + 273.15
            
        return result

    if st.button('Convert'):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')