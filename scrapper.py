from bs4 import BeautifulSoup
import json

# Read the index.html file
with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all divs with class "upcoming-events-item"
events = soup.find_all('div', class_='upcoming-events-item')

# List to hold event data
events_data = []

# Iterate over each event div
for event in events:
    # Initialize event details
    event_details = {}
    
    # Find the image link
    img = event.find('img', class_='js-img')
    if img and img.has_attr('src'):
        event_details['img_src'] = img['src']
    else:
        event_details['img_src'] = ' '
    
    # Find the date
    date_span = event.find('span', class_='upcoming-events-item__dates')
    event_details['date'] = date_span.text if date_span else ' '
    
    # Find the title
    title_span = event.find('span', class_='upcoming-events-item__title')
    event_details['title'] = title_span.text if title_span else ' '
    
    # Find the tag
    tag_span = event.find('span', class_='upcoming-events-item__tag')
    event_details['upcomingevents'] = tag_span.text if tag_span else ' '
    
    # Add the event details to the list
    events_data.append(event_details)

# Write the event data to a JSON file
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(events_data, json_file, ensure_ascii=False, indent=4)

print(events_data)
