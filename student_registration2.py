import streamlit as st
import pandas as pd

# Apply custom CSS for a dark theme
st.markdown("""
    <style>
        body { background-color: #1E1E1E; color: #FFFFFF; }
        .stButton>button { background-color: #4CAF50; color: white; }
        .stTextInput>div>div>input { background-color: #262730; color: white; }
        .stNumberInput>div>div>input { background-color: #262730; color: white; }
        .stTable { background-color: #262730; color: white; }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for persistent storage
if "students" not in st.session_state:
    st.session_state.students = {}  # Dictionary to store student records
if "student_ids" not in st.session_state:
    st.session_state.student_ids = []  # List to track student IDs

# Streamlit UI
st.title("🎓 Student Registration System")

# Sidebar menu
menu = st.sidebar.radio("📌 Navigation", ["Add Student", "View Students", "Search Student", "Update Student", "Delete Student", "Import/Export Data"])

# Display total student count
st.sidebar.markdown(f"👥 **Total Students:** {len(st.session_state.students)}")

# 1. Add Student Record
if menu == "Add Student":
    st.subheader("📝 Add Student Record")
    student_id = st.text_input("📌 Enter Student ID")
    name = st.text_input("🧑 Enter Student Name")
    age = st.number_input("📅 Enter Student Age", min_value=1, max_value=100, step=1)
    grade = st.text_input("🎓 Enter Student Grade")

    if st.button("✅ Add Student"):
        if student_id and name and grade:
            if student_id in st.session_state.students:
                st.error("⚠️ Student ID already exists!")
            else:
                st.session_state.students[student_id] = {'name': name, 'age': age, 'grade': grade}
                st.session_state.student_ids.append(student_id)
                st.success("🎉 Student added successfully!")
        else:
            st.error("❌ Please fill all the details.")

# 2. View All Students
elif menu == "View Students":
    st.subheader("📋 All Student Records")
    if not st.session_state.students:
        st.warning("⚠️ No students found.")
    else:
        student_list = [{"ID": sid, "Name": st.session_state.students[sid]['name'], 
                         "Age": st.session_state.students[sid]['age'], 
                         "Grade": st.session_state.students[sid]['grade']} 
                        for sid in st.session_state.student_ids]
        st.table(student_list)

# 3. Search Student
elif menu == "Search Student":
    st.subheader("🔍 Search Student Record")
    student_id = st.text_input("🔎 Enter Student ID to Search")
    if st.button("🔍 Search"):
        if student_id in st.session_state.students:
            student = st.session_state.students[student_id]
            st.write(f"**🆔 ID:** {student_id}")
            st.write(f"**🧑 Name:** {student['name']}")
            st.write(f"**📅 Age:** {student['age']}")
            st.write(f"**🎓 Grade:** {student['grade']}")
        else:
            st.error("❌ Student not found.")

# 4. Update Student Information
elif menu == "Update Student":
    st.subheader("✏️ Update Student Record")
    student_id = st.text_input("✍️ Enter Student ID to Update")
    if student_id in st.session_state.students:
        name = st.text_input("🧑 Enter New Name", value=st.session_state.students[student_id]['name'])
        age = st.number_input("📅 Enter New Age", min_value=1, max_value=100, step=1, 
                              value=st.session_state.students[student_id]['age'])
        grade = st.text_input("🎓 Enter New Grade", value=st.session_state.students[student_id]['grade'])

        if st.button("🔄 Update Student"):
            st.session_state.students[student_id] = {'name': name, 'age': age, 'grade': grade}
            st.success("✅ Student information updated successfully!")
    elif student_id:
        st.error("❌ Student not found.")

# 5. Delete Student Record
elif menu == "Delete Student":
    st.subheader("🗑️ Delete Student Record")
    student_id = st.text_input("⚠️ Enter Student ID to Delete")
    if st.button("🚨 Delete Student"):
        if student_id in st.session_state.students:
            del st.session_state.students[student_id]
            st.session_state.student_ids.remove(student_id)
            st.success("🗑️ Student record deleted successfully!")
        else:
            st.error("❌ Student not found.")

# 6. Import/Export Data
elif menu == "Import/Export Data":
    st.subheader("📂 Import/Export Student Data")

    # Export Data as CSV
    if st.button("⬇️ Export to CSV"):
        if st.session_state.students:
            df = pd.DataFrame([{"ID": sid, **st.session_state.students[sid]} for sid in st.session_state.student_ids])
            df.to_csv("students.csv", index=False)
            st.success("✅ Data exported successfully! (File: students.csv)")
        else:
            st.warning("⚠️ No data to export!")

    # Import Data from CSV
    uploaded_file = st.file_uploader("📤 Upload CSV to Import Students", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        for _, row in df.iterrows():
            student_id = str(row["ID"])
            st.session_state.students[student_id] = {'name': row["name"], 'age': int(row["age"]), 'grade': row["grade"]}
            if student_id not in st.session_state.student_ids:
                st.session_state.student_ids.append(student_id)
        st.success("✅ Data imported successfully!")
