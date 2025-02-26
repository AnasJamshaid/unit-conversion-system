# The Conversion Compass 🧭

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-orange?style=flat-square)](https://conversioncompass-by-muhammadanasjamshaid.streamlit.app/)
[![GitHub Stars](https://img.shields.io/github/stars/your-github-username/your-repo-name?style=social)](https://github.com/your-github-username/your-repo-name)
[![GitHub Forks](https://img.shields.io/github/forks/your-github-username/your-repo-name?style=social)](https://github.com/your-github-username/your-repo-name)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  <!-- Replace MIT with your license -->

## Description

The Conversion Compass is a Streamlit web application designed to make unit conversions easy and accessible for everyone.  Whether you're a student, professional, or just need to quickly convert between units, this tool provides a user-friendly interface and accurate results. It handles a wide variety of unit types, including length, mass, temperature, area, digital storage, speed, time, pressure, volume, and power.  The app also features an AI assistant (Beta) powered by Google's Gemini model to help with more complex conversion questions and calculations.

## Features

*   **Wide Range of Unit Types:** Supports conversions for length, mass, temperature, area, digital storage, speed, time, pressure, volume, and power.
*   **Accurate Conversions:**  Uses precise conversion factors for reliable results.
*   **User-Friendly Interface:**  Easy to navigate and use, even for those unfamiliar with unit conversions.
*   **AI Assistant (Beta):**  Powered by Google's Gemini model, the AI assistant can answer questions related to unit conversions and perform calculations.
*   **Clear Conversion Guidance:** Provides explanations of the formulas used in the conversions.
*   **Dark Theme:**  A visually appealing dark theme for comfortable use in any environment.
*   **Responsive Design:**  Works well on various screen sizes (desktop, tablet, mobile).

## Usage

1.  **Select a Category:**  Choose the type of unit you want to convert (e.g., Length, Mass, Temperature) from the "Choose a Category" dropdown.
2.  **Select Units:** Specify the unit to convert from in the "Convert From" dropdown and the unit to convert to in the "Convert To" dropdown.
3.  **Enter Value:** Enter the numerical value you want to convert in the input field.
4.  **Click "Chart the Course!":**  Press the button to perform the conversion.  The result and the conversion formula will be displayed.
5.  **AI Assistant:**  Use the AI assistant at the bottom of the page to ask more complex questions or get help with specific conversions.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-github-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your Google Gemini API key:**

    *   Obtain an API key from [Google AI Studio](https://makersuite.google.com/).
    *   **Important:** Do *not* commit your API key directly to the repository.
    *   Streamlit:  Set the API key as a Streamlit secret.  Go to your Streamlit Cloud app's settings and add a secret named `"GEMINI_API_KEY"` with your API key as the value.

5.  **Run the Streamlit app:**

    ```bash
    streamlit run your_app_name.py
    ```

## Contributing

Contributions are welcome!  If you'd like to contribute to the project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, descriptive commit messages.
4.  Submit a pull request.

Please ensure that your code adheres to the project's coding style and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Creator

This application was created by **Muhammad Anas Jamshaid**.

*   [GitHub](https://github.com/AnasJamshaid)
*   [LinkedIn](https://www.linkedin.com/in/muhammadanasjamshaid/)

## Acknowledgements

*   [Streamlit](https://streamlit.io/) for providing the framework for building the web application.
*   [Google AI](https://ai.google.dev/) for the Gemini model used in the AI assistant.
*   [Icons8](https://icons8.com/) for providing the social media icons.

## Contact

If you have any questions or suggestions, feel free to contact me through my GitHub or LinkedIn profiles.