import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Wireless Frequency Monitor", page_icon=":vibration_mode:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

Lottie1 = load_lottie_url("https://lottie.host/f7f9b5f6-e9d8-4b72-8d80-90a6e857788a/cEgUDUjXxB.json")#Purple
Lottie2 = load_lottie_url("https://lottie.host/737052d4-6263-46ac-a0d8-bc11c53839ce/5zvEr3VVx1.json")#Thin
Lottie3 = load_lottie_url("https://lottie.host/5bd0537f-12d4-4619-a9af-b5847e26335a/MWYK7Nh17P.json")#Yellow
Lottie4 = load_lottie_url("https://lottie.host/17c74452-f12e-4780-9b8b-33d8cea05dd2/Y8gXYgLOXg.json")#big wave
Lottie5 = load_lottie_url("https://lottie.host/b22ff990-1979-4045-a9ca-5d497018607c/6IVsWVYQyt.json")#Switch on Blt
Lottie6 = load_lottie_url("https://lottie.host/cc535049-e2da-4957-ae6c-dfaf1514e15b/oshJli4JW8.json")#Blt Device
Lottie7 = load_lottie_url("https://lottie.host/dfdc9966-fc1f-4cbe-a41a-82641a5f14b2/wfZxuqSaKs.json")#Multiple Fx
Lottie8 = load_lottie_url("https://lottie.host/55e7d8bd-7fd9-49de-94c6-42711b7ea19b/5Ps5QIdaXW.json")#Blt logo
lottie9 = load_lottie_url("https://lottie.host/3a8cf170-72cd-48a1-b649-98ef38c28757/fALgLT26Ms.json")#Engineers
lottie10 = load_lottie_url("https://lottie.host/435f6294-4ad0-4f30-922b-59507615507e/sgc5QvZHcd.json")#Safety
lottie11 = load_lottie_url("https://lottie.host/a722fbce-9063-4aa9-9212-7ddeb9962d0a/FGtnJP3vMi.json")#Space
img1 = Image.open("images/photo_2024-04-16_15-48-28.jpg")  # pic
img2 = Image.open("images/photo_2024-04-16_15-45-14.jpg")  # ios
img3 = Image.open("images/photo_2024-04-16_15-45-16.jpg")  # ios
img4 = Image.open("images/photo_2024-04-16_15-45-19.jpg")  # andr
img5 = Image.open("images/image_2024-04-16_15-46-38.png")  # diag

# header
st.title("Wireless Frequency Monitor")
st.subheader("Project For Module 5FTC - 1439 Project Management and Product Development, Project based on Arduino and Bluetooth Low Energy Edition for Frequency Monitoring and Wireless Communication")
left_column, right_column = st.columns(2)
with left_column:
    st.write("##")
    st.write("Project Members")
    st.write("##")
    st.write("Project Manager  : Linuk Perera")
    st.write("Project Analyst  : Neleesha Nulundeniya")
    st.write("Project Planner  : Induwara Weerasekara")
    st.write("Project Marketer : Mihijaya Kumarasiri")
with right_column:
    st_lottie(load_lottie_url("https://lottie.host/5bd0537f-12d4-4619-a9af-b5847e26335a/MWYK7Nh17P.json"), height = 300, key = "Lottie3")


#User Manual
st.write("---")
st.header("How To Use the Wireless Frequency Monitor")
st.write("##")
st.write("A step by step guid to use our system")
left_column, right_column = st.columns(2)
with left_column:
    st.write("##")
    st.write("Follow 3 Easy steps to Measure Frequency of Any Voltage Source")
    st.write("Prerequisites Include")
    st.write("1 An Android or IOS Device that Supports Bluetooth")
    st.write("2 Installation od the DSD Bluetooth Application")

with right_column:
    st_lottie(load_lottie_url("https://lottie.host/f7f9b5f6-e9d8-4b72-8d80-90a6e857788a/cEgUDUjXxB.json"), height = 200, key = "coding")


st.write("##")
st.subheader("Step 1 - Switch on Bluetooth in Your Android or IOS Device")
st.write("##")
st_lottie(load_lottie_url("https://lottie.host/b22ff990-1979-4045-a9ca-5d497018607c/6IVsWVYQyt.json"), height = 300, key = "Lottie5")
st.subheader("Step 2 - Connect Your Device to the HM - 10 Through the DSD App")
st.write("##")
st_lottie(load_lottie_url("https://lottie.host/cc535049-e2da-4957-ae6c-dfaf1514e15b/oshJli4JW8.json"), height = 300, key = "Lottie6")
st.subheader("Step 3 - Observe Frequency Data Through Your Mobile Device")
st.write("##")
st_lottie(load_lottie_url("https://lottie.host/dfdc9966-fc1f-4cbe-a41a-82641a5f14b2/wfZxuqSaKs.json"), height = 300, key = "Lottie7")






#Mission
st.write("---")
st.header("Our Mission")
st.subheader("To Create A Safe Working Environment")
st.write("##")
st_lottie(load_lottie_url("https://lottie.host/435f6294-4ad0-4f30-922b-59507615507e/sgc5QvZHcd.json"), height = 300, key = "Lottie9")
st.subheader("To Create A Reliable Yet Affordable Product")
st.write("##")
st_lottie(load_lottie_url("https://lottie.host/3a8cf170-72cd-48a1-b649-98ef38c28757/fALgLT26Ms.json"), height = 300, key = "Lottie10")
st.subheader("To Provide Wide Functionality Through our Product")
st.write("##")
st_lottie(load_lottie_url("https://lottie.host/a722fbce-9063-4aa9-9212-7ddeb9962d0a/FGtnJP3vMi.json"), height = 300, key = "Lottie11")





#Physical Implementation
st.write("---")
st.header("Physical Implementation")
st.subheader("This is an Overview of the Actual Project and its Circuitry")
st.write("")
image_column, text_column = st.columns((2, 1))
with image_column:
    st.image(img1)
with text_column:
    st.write("Project For 5FTC - 1439 Project Management abd Product Development, Project based on Arduino and Bluetooth Low Energy Edition")
    st.write("##")
    st.write("Refer Project Physical Implementation")





#Project Outputs
st.write("---")
st.header("Project Outputs")
st.subheader("IOS Output Interface")
st.subheader("Request For Standard Deviation")

left_column, right_column = st.columns(2)
with left_column:
    st.image(img2)
    st.subheader("Request For Frequency")
    st.image(img3)
with right_column:
    st.write("View of system User Interface")
    st.write("IOS Output Interface can be seen to the Left, Request For Standard Deviation is prompt with the input of 'Sd 'and Request For Frequency is Promp from the input of 'F'")
    st.write("Bluetooth Low Energy (BLE) mode is revolutionizing telecommunications applications for mobile devices engineered for engineers. Its low power consumption and short-range communication capabilities make it an ideal choice for connecting engineering tools and equipment wirelessly. Whether it's transmitting data from sensors in industrial machinery or enabling real-time communication between handheld devices and control systems, BLE facilitates seamless connectivity while conserving battery life. Engineers can leverage BLE to create efficient and reliable solutions for monitoring, control, and data acquisition in various industries, including manufacturing, automotive, and healthcare. With BLE, engineers can develop mobile applications that offer unparalleled flexibility and convenience, empowering users to interact with their equipment and systems in innovative ways.")
    st.write("1. Low Power Consumption: BLE is optimized for low power consumption, making it ideal for battery-operated devices. It achieves this by reducing the duty cycle and maintaining short connection intervals, allowing devices to operate for months or even years on a single coin cell battery.")
    st.write("2. Short Range Communication: Similar to traditional Bluetooth, BLE operates in the 2.4 GHz ISM band but with a shorter range, typically up to 100 meters. This short-range communication is suitable for applications where devices need to communicate within a localized area, such as wearables, sensors, and smart home devices.")
    st.write("3. Fast Connection and Data Transfer: BLE devices can establish connections quickly and transfer small amounts of data efficiently. This makes it suitable for applications that require periodic data exchange, such as health and fitness trackers, smart watches, and proximity sensors.")
    st.write("4. Advertising and Scanning: BLE devices can operate in advertising or scanning modes. Advertising mode allows devices to broadcast data packets, while scanning mode enables other devices to discover and connect to nearby BLE devices. This enables efficient discovery and communication between devices in a BLE network.")
    st.write("5. Peripheral and Central Roles: In a BLE network, devices can operate in peripheral or central roles. Peripheral devices typically broadcast data and respond to requests from central devices, while central devices scan for nearby peripherals and initiate connections. This flexible architecture allows for various device configurations and communication patterns.")
    st.write("6. Security: BLE incorporates security features such as encryption and authentication to protect data transmission between devices. This ensures data privacy and integrity, making BLE suitable for applications that handle sensitive information, such as medical devices and industrial sensors.")
    st.write("7. Interoperability: BLE is a standardized technology maintained by the Bluetooth Special Interest Group (SIG), ensuring interoperability between different devices and manufacturers. This standardization allows developers to create BLE-enabled products and applications that can communicate seamlessly with other BLE devices")

st.subheader("Android Output Interface")
left_column, right_column = st.columns(2)
with left_column:
    st.image(img4)
with right_column:
    st.write("Functions Being Called for on the Android Interface Can be seen on the Left")




#Diagram
st.write("---")
st.header("System Diagram")
st.subheader("The Circuit Diagram of The Implemented System")

left_column, right_column = st.columns(2)
with left_column:
    st.image(img5)
with right_column:
    st.write("The circuitry is basically a Programmed Arduino Uno board Connected to a HM - 10 Bluetooth Module")
    st_lottie(load_lottie_url("https://lottie.host/55e7d8bd-7fd9-49de-94c6-42711b7ea19b/5Ps5QIdaXW.json"), height = 150, key = "Lottie8")
    st.write("Bluetooth Low Energy was used due to its high energy Efficiency and Compatibility")
    st.write("Wiring choices are Intentional, to give a maximum output from the implemented system")




#Submission Portal
st.write("---")
st.header("To contact the development team use the below Submission Portal")
st.write("Fill all 3 boxes")
form = """<form action="https://formsubmit.co/linukperera402@gmail.com" method="POST">
    <input type = "hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name = "message" placeholder= "Your Message Here" required></textarea>
     <button type="submit">Send</button>
</form>"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(form, unsafe_allow_html=True)
with right_column:
    st_lottie(load_lottie_url("https://lottie.host/737052d4-6263-46ac-a0d8-bc11c53839ce/5zvEr3VVx1.json"), height = 300, key = "Lottie2")

st_lottie(load_lottie_url("https://lottie.host/17c74452-f12e-4780-9b8b-33d8cea05dd2/Y8gXYgLOXg.json"), height = 300, key = "Lottie4")
