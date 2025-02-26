import streamlit as st
import google.generativeai as genai
import logging
import traceback
from PIL import Image


from PIL import Image

with st.sidebar:
    try:
        image = Image.open("./Muhammad Anas Jamshaid.png")
        st.image(image, width=150)
    except FileNotFoundError:
        st.error("Image not found! Please ensure 'Muhammad Anas Jamshaid.png' is in the correct directory.")
    st.header("About the Creator")

    
# --- Setup Logging ---
logging.basicConfig(level=logging.ERROR)

# --- Configuration ---
PAGE_TITLE = "The Conversion Compass"  # New Title
PAGE_ICON = "🧭"  # New Icon
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# --- Sidebar Content ---
with st.sidebar:
    st.image("./Muhammad Anas Jamshaid.png", width=150)  # Replace with your image URL
    st.header("About the Creator")  # Sidebar Header
    st.markdown(
        """
        Hi, I'm **Muhammad Anas Jamshaid**! I developed this Conversion Compass to make unit conversions effortless for everyone. 
        Whether you're a student, professional, or just curious, I hope this tool simplifies your calculations.
        """
    )  # Short description of the app and you

    st.markdown("---")  # Divider

    st.subheader("Connect with Me")
    # Social Media Icons with Links
    st.markdown(
        """
        <div style="display: flex; gap: 10px;">
            <a href="https://github.com/AnasJamshaid" target="_blank">
                <img src="https://img.icons8.com/ios-filled/50/FFFFFF/github.png" alt="GitHub" width="30">
            </a>
            <a href="https://www.linkedin.com/in/muhammadanasjamshaid/" target="_blank">
                <img src="https://img.icons8.com/ios-filled/50/FFFFFF/linkedin.png" alt="LinkedIn" width="30">
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")  # Divider

    st.subheader("More Information")
    st.markdown(
        """
        - Explore a wide range of unit categories.
        - Get accurate and reliable conversions.
        - Use the AI Assistant for extra help.
        - Contact me with suggestions for new features!
        """
    )  # Add more useful information

# --- Unit Conversion Functions ---
# (Keep all your existing conversion functions here)

# --- Streamlit App ---

# Dark Theme CSS Styling
st.markdown(
    """
    <style>
    /* General app styling */
    .stApp {
        background-color: #0E1117;  /* Dark background */
        color: #FFFFFF;  /* White text */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Title styling */
    h1 {
        color: #4CAF50; /* Green */
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 0.5em;
        letter-spacing: -1px;
    }

    /* Subheader styling */
    h2 {
        color: #4CAF50; /* Green */
        font-size: 1.75em;
        margin-top: 1em;
        margin-bottom: 0.5em;
    }

    /* Markdown text styling */
    .stMarkdown {
        font-size: 1.1em;
        line-height: 1.6;
        color: #FFFFFF; /* White text */
    }

    /* Selectbox and number input labels */
    label {
        font-weight: 500;
        color: #FFFFFF; /* White text */
    }

    /* Input elements */
    .stSelectbox>div>div>button,
    .stNumberInput>div>div>input {
        background-color: #1E1E1E; /* Dark input background */
        border-color: #333333; /* Dark border */
        color: #FFFFFF; /* White text */
        border-radius: 0.5rem;
        padding: 0.5rem 0.75rem;
        transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    }

    /* Button styling */
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.75rem 1.5rem;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.2s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }

    /* Success message styling */
    .success {
        color: #d4edda; /* Light green */
        background-color: #155724; /* Dark green */
        border: 1px solid #c3e6cb;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 4px;
    }

    /* Info message styling */
    .info {
        color: #d1ecf1; /* Light blue */
        background-color: #0c5460; /* Dark blue */
        border: 1px solid #bee5eb;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 4px;
    }

    /* Error message styling */
    .error {
        color: #f8d7da; /* Light red */
        background-color: #721c24; /* Dark red */
        border: 1px solid #f5c6cb;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 4px;
    }

    /* Chat message styles */
    .stChatMessage {
        border-radius: 8px;
        padding: 8px 12px;
        margin-bottom: 8px;
    }

    .stChatMessage[data-streamlit=true] {
        background-color: #1E1E1E; /* Dark background for user messages */
        border: 1px solid #333333;
        color: #FFFFFF; /* White text */
    }

    .stChatMessage:not([data-streamlit=true]) {
        background-color: #2E2E2E; /* Darker background for assistant messages */
        color: #FFFFFF; /* White text */
    }

    /* Scrollable chat area */
    .chat-container {
        height: 400px; /* Fixed height for scrollable area */
        overflow-y: auto; /* Enable vertical scrolling */
        padding: 10px;
        border: 1px solid #333333;
        border-radius: 8px;
        margin-bottom: 15px;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1E1E1E; /* Dark sidebar background */
    }

    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg h5, .css-1d391kg h6 {
        color: #4CAF50; /* Green headings */
    }

    .css-1d391kg p {
        color: #FFFFFF; /* White text */
    }

    </style>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# --- Rest of the Code ---
# (Keep all your existing app logic here)


# --- Unit Conversion Functions ---
def meters_to_centimeters(meters):
    try:
        result = meters * 100
        return result, "Multiply meters by 100."
    except Exception as e:
        logging.error(f"Error in meters_to_centimeters: {e}")
        return None, "Error during conversion"

def centimeters_to_meters(centimeters):
    return centimeters / 100, "Divide centimeters by 100."

def meters_to_feet(meters):
    return meters * 3.28084, "Multiply meters by 3.28084."

def feet_to_meters(feet):
    return feet / 3.28084, "Divide feet by 3.28084."

def miles_to_kilometers(miles):
    return miles * 1.60934, "Multiply miles by 1.60934."

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934, "Divide kilometers by 1.60934."

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462, "Multiply kilograms by 2.20462."

def pounds_to_kilograms(pounds):
    return pounds / 2.20462, "Divide pounds by 2.20462."

def grams_to_ounces(grams):
    return grams * 0.035274, "Multiply grams by 0.035274."

def ounces_to_grams(ounces):
    return ounces / 0.035274, "Divide ounces by 0.035274."

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32, "Multiply Celsius by 9/5 and add 32."

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9, "Subtract 32 from Fahrenheit and multiply by 5/9."

def celsius_to_kelvin(celsius):
    return celsius + 273.15, "Add 273.15 to Celsius."

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15, "Subtract 273.15 from Kelvin."

def square_meters_to_square_feet(square_meters):
    return square_meters * 10.764, "Multiply square meters by 10.764."

def square_feet_to_square_meters(square_feet):
    return square_feet / 10.764, "Divide square feet by 10.764."

def bytes_to_kilobytes(bytes_value):
    return bytes_value / 1024, "Divide bytes by 1024."

def kilobytes_to_bytes(kilobytes_value):
    return kilobytes_value * 1024, "Multiply kilobytes by 1024."

def megabytes_to_gigabytes(megabytes):
    return megabytes / 1024, "Divide megabytes by 1024."

def gigabytes_to_megabytes(gigabytes):
    return gigabytes * 1024, "Multiply gigabytes by 1024."

def kmh_to_mph(kmh):
    return kmh * 0.621371, "Multiply km/h by 0.621371."

def mph_to_kmh(mph):
    return mph / 0.621371, "Divide mph by 0.621371."

def seconds_to_minutes(seconds):
    return seconds / 60, "Divide seconds by 60."

def minutes_to_seconds(minutes):
    return minutes * 60, "Multiply minutes by 60."

def hours_to_minutes(hours):
    return hours * 60, "Multiply hours by 60."

def minutes_to_hours(minutes):
    return minutes / 60, "Divide minutes by 60."

def pascals_to_psi(pascals):
    return pascals * 0.000145038, "Multiply Pascals by 0.000145038."

def psi_to_pascals(psi):
    return psi / 0.000145038, "Divide PSI by 0.000145038."

# Volume
def liters_to_gallons(liters):
    return liters * 0.264172, "Multiply liters by 0.264172"
def gallons_to_liters(gallons):
    return gallons / 0.264172, "Divide gallons by 0.264172"

# Power
def watts_to_horsepower(watts):
    return watts * 0.00134102, "Multiply watts by 0.00134102"
def horsepower_to_watts(horsepower):
    return horsepower / 0.00134102, "Divide horsepower by 0.00134102"

# --- Generic Conversion Function ---
def no_conversion(value):
    return value, "No conversion needed (same units)."

# --- Expanded List of Units ---
UNIT_TYPES = {
    "Length": ["Meter", "Centimeter", "Feet", "Kilometer", "Mile", "Inch", "Yard"],
    "Mass": ["Kilogram", "Pound", "Gram", "Ounce", "Ton"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Area": ["Square Meter", "Square Feet", "Square Kilometer", "Square Mile"],
    "Digital Storage": ["Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"],
    "Speed": ["Kilometers per hour", "Miles per hour", "Meters per second"],
    "Time": ["Second", "Minute", "Hour", "Day", "Week"],
    "Pressure": ["Pascal", "PSI", "Atmosphere", "Bar"],
    "Volume": ["Liter", "Gallon", "Cubic Meter", "Cubic Feet"],
    "Power": ["Watt", "Horsepower"]
}

# --- Expanded Conversion Function Map ---
CONVERSION_FUNCTIONS = {
    ("Length", "Meter", "Centimeter"): meters_to_centimeters,
    ("Length", "Centimeter", "Meter"): centimeters_to_meters,
    ("Length", "Meter", "Feet"): meters_to_feet,
    ("Length", "Feet", "Meter"): feet_to_meters,
    ("Length", "Mile", "Kilometer"): miles_to_kilometers,
    ("Length", "Kilometer", "Mile"): kilometers_to_miles,
    ("Length", "Meter", "Inch"): lambda x: (x * 39.3701, "Multiply meters by 39.3701"),
    ("Length", "Inch", "Meter"): lambda x: (x / 39.3701, "Divide inches by 39.3701"),
    ("Length", "Meter", "Yard"): lambda x: (x * 1.09361, "Multiply meters by 1.09361"),
    ("Length", "Yard", "Meter"): lambda x: (x / 1.09361, "Divide yards by 1.09361"),
    ("Length", "Meter", "Meter"): no_conversion,
    ("Length", "Centimeter", "Centimeter"): no_conversion,
    ("Length", "Feet", "Feet"): no_conversion,
    ("Length", "Kilometer", "Kilometer"): no_conversion,
    ("Length", "Mile", "Mile"): no_conversion,
    ("Length", "Inch", "Inch"): no_conversion,
    ("Length", "Yard", "Yard"): no_conversion,

    ("Mass", "Kilogram", "Pound"): kilograms_to_pounds,
    ("Mass", "Pound", "Kilogram"): pounds_to_kilograms,
    ("Mass", "Gram", "Ounce"): grams_to_ounces,
    ("Mass", "Ounce", "Gram"): ounces_to_grams,
    ("Mass", "Kilogram", "Ton"): lambda x: (x * 0.00110231, "Multiply kg by 0.00110231 (metric ton)"),
    ("Mass", "Ton", "Kilogram"): lambda x: (x * 1000, "Multiply tons by 1000"),
    ("Mass", "Kilogram", "Kilogram"): no_conversion,
    ("Mass", "Pound", "Pound"): no_conversion,
    ("Mass", "Gram", "Gram"): no_conversion,
    ("Mass", "Ounce", "Ounce"): no_conversion,
    ("Mass", "Ton", "Ton"): no_conversion,

    ("Temperature", "Celsius", "Fahrenheit"): celsius_to_fahrenheit,
    ("Temperature", "Fahrenheit", "Celsius"): fahrenheit_to_celsius,
    ("Temperature", "Celsius", "Kelvin"): celsius_to_kelvin,
    ("Temperature", "Kelvin", "Celsius"): kelvin_to_celsius,
    ("Temperature", "Celsius", "Celsius"): no_conversion,
    ("Temperature", "Fahrenheit", "Fahrenheit"): no_conversion,
    ("Temperature", "Kelvin", "Kelvin"): no_conversion,

    ("Area", "Square Meter", "Square Feet"): square_meters_to_square_feet,
    ("Area", "Square Feet", "Square Meter"): square_feet_to_square_meters,
    ("Area", "Square Kilometer", "Square Mile"): lambda x: (x * 0.386102, "Multiply sq km by 0.386102"),
    ("Area", "Square Mile", "Square Kilometer"): lambda x: (x / 0.386102, "Divide sq mi by 0.386102"),
    ("Area", "Square Meter", "Square Meter"): no_conversion,
    ("Area", "Square Feet", "Square Feet"): no_conversion,
    ("Area", "Square Kilometer", "Square Kilometer"): no_conversion,
    ("Area", "Square Mile", "Square Mile"): no_conversion,

    ("Digital Storage", "Byte", "Kilobyte"): bytes_to_kilobytes,
    ("Digital Storage", "Kilobyte", "Byte"): kilobytes_to_bytes,
    ("Digital Storage", "Megabyte", "Gigabyte"): megabytes_to_gigabytes,
    ("Digital Storage", "Gigabyte", "Megabyte"): gigabytes_to_megabytes,
    ("Digital Storage", "Gigabyte", "Terabyte"): lambda x: (x / 1024, "Divide GB by 1024"),
    ("Digital Storage", "Terabyte", "Gigabyte"): lambda x: (x * 1024, "Multiply TB by 1024"),
    ("Digital Storage", "Byte", "Byte"): no_conversion,
    ("Digital Storage", "Kilobyte", "Kilobyte"): no_conversion,
    ("Digital Storage", "Megabyte", "Megabyte"): no_conversion,
    ("Digital Storage", "Gigabyte", "Gigabyte"): no_conversion,
    ("Digital Storage", "Terabyte", "Terabyte"): no_conversion,

    ("Speed", "Kilometers per hour", "Miles per hour"): kmh_to_mph,
    ("Speed", "Miles per hour", "Kilometers per hour"): mph_to_kmh,
    ("Speed", "Kilometers per hour", "Meters per second"): lambda x: (x * 0.277778, "Multiply km/h by 0.277778"),
    ("Speed", "Meters per second", "Kilometers per hour"): lambda x: (x / 0.277778, "Divide m/s by 0.277778"),
    ("Speed", "Kilometers per hour", "Kilometers per hour"): no_conversion,
    ("Speed", "Miles per hour", "Miles per hour"): no_conversion,
    ("Speed", "Meters per second", "Meters per second"): no_conversion,

    ("Time", "Second", "Minute"): seconds_to_minutes,
    ("Time", "Minute", "Second"): minutes_to_seconds,
    ("Time", "Hour", "Minute"): hours_to_minutes,
    ("Time", "Minute", "Hour"): minutes_to_hours,
    ("Time", "Day", "Hour"): lambda x: (x * 24, "Multiply days by 24"),
    ("Time", "Hour", "Day"): lambda x: (x / 24, "Divide hours by 24"),
    ("Time", "Week", "Day"): lambda x: (x * 7, "Multiply weeks by 7"),
    ("Time", "Day", "Week"): lambda x: (x / 7, "Divide days by 7"),
    ("Time", "Second", "Second"): no_conversion,
    ("Time", "Minute", "Minute"): no_conversion,
    ("Time", "Hour", "Hour"): no_conversion,
    ("Time", "Day", "Day"): no_conversion,
    ("Time", "Week", "Week"): no_conversion,

    ("Pressure", "Pascal", "PSI"): pascals_to_psi,
    ("Pressure", "PSI", "Pascal"): psi_to_pascals,
    ("Pressure", "Pascal", "Atmosphere"): lambda x: (x * 9.86923e-6, "Multiply Pascals by 9.86923e-6"),
    ("Pressure", "Atmosphere", "Pascal"): lambda x: (x * 101325, "Multiply Atmospheres by 101325"),
    ("Pressure", "Pascal", "Pascal"): no_conversion,
    ("Pressure", "Bar", "Pascal"): lambda x: (x * 100000, "Multiply Bar by 100000"),
    ("Pressure", "PSI", "PSI"): no_conversion,
    ("Pressure", "Atmosphere", "Atmosphere"): no_conversion,
    ("Pressure", "Bar", "Bar"): no_conversion,

    ("Volume", "Liter", "Gallon"): liters_to_gallons,
    ("Volume", "Gallon", "Liter"): gallons_to_liters,
    ("Volume", "Liter", "Cubic Meter"): lambda x: (x / 1000, "Divide Liters by 1000"),
    ("Volume", "Cubic Meter", "Liter"): lambda x: (x * 1000, "Multiply Cubic Meters by 1000"),
    ("Volume", "Liter", "Cubic Feet"): lambda x: (x * 0.0353147, "Multiply Liters by 0.0353147"),
    ("Volume", "Cubic Feet", "Liter"): lambda x: (x / 0.0353147, "Divide Cubic Feet by 0.0353147"),
    ("Volume", "Liter", "Liter"): no_conversion,
    ("Volume", "Gallon", "Gallon"): no_conversion,
    ("Volume", "Cubic Meter", "Cubic Meter"): no_conversion,
    ("Volume", "Cubic Feet", "Cubic Feet"): no_conversion,

    ("Power", "Watt", "Horsepower"): watts_to_horsepower,
    ("Power", "Horsepower", "Watt"): horsepower_to_watts,
    ("Power", "Watt", "Watt"): no_conversion,
    ("Power", "Horsepower", "Horsepower"): no_conversion,
}

# --- Streamlit App ---

# Modern Dark Theme CSS Styling
st.markdown(
    """
    <style>
    /* General app styling */
    .stApp {
        background-color: #121212; /* Darker gray background */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #ffffff; /* Light text color */
    }

    /* Sidebar styling */
    .stSidebar {
        background-color: #212121; /* Darker sidebar */
        color: #ffffff;
    }

    /* Header styling */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff; /* Light heading color */
    }

    /* Link styling */
    a {
        color: #80cbc4; /* Teal for links */
    }

    /* Markdown text styling */
    .stMarkdown {
        color: #d3d3d3; /* Light gray for markdown text */
    }

    /* Input elements */
    .stSelectbox>div>div>button,
    .stNumberInput>div>div>input {
        background-color: #333333; /* Dark gray input background */
        color: #ffffff;
        border-color: #666666;
    }

    /* Button styling */
    .stButton>button {
        background-color: #6a1b9a; /* Dark purple button */
        color: #ffffff;
        border: none;
        border-radius: 0.5rem;
        padding: 0.75rem 1.5rem;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.2s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #4a148c; /* Darker purple on hover */
    }

    /* Success message styling */
    .success {
        color: #b9f6ca; /* Light green */
        background-color: #1b5e20; /* Dark green */
        border: 1px solid #69f0ae;
    }

    /* Info message styling */
    .info {
        color: #80d8ff; /* Light blue */
        background-color: #0d47a1; /* Dark blue */
        border: 1px solid #82b1ff;
    }

    /* Error message styling */
    .error {
        color: #ffdde0; /* Light red */
        background-color: #b71c1c; /* Dark red */
        border: 1px solid #ef9a9a;
    }

    /* Chat message styles */
    .stChatMessage {
        border-radius: 8px;
        padding: 8px 12px;
        margin-bottom: 8px;
    }

    .stChatMessage[data-streamlit=true] {
        background-color: #424242; /* Darker gray for user messages */
        border: 1px solid #616161;
        color: #eceff1; /* Light gray text */
    }

    .stChatMessage:not([data-streamlit=true]) {
        background-color: #33691e; /* Darker green for assistant messages */
        color: #b2ff59; /* Lime text */
    }

    /* Scrollable chat area */
    .chat-container {
        height: 400px; /* Fixed height for scrollable area */
        overflow-y: auto; /* Enable vertical scrolling */
        padding: 10px;
        border: 1px solid #616161; /* Dark gray border */
        border-radius: 8px;
        margin-bottom: 15px;
    }

    
    .fa {
        font-size: 20px; /* Adjust the size as needed */
        margin-right: 5px; /* Space between icon and text */
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" integrity="sha512-9usAa10IRO0HhonpyAIVpjrylPvoDwiPUiKdWk5t3PyolY1cOd4DSE0Ga+ri4AuTroPR5aQvXU9xC6qOPnzFeg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    """,
    unsafe_allow_html=True
)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.markdown("Embark on a journey through a world of units! The Conversion Compass empowers you to effortlessly navigate and translate between various measurement systems.")
st.markdown("Whether you're tackling a tricky recipe, deciphering scientific data, or planning your next adventure, this tool is your trusty guide.")

st.subheader("Start Your Conversion")
st.markdown("Select the category of units you're interested in, then specify the units to convert from and to.")

unit_type = st.selectbox("Choose a Category:", list(UNIT_TYPES.keys()), help="Select the type of units you want to convert.")
unit_from, unit_to = st.columns(2)

with unit_from:
    unit_from_selected = st.selectbox("Convert From:", UNIT_TYPES[unit_type], help="Select the unit you want to convert from.")
with unit_to:
    unit_to_selected = st.selectbox("Convert To:", UNIT_TYPES[unit_type], help="Select the unit you want to convert to.")

value_to_convert = st.number_input(f"Enter {unit_from_selected} Value:", value=1.0, help=f"Enter the numerical value in {unit_from_selected} you want to convert.")

if st.button("Chart the Course!"):  # More evocative button text
    # --- Conversion Logic ---
    conversion_key = (unit_type, unit_from_selected, unit_to_selected)
    #st.write(f"Value to convert: {value_to_convert}")  # Debugging - Keep for now
    #st.write(f"Conversion key: {conversion_key}")  # Debugging - Keep for now
    if conversion_key in CONVERSION_FUNCTIONS:
        conversion_function = CONVERSION_FUNCTIONS[conversion_key]
        #st.write(f"Conversion function: {conversion_function}") # Debugging - Keep for now
        try:  # Add try-except block for conversion
            converted_value, formula = conversion_function(value_to_convert)
            st.markdown(f'<p class="success">{value_to_convert} {unit_from_selected} = {converted_value:.2f} {unit_to_selected}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="info">Conversion Guidance: {formula}</p>', unsafe_allow_html=True)  # More friendly label
        except Exception as e:
            st.markdown('<p class="error">An error occurred during conversion.</p>', unsafe_allow_html=True)  # More specific error
            logging.error(f"Conversion error: {e}\n{traceback.format_exc()}")  # Log detailed error

    else:
        st.markdown('<p class="error">Oops! That conversion isn\'t available yet.</p>', unsafe_allow_html=True)

# --- AI Chatbot Section ---
st.markdown("---")
st.subheader("Seek Wisdom from the AI Oracle (Beta)")  # More evocative subheader
st.markdown("Confused? Let our AI assistant guide you! Ask questions about unit relationships, conversion strategies, or even complex calculations.")  # Enhanced description

# Configure the API key
try:  # Try to get API key
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError as e:
    st.error("API key not found in Streamlit secrets. Please configure it.")
    logging.error(f"API Key Error: {e}")  # Log it
    model = None  # Prevent further execution
except Exception as e:
    st.error(f"An error occurred while configuring the API key: {e}")
    logging.error(f"API Key Configuration Error: {e}")  # Log it
    model = None
else:  # Only initialize the model if the API key is successfully loaded
    # Initialize the Generative AI model
    try:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
    except Exception as e:
        st.error(f"Model initialization failed: {str(e)}")
        logging.error(f"Model Initialization Error: {e}\n{traceback.format_exc()}")
        model = None

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to check if the input is calculation-related (Expanded Keywords)
def is_calculation_related(user_input):
    calculation_keywords = [
        # General math terms
        "calculate", "math", "mathematics", "arithmetic", "algebra", "geometry", "trigonometry", "calculus", "statistics",
        "probability",

        # Basic operations
        "add", "addition", "plus", "+",
        "subtract", "subtraction", "minus", "-",
        "multiply", "multiplication", "times", "*", "x",
        "divide", "division", "divided by", "/",
        "sum", "difference", "product", "quotient", "remainder", "modulus", "mod",

        # Advanced operations
        "exponent", "power", "square", "cube", "root", "sqrt", "square root", "cube root",
        "logarithm", "log", "ln", "natural logarithm",
        "factorial", "permutation", "combination",
        "derivative", "integral", "limit", "function", "equation", "inequality",

        # Fractions and decimals
        "fraction", "decimal", "percentage", "percent", "%", "ratio", "proportion",

        # Units and measurements
        "unit", "convert", "conversion", "length", "mass", "weight", "temperature", "area", "volume", "speed", "time",
        "pressure", "energy", "power", "currency",
        "kilometer", "meter", "centimeter", "millimeter", "feet", "inch", "mile", "yard", "nautical mile",
        "kilogram", "gram", "milligram", "pound", "ounce", "ton", "stone", "carat",
        "celsius", "fahrenheit", "kelvin", "rankine",
        "square meter", "square feet", "square kilometer", "square mile", "acre", "hectare",
        "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte", "exabyte",
        "km/h", "mph", "m/s", "knot", "mach",
        "second", "minute", "hour", "day", "week", "month", "year", "decade", "century",
        "pascal", "psi", "atm", "bar", "torr", "mmHg",
        "joule", "calorie", "btu", "kilowatt hour",
        "watt", "horsepower", "kilowatt", "megawatt",
        "usd", "eur", "gbp", "jpy", "cad", "aud", "inr", "cny",

        # Shapes and geometry
        "circle", "triangle", "rectangle", "square", "cube", "sphere", "cylinder", "cone", "pyramid",
        "area", "perimeter", "circumference", "radius", "diameter", "volume", "surface area",

        # Trigonometry
        "sine", "cosine", "tangent", "sin", "cos", "tan", "angle", "degree", "radian",

        # Algebra
        "variable", "constant", "coefficient", "polynomial", "quadratic", "linear", "equation", "solve",

        # Calculus
        "derivative", "integral", "limit", "differentiation", "integration",

        # Statistics and probability
        "mean", "median", "mode", "average", "standard deviation", "variance", "probability", "distribution",

        # Financial math
        "interest", "simple interest", "compound interest", "loan", "mortgage", "investment", "profit", "loss",

        # Symbols
        "+", "-", "*", "/", "=", "<", ">", "≤", "≥", "≠", "≈", "√", "²", "³", "π", "∞",

        # Miscellaneous
        "solve", "compute", "evaluate", "expression", "formula", "theorem", "proof", "graph", "plot",
        "average", "sum", "total", "ratio", "percentage",
    ]
    return any(keyword in user_input.lower() for keyword in calculation_keywords)

# Function to generate a response using Google's Generative AI
def generate_response(user_input):
    if model is None:
        return "The AI converter is currently unavailable. Please try again later."  # More informative message
    try:
        # Check if the input is calculation-related
        if not is_calculation_related(user_input):
            return "I specialize in calculation-based questions, including unit conversions and math problems. Please rephrase your request."  # More specific
        # Generate a response using Google's Generative AI
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        error_message = f"An error occurred while processing your request: {e}"
        logging.error(f"AI Chatbot Error: {error_message}\n{traceback.format_exc()}")  # Log detailed error
        return error_message  # Still return a message to the user


for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.markdown('</div>', unsafe_allow_html=True) #Close scrollable chat area

user_input = st.chat_input("Consult the Oracle with your query...")  # Updated Chat Input Text

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    bot_response = generate_response(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)