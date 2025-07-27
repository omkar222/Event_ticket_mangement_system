import streamlit as st
import requests
from datetime import datetime

# Configuration
BASE_URL = "http://localhost:5000"
st.set_page_config(page_title="Event Ticket System", layout="wide")

def create_event_section():
    st.header("🎭 Create New Event")
    with st.form("event_form"):
        name = st.text_input("Event Name*")
        date = st.date_input("Date*")
        time = st.time_input("Time*")
        location = st.text_input("Location")
        description = st.text_area("Description")
        
        if st.form_submit_button("Create Event"):
            if not name:
                st.warning("Event name is required")
            else:
                event_datetime = datetime.combine(date, time).isoformat()
                response = requests.post(
                    f"{BASE_URL}/api/events",
                    json={
                        "name": name,
                        "date": event_datetime,
                        "location": location,
                        "description": description
                    }
                )
                if response.status_code == 201:
                    st.success("Event created successfully!")
                else:
                    st.error(f"Error: {response.json().get('message')}")

def generate_tickets_section():
    st.header("🎫 Generate Tickets")
    col1, col2 = st.columns(2)
    
    with col1:
        # Get existing events
        events = requests.get(f"{BASE_URL}/api/events").json()
        event_options = {e['id']: e['name'] for e in events.get('data', [])}
        
        selected_event = st.selectbox(
            "Select Event",
            options=list(event_options.keys()),
            format_func=lambda x: event_options[x]
        )
        
        quantity = st.number_input("Number of Tickets", min_value=1, max_value=100, value=1)
    
    with col2:
        if st.button("Generate Tickets"):
            with st.spinner("Generating tickets..."):
                # Get event details first
                event_response = requests.get(f"{BASE_URL}/api/events/{selected_event}")
                event_data = event_response.json()
                
                # Generate tickets
                ticket_response = requests.post(
                    f"{BASE_URL}/api/tickets/{selected_event}/generate",
                    json={"quantity": quantity}
                )
                
                if ticket_response.status_code == 201:
                    tickets = ticket_response.json()['data']
                    st.success(f"Generated {quantity} tickets for {event_data['data']['name']}!")
                    
                    # Format ticket data with event details
                    ticket_output = []
                    ticket_output.append("=== EVENT DETAILS ===")
                    ticket_output.append(f"Event: {event_data['data']['name']}")
                    ticket_output.append(f"Date: {event_data['data']['date']}")
                    ticket_output.append(f"Location: {event_data['data'].get('location', 'N/A')}")
                    ticket_output.append(f"Description: {event_data['data'].get('description', 'None')}")
                    ticket_output.append("\n=== TICKET TOKENS ===")
                    ticket_output.extend([t['token'] for t in tickets])
                    
                    # Display in expandable section
                    with st.expander("📄 View Tickets with Event Details"):
                        st.code("\n".join(ticket_output))
                    
                    # Download option
                    st.download_button(
                        "💾 Download Tickets with Event Info",
                        data="\n".join(ticket_output),
                        file_name=f"tickets_{event_data['data']['name'].replace(' ','_')}.txt",
                        help="Download includes both event details and ticket tokens"
                    )
                    
                  
                else:
                    st.error(f"Error generating tickets: {ticket_response.text}")

def redeem_ticket_section():
    st.header("✅ Redeem Tickets")
    token = st.text_input("Enter Ticket Token", key="redeem_input")
    
    if st.button("Check & Redeem"):
        if not token:
            st.warning("Please enter a ticket token")
        else:
            # First check current status
            status_response = requests.get(f"{BASE_URL}/api/tickets/{token}")
            status_data = status_response.json()
            
            if status_response.status_code == 200:
                if status_data['data']['is_redeemed']:
                    st.error("❌ This ticket was already redeemed")
                    st.write(f"Redeemed at: {status_data['data'].get('redeemed_at', 'Unknown time')}")
                else:
                    # Attempt redemption if not redeemed
                    redeem_response = requests.post(f"{BASE_URL}/api/tickets/{token}/redeem")
                    redeem_data = redeem_response.json()
                    
                    if redeem_response.status_code == 200:
                        st.success("✅ Ticket successfully redeemed!")
                    else:
                        st.error(f"Redemption failed: {redeem_data.get('message')}")
                
                # Show ticket details in expandable section
                with st.expander("Ticket Details"):
                    st.json(status_data['data'])
            
            elif status_response.status_code == 404:
                st.error("Ticket not found - invalid token")
            else:
                st.error(f"Error: {status_data.get('message')}")

def main():
    st.title("🎟️ Event Ticket Management System")
    
    menu_option = st.sidebar.selectbox(
        "Menu",
        ["Create Event", "Generate Tickets", "Redeem Tickets"]
    )
    
    if menu_option == "Create Event":
        create_event_section()
    elif menu_option == "Generate Tickets":
        generate_tickets_section()
    elif menu_option == "Redeem Tickets":
        redeem_ticket_section()

if __name__ == "__main__":
    main()