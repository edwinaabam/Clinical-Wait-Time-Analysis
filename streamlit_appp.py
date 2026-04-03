import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Pure Life Hospital: Time Intelligence Analysis", 
                   page_icon= "🩺",
                   layout="wide")

# --- 1. TITLE BANNER ---
# --- 1. TITLE BANNER (Slim Version) ---
st.markdown("""
    <div style="background-color:#04784D; padding: 10px 20px; border-radius:10px; margin-bottom:15px; border: 1px solid #dcdcdc;">
    <h2 style="color:white; text-align:center; font-family:sans-serif; margin:0; line-height:1.2;">Pure Life Time Intelligence Dashboard</h2>
    <p style="color:white; text-align:center; font-size:16px; margin:2px 0 0 0;">Clinical Flow & Wait Time Operational Analysis</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. TABS ---
tabs = st.tabs(["📖 About the Project", "🔗 Live Power BI", "Report Analysis", ])

# --- TAB 1: ABOUT THE PROJECT ---
with tabs[0]:
    #st.title("Pure Life Hospital: Time Intelligence Analysis")
    
    st.header("Project Overview")
    st.write("""
    Pure Life Hospital is a multi-departmental healthcare provider spanning across five departments: 
    **Cardiology, Emergency, Orthopedics, Outpatient, and Pediatrics**. 
    This project utilizes Electronic Health Record (EHR) data to track 'Time Intelligence,' 
    monitoring the entire patient journey from arrival to discharge to optimize throughput.
    """)

    st.header("Problem Statement")
    st.write("""
    Pure Life Hospital is facing a critical operational breakdown where excessive patient wait times 
    are undermining clinical outcomes and revenue. Patients spend the majority of their visit 
    waiting (**non-value-added time**) rather than receiving care. 
    
    Key issues include:
    * Staffing levels failing to align with peak demand windows.
    * High 'Left Without Being Seen' (LWBS) rates.
    * Low patient satisfaction (currently 19.7%).
    """)

    st.header("Key Objectives")
    st.markdown("""
    - Identify department-level bottlenecks (specifically in **Emergency**).
    - Reduce the **Length of Stay (LOS)** without increasing infrastructure costs.
    - Align staffing with peak demand hours to reduce LWBS.
    """)


# --- TAB 3: LIVE POWER BI ---
with tabs[1]:
    #st.header("Interactive Clinical Dashboard")
    
    # Replicating the requested KPIs for consistency on the Live page
    #k1, k2, k3, k4, k5 = st.columns(5)
    #k1.metric("Avg LOS", "145 min")
    #k2.metric("Avg Wait for Doctor", "55 min")
    #k3.metric("Avg Consultation", "45 min")
    #k4.metric("LWBS Rate %", "3.1%")
    #k5.metric("Satisfaction Rate %", "19.7%")
    
    #st.divider()

    # Replace the URL below with your actual Power BI Embed Link
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiYzc5ODk1OWYtYTcxMS00MDAxLTkzYTYtNDI3YzBkM2FlY2NkIiwidCI6IjhkMWE2OWVjLTAzYjUtNDM0NS1hZTIxLWRhZDExMmY1ZmI0ZiIsImMiOjN9"
    
    components.iframe(power_bi_url, height=800, scrolling=True)

# --- TAB 2: DASHBOARD PAGE ---
with tabs[2]:
    #st.title("Clinical Wait Time Intelligence Dashboard")
    
    # Top Level Metrics (KPIs)
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Avg LOS", "145 min")
    col2.metric("Avg Wait for Doctor", "55 min")
    col3.metric("Avg Consultation", "45 min")
    col4.metric("LWBS Rate %", "3.1%", delta="-0.5%", delta_color="inverse")
    col5.metric("Satisfaction Rate %", "19.7%", delta="7.3%", delta_color="normal")

    st.divider()

    # Main Layout
    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.subheader("Departmental Performance")
        st.info("Emergency is the primary constraint with a LOS of ~205 mins.")
        # Displaying the dashboard image
        st.image("dashboardreport.png", caption="Pure Life Hospital Dashboard Analysis", use_container_width=True)

    with right_col:
        st.subheader("Key Findings & Insights")
        
        with st.expander("Wait Time & Satisfaction Trends"):
            st.write("""
            - **Wait Times:** Peaked in Feb (~58m) and improved by June (~52m).
            - **Satisfaction:** Although it rose to 27% in June, it remains critically low. 
            - **The Gap:** Lower wait times help, but service quality and communication are likely secondary factors.
            """)
            
        with st.expander("The Emergency Bottleneck"):
            st.write("""
            - **Emergency LOS:** ~205 minutes.
            - **Emergency Wait:** ~85-90 minutes.
            - This department is the main driver of 'non-value-added' time.
            """)

        with st.expander("Heatmap Analysis (Peak Hours)"):
            st.write("""
            The heatmap indicates high wait times (80+ mins) during mid-day windows 
            (Hours 10-13) particularly on **Saturdays and Sundays**.
            """) 

# --- SIDEBAR ---
#st.sidebar.header("Filter Analytics")
#st.sidebar.multiselect("Select Department", ["Cardiology", "Emergency", "Orthopedics", "Outpatient", "Pediatrics"], default=["Emergency"])
#st.sidebar.markdown("---")
#st.sidebar.write("Developed by: **Edwina Abam**")