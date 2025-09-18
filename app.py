import streamlit as st
import streamlit_authenticator as stauth

# Load config and authenticate (same as before)
# ... [Code from previous response] ...

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    # Use a sidebar for logout button and navigation
    with st.sidebar:
        st.write(f"Welcome, {name}!")
        authenticator.logout('Logout', 'sidebar')
    
    st.title("College Web Portal")

    # Student Dashboard
    if username in ["j_doe", "s_williams"]:
        st.header("Student Dashboard 🎓")
        
        # UI for students
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
        
        # Display metrics for the selected course
        c1, c2 = st.columns(2)
        c1.metric(label="Total Students", value="35")
        c2.metric(label="Average Grade", value="B+")

        st.subheader("Student Grades")
        # Example data for a dataframe
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

    else:
        st.warning("You do not have a defined role. Please contact support.")

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
