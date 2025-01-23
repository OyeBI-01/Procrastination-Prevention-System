# Procrastination-Prevention-System
The Procrastination Prevention System is an intelligent application designed to help users stay productive and focused. By leveraging AI-powered tools, automated screen captures, and notifications, this system helps prevent distractions and ensures users stay on track with their goals.

## Features
## 1. User Intention Parsing

• Collect user intentions through the command line

• Summarize the user's intentions using a pre-trained T5 summarization model

## 2. Automated Screen Capture

• Capture screenshots at regular intervals

• Save screenshots in a designated directory for later analysis

## 3. Procrastination Alerts
• Send desktop notifications when the user deviates from their stated intentions

## 4. Screenshot Classification
• Classify screenshots using a zero-shot classification model (BART)

• Detect whether screenshots are work-related or entertainment-related

## 5. Log Analytics Dashboard
• Visualize system events, including screen captures and notifications.

• Generate charts for insights such as: 
                                        -Frequency of different event types

                                        -Timing of screenshots

## File Structure

.
├── main.py                # Main application script

├── analytics_dashboard.py # Analytics dashboard script

├── analytics.csv          # Log file for events

├── requirements.txt       # Dependencies

├── screenshots/           # Directory for saved screenshots

└── README.md              # Project documentation


## Logging
The application logs all activities to app.log:

• User inputs

• Notifications sent

• Screenshots captured

• Errors and exceptions


## Analytics
The analytics dashboard visualizes logged events from analytics.csv. Key insights include:
• Breakdown of event types (e.g., screenshots, notifications)

• Times of screenshot captures

## Contact
For questions or feedback, please contact Blessing Oyewole at oyewoleblessing10@gmail.com.
