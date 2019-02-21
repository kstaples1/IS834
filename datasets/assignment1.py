
a = "Dear {}, \n\nThank you for taking the time to reach out. Attached below is my schedule. Please create a new event with me and then confirm via email or via text 1 hour before the meeting. If you have any questions feel free to ask. I look forward to meeting with you. \n\nSincerely, \n\nKyle Staples \n\nhttps://calendar.google.com/calendar/embed?src=kyle.staples97%40gmail.com&ctz=America%2FNew_York \n"
list = ["Charisma", "Jay", "Rebecca", "Kayla", "Ethan", "Richard", "Tony", "Henry"]

for name in list:
    print(a.format(name))
