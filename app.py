import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# --- PAGE CONFIGURATION & STYLING ---
# Set the page to wide mode for a better layout
st.set_page_config(layout="wide")

# Custom CSS for a more attractive and clean look
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f2f6; /* A light grey background for a clean look */
        }
        .main-container {
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        h1, h2, h3 {
            color: #2e7d32;
        }
    </style>
""", unsafe_allow_html=True)

# --- USER AUTHENTICATION & CONFIGURATION ---
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("config.yaml not found. Please make sure the file is in your project directory.")
    st.stop()

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

# --- LOGIN & APPLICATION LOGIC ---
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
elif authentication_status:
    # This block runs only when a user is authenticated
    with st.sidebar:
        st.write(f"Welcome, **{name}**!")
        authenticator.logout('Logout', 'sidebar')

    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("College Web Portal")

    # Student Dashboard
    if username in ["j_doe", "s_williams"]:
        st.header("Student Dashboard 🎓")

        st.subheader("Your Courses")
        col1, col2 = st.columns(2)
        with col1:
            st.info("💡 **Course 101: Intro to CS**\n\nLecturer: Alex Smith")
            st.progress(0.75, text="Progress: 75%")
        with col2:
            st.info("💡 **Course 201: Data Structures**\n\nLecturer: Jane Doe")
            st.progress(0.40, text="Progress: 40%")

        st.subheader("Upcoming Assignments")
        with st.expander("Click to see your assignments"):
            st.dataframe({
                'Assignment': ['Homework 1', 'Project 1'],
                'Due Date': ['2025-10-01', '2025-11-15'],
                'Status': ['Pending', 'Submitted']
            })

    # Lecturer Dashboard
    elif username == "a_smith":
        st.header("Lecturer Dashboard 🧑‍🏫")

        st.subheader("Course Management")
        selected_course = st.selectbox(
            "Select a course to manage:",
            ["Course 101: Intro to CS", "Course 201: Data Structures"]
        )

        c1, c2 = st.columns(2)
        c1.metric(label="Total Students", value="35")
        c2.metric(label="Average Grade", value="B+")

        st.subheader("Student Grades")
        student_data = {
            'Student Name': ['John Doe', 'Sally Williams'],
            'Student ID': ['12345', '67890'],
            'Assignment 1 Grade': ['A', 'B'],
            'Final Grade': ['A-', 'B+']
        }
        st.dataframe(student_data)

        st.subheader("Upload Materials")
        with st.form("upload_form"):
            file = st.file_uploader("Upload a file for your students:")
            st.form_submit_button("Upload File")
    
    st.markdown('</div>', unsafe_allow_html=True)
