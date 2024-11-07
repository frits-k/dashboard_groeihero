import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import matplotlib.pyplot as plt

primaryColor = "#E84A27"          # Orange from logo for primary actions

# Sidebar
st.sidebar.image("logo.jpeg", width=200)  # Display the logo at the top of the sidebar
st.sidebar.title("Groeihero")
st.sidebar.write("Voorbeeld filters:")

# Text Input
st.sidebar.subheader("Text Input")
text_input = st.sidebar.text_input("Enter some text:", "Sample text")

# Text Area
st.sidebar.subheader("Text Area")
text_area = st.sidebar.text_area("Enter longer text here:", "This is a sample longer text area.")

# Number Input
st.sidebar.subheader("Number Input")
number_input = st.sidebar.number_input("Choose a number:", min_value=0, max_value=100, value=25, step=5)

# Date Input
st.sidebar.subheader("Date Input")
date_input = st.sidebar.date_input("Pick a date:", value=datetime.date.today())

# Time Input
st.sidebar.subheader("Time Input")
time_input = st.sidebar.time_input("Pick a time:", value=datetime.time(12, 0))

# Checkbox
st.sidebar.subheader("Checkbox")
checkbox = st.sidebar.checkbox("Check this box")

# Radio Buttons
st.sidebar.subheader("Radio Buttons")
radio_choice = st.sidebar.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])

# Select Box
st.sidebar.subheader("Select Box")
select_box = st.sidebar.selectbox("Choose from the list:", ["Choice 1", "Choice 2", "Choice 3"])

# Multi-Select Box
st.sidebar.subheader("Multi-Select Box")
multi_select = st.sidebar.multiselect("Select multiple options:", ["Choice A", "Choice B", "Choice C"])

# Slider
st.sidebar.subheader("Slider")
slider = st.sidebar.slider("Slide to choose a value:", min_value=0, max_value=100, value=50)

# Range Slider
st.sidebar.subheader("Range Slider")
range_slider = st.sidebar.slider("Select a range:", min_value=0, max_value=100, value=(20, 80))

# File Uploader
st.sidebar.subheader("File Uploader")
file_uploader = st.sidebar.file_uploader("Upload a file:", type=["csv", "txt", "pdf"])

# Color Picker
st.sidebar.subheader("Color Picker")
color_picker = st.sidebar.color_picker("Pick a color:", "#00f900")

# Form with Submit Button
st.sidebar.subheader("Form Example")
with st.sidebar.form(key="example_form"):
    form_text = st.text_input("Enter form text:")
    form_slider = st.slider("Form slider:", 0, 10, 5)
    form_submit = st.form_submit_button("Submit Form")

# Displaying Selected Inputs
st.sidebar.write("### Selected Inputs:")
st.sidebar.write("Text Input:", text_input)
st.sidebar.write("Text Area:", text_area)
st.sidebar.write("Number Input:", number_input)
st.sidebar.write("Date Input:", date_input)
st.sidebar.write("Time Input:", time_input)
st.sidebar.write("Checkbox:", checkbox)
st.sidebar.write("Radio Choice:", radio_choice)
st.sidebar.write("Select Box:", select_box)
st.sidebar.write("Multi-Select:", multi_select)
st.sidebar.write("Slider:", slider)
st.sidebar.write("Range Slider:", range_slider)
st.sidebar.write("Uploaded File:", file_uploader)
st.sidebar.write("Picked Color:", color_picker)
st.sidebar.write("Form Text:", form_text)
st.sidebar.write("Form Slider:", form_slider)
st.sidebar.write("Form Submitted:", form_submit)

# Title
st.title("Groeidashboard")

# Tabs for Different Platforms
tabs = st.tabs(["Google Analytics", "Google Ads", "Facebook", "Instagram", "TikTok", "Catalogus"])

# Content for Google Analytics Tab
with tabs[0]:
    st.header("Google Analytics")

    # 1. Bounce Rate Visualization using Plotly
    st.subheader("Bounce Rate over de Afgelopen Week")
    dates = pd.date_range(end=datetime.date.today(), periods=7)
    bounce_rate = np.random.uniform(30, 70, size=7)  # Dummy bounce rate data
    bounce_data = pd.DataFrame({"Datum": dates, "Bounce Rate": bounce_rate})
    fig = px.line(bounce_data, x="Datum", y="Bounce Rate", title="Bounce Rate Trend")
    fig.update_traces(line=dict(color=primaryColor))  # Apply primary color
    st.plotly_chart(fig)

    # 2. Landing Pages Visualization using Plotly
    st.subheader("Populaire Landingpages")
    landing_pages = {
        "Pagina": ["Home", "Producten", "Contact", "Over Ons", "Blog"],
        "Bezoekers": np.random.randint(500, 1500, size=5)  # Dummy visitor data for each landing page
    }
    landing_pages_df = pd.DataFrame(landing_pages)
    fig = px.bar(landing_pages_df, x="Pagina", y="Bezoekers", title="Populaire Landingpages", color_discrete_sequence=[primaryColor])
    st.plotly_chart(fig)

    # 3. Events Visualization using Plotly
    st.subheader("Top Gebeurtenissen (Events) over de Afgelopen Week")
    events = {
        "Event": ["Aanmeldingen", "Video Bekeken", "Download", "Button Klik", "Formulier Ingevuld"],
        "Frequentie": np.random.randint(100, 500, size=5)  # Dummy event frequency data
    }
    events_df = pd.DataFrame(events)
    fig = px.bar(events_df, x="Event", y="Frequentie", title="Top Gebeurtenissen", color_discrete_sequence=[primaryColor])
    st.plotly_chart(fig)

    # 4. Conversion Rate Visualization using Plotly
    st.subheader("Conversies over de Afgelopen Week")
    conversion_rate = np.random.uniform(2, 10, size=7)  # Dummy conversion rate data
    conversion_data = pd.DataFrame({"Datum": dates, "Conversies (%)": conversion_rate})
    fig = px.line(conversion_data, x="Datum", y="Conversies (%)", title="Conversies Trend")
    fig.update_traces(line=dict(color=primaryColor))  # Apply primary color
    st.plotly_chart(fig)

# Content for Google Ads Tab
with tabs[1]:
    st.header("Google Ads")

    # Dummy data for the last 7 days
    dates = pd.date_range(end=datetime.date.today(), periods=7)
    data = pd.DataFrame({
        "Date": dates,
        "Vertoningen": np.random.randint(1000, 5000, size=7),          # Random impressions
        "Vertoningspercentage": np.random.uniform(50, 100, size=7),    # Random impression share in percentage
        "Kliks": np.random.randint(200, 1000, size=7)                  # Random clicks
    })

    # Show Vertoningen (Impressions) trend using Plotly
    st.subheader("Vertoningen (over de Afgelopen Week)")
    fig = px.line(data, x="Date", y="Vertoningen", title="Vertoningen Trend")
    fig.update_traces(line=dict(color=primaryColor))
    st.plotly_chart(fig)

    # Show Vertoningspercentage (Impression Share) trend using Plotly
    st.subheader("Vertoningspercentage (over de Afgelopen Week)")
    fig = px.line(data, x="Date", y="Vertoningspercentage", title="Vertoningspercentage Trend")
    fig.update_traces(line=dict(color=primaryColor))
    st.plotly_chart(fig)

    # Show Kliks (Clicks) trend using Plotly
    st.subheader("Kliks (over de Afgelopen Week)")
    fig = px.line(data, x="Date", y="Kliks", title="Kliks Trend")
    fig.update_traces(line=dict(color=primaryColor))
    st.plotly_chart(fig)

# Content for Facebook Tab
with tabs[2]:
    st.header("Facebook")

    # 1. Engagement Rate using Plotly
    st.subheader("Engagement Rate over de Afgelopen Week")
    engagement_rate = np.random.uniform(2, 10, size=7)  # Dummy engagement rate data
    engagement_data = pd.DataFrame({"Datum": dates, "Engagement Rate (%)": engagement_rate})
    fig = px.line(engagement_data, x="Datum", y="Engagement Rate (%)", title="Engagement Rate Trend")
    fig.update_traces(line=dict(color=primaryColor))
    st.plotly_chart(fig)

    # 2. Post Reach for Top 5 Posts using Plotly
    st.subheader("Bereik van Top 5 Berichten")
    post_reach = {
        "Bericht": [f"Post {i+1}" for i in range(5)],
        "Bereik": np.random.randint(1000, 5000, size=5)  # Dummy reach data
    }
    post_reach_df = pd.DataFrame(post_reach)
    fig = px.bar(post_reach_df, x="Bericht", y="Bereik", title="Top 5 Bereik van Berichten", color_discrete_sequence=[primaryColor])
    st.plotly_chart(fig)

    # 3. Page Followers Trend using Plotly
    st.subheader("Volgers Groei over de Afgelopen Maand")
    follower_dates = pd.date_range(end=datetime.date.today(), periods=30)
    followers = np.cumsum(np.random.randint(10, 50, size=30))  # Dummy followers growth data
    followers_data = pd.DataFrame({"Datum": follower_dates, "Volgers": followers})
    fig = px.line(followers_data, x="Datum", y="Volgers", title="Volgers Groei")
    fig.update_traces(line=dict(color=primaryColor))
    st.plotly_chart(fig)

# Content for Instagram Tab
with tabs[3]:
    st.header("Instagram")

    # 1. Story Views using Plotly
    st.subheader("Trend van Verhaal Weergaven over de Afgelopen Week")
    dates = pd.date_range(end=datetime.date.today(), periods=7)
    story_views = np.random.randint(500, 1500, size=7)  # Dummy story views data
    story_data = pd.DataFrame({"Datum": dates, "Verhaal Weergaven": story_views})
    fig = px.line(story_data, x="Datum", y="Verhaal Weergaven", title="Verhaal Weergaven Trend")
    fig.update_traces(line=dict(color=primaryColor))  # Apply primary color
    st.plotly_chart(fig)

    # 2. Top Performing Posts (Likes) using Plotly
    st.subheader("Top Berichten op Basis van Likes")
    post_likes = {
        "Bericht": [f"Post {i+1}" for i in range(5)],
        "Likes": np.random.randint(100, 1000, size=5)  # Dummy likes data
    }
    post_likes_df = pd.DataFrame(post_likes)
    fig = px.bar(post_likes_df, x="Bericht", y="Likes", title="Top Berichten op Basis van Likes", color_discrete_sequence=[primaryColor])
    st.plotly_chart(fig)

    # 3. Follower Growth using Plotly
    st.subheader("Volgers Groei over de Afgelopen Maand")
    follower_dates = pd.date_range(end=datetime.date.today(), periods=30)
    followers_instagram = np.cumsum(np.random.randint(10, 40, size=30))  # Dummy followers growth data
    followers_data_instagram = pd.DataFrame({"Datum": follower_dates, "Volgers": followers_instagram})
    fig = px.line(followers_data_instagram, x="Datum", y="Volgers", title="Volgers Groei")
    fig.update_traces(line=dict(color=primaryColor))  # Apply primary color
    st.plotly_chart(fig)

# Content for TikTok Tab
with tabs[4]:
    st.header("TikTok")

    # 1. Video Views Trend using Plotly
    st.subheader("Video Weergaven over de Afgelopen Week")
    dates = pd.date_range(end=datetime.date.today(), periods=7)
    video_views = np.random.randint(800, 3000, size=7)  # Dummy video views data
    video_views_data = pd.DataFrame({"Datum": dates, "Video Weergaven": video_views})
    fig = px.line(video_views_data, x="Datum", y="Video Weergaven", title="Video Weergaven Trend")
    fig.update_traces(line=dict(color=primaryColor))  # Apply primary color
    st.plotly_chart(fig)

    # 2. Top Performing Videos (Engagement) using Plotly
    st.subheader("Top Video's op Basis van Engagement")
    video_engagement = {
        "Video": [f"Video {i+1}" for i in range(5)],
        "Engagement": np.random.randint(1000, 5000, size=5)  # Dummy engagement data
    }
    video_engagement_df = pd.DataFrame(video_engagement)
    fig = px.bar(video_engagement_df, x="Video", y="Engagement", title="Top Video's op Basis van Engagement", color_discrete_sequence=[primaryColor])
    st.plotly_chart(fig)

    # 3. New Followers Trend using Plotly
    st.subheader("Nieuwe Volgers over de Afgelopen Week")
    new_followers = np.random.randint(50, 200, size=7)  # Dummy new followers data
    new_followers_data = pd.DataFrame({"Datum": dates, "Nieuwe Volgers": new_followers})
    fig = px.line(new_followers_data, x="Datum", y="Nieuwe Volgers", title="Nieuwe Volgers Trend")
    fig.update_traces(line=dict(color=primaryColor))  # Apply primary color
    st.plotly_chart(fig)

# Catalog of Streamlit Visualizations
with tabs[5]:
    st.header("Visualisatie Catalogus")

    # Generate some example data for use in the visualizations
    dates = pd.date_range(end=datetime.date.today(), periods=30)
    data = pd.DataFrame({
        "Datum": dates,
        "Waarde": np.random.randint(100, 500, size=30)
    })

    # 1. Line Chart using Plotly
    st.subheader("Lijn Grafiek (Line Chart)")
    fig = px.line(data, x="Datum", y="Waarde", title="Lijn Grafiek")
    fig.update_traces(line=dict(color=primaryColor))
    st.plotly_chart(fig)

    # 2. Area Chart using Plotly
    st.subheader("Gebied Grafiek (Area Chart)")
    fig = px.area(data, x="Datum", y="Waarde", title="Gebied Grafiek", color_discrete_sequence=[primaryColor])
    st.plotly_chart(fig)

    # 3. Bar Chart using Plotly
    st.subheader("Staafdiagram (Bar Chart)")
    fig = px.bar(data, x="Datum", y="Waarde", title="Staafdiagram", color_discrete_sequence=[primaryColor])
    st.plotly_chart(fig)

    # 4. Map Chart
    st.subheader("Kaart (Map Chart)")
    map_data = pd.DataFrame({
        'lat': np.random.uniform(-90, 90, 100),
        'lon': np.random.uniform(-180, 180, 100)
    })
    st.map(map_data)

    # 5. Histogram using Plotly
    st.subheader("Histogram")
    hist_data = np.random.normal(50, 15, 1000)
    fig = px.histogram(pd.DataFrame(hist_data, columns=['Waarde']), x="Waarde", title="Histogram", color_discrete_sequence=[primaryColor])
    st.plotly_chart(fig)

    # 6. Scatter Plot using Plotly
    st.subheader("Spreidingsdiagram (Scatter Plot)")
    scatter_data = pd.DataFrame({
        "x": np.random.randn(100),
        "y": np.random.randn(100)
    })
    fig = px.scatter(scatter_data, x="x", y="y", title="Spreidingsdiagram met Plotly", color_discrete_sequence=[primaryColor])
    st.plotly_chart(fig)

    # 7. Pie Chart using Matplotlib
    st.subheader("Taartdiagram (Pie Chart)")
    pie_data = pd.Series([50, 30, 20], index=["Categorie A", "Categorie B", "Categorie C"], name="Waarde")
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90, colors=[primaryColor, "#FAD02E", "#000000"])
    st.pyplot(fig)