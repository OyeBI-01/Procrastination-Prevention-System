import argparse
import logging
import os
import time
from transformers import pipeline
import pyautogui
from plyer import notification
import csv

# Configure logging
logging.basicConfig(
    filename="app.log",         # Log messages will be saved in 'app.log'
    level=logging.DEBUG,        # Log level set to DEBUG to capture detailed information
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format
)

ANALYTICS_FILE = "analytics.csv"

# Initialize analytics file
if not os.path.exists(ANALYTICS_FILE):
    with open(ANALYTICS_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Type", "Data1", "Data2", "Data3"])

def log_analytics(event_type, data1=None, data2=None, data3=None):
    """Logs analytics data to a CSV file."""
    try:
        with open(ANALYTICS_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), event_type, data1, data2, data3])
        logging.info(f"Logged analytics data: {event_type}, {data1}, {data2}, {data3}")
    except Exception as e:
        logging.error("Error logging analytics data", exc_info=True)


def collect_user_input():
    """Collects user input using argparse."""
    logging.info("Collecting user input.")
    parser = argparse.ArgumentParser(description="Procrastination Prevention System")
    parser.add_argument("--intention", type=str, required=True, help="Describe your intended activities.")
    args = parser.parse_args()
    logging.debug(f"User input collected: {args.intention}")
    log_analytics("Intent", data1=args.intention)
    return args.intention


def parse_intention(intention):
    """Parses user intention using a summarization model."""
    try:
        logging.info("Initializing the summarizer model.")
        summarizer = pipeline("summarization", model="t5-small")
        logging.debug("Summarizer model loaded successfully.")
        summary = summarizer(intention, max_length=30, min_length=10, do_sample=False)
        parsed = summary[0]['summary_text']
        logging.info("Intention parsed successfully.")
        log_analytics("Parsed Intent", data1=intention, data2=parsed)
        return parsed
    except Exception as e:
        logging.error("Error in parse_intention", exc_info=True)
        raise


def capture_screen(interval=300, output_dir="screenshots"):
    """Captures the screen at regular intervals."""
    try:
        logging.info(f"Setting up screen capture with interval: {interval}s and output directory: {output_dir}.")
        os.makedirs(output_dir, exist_ok=True)
        while True:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"{output_dir}/screenshot_{timestamp}.png"
            pyautogui.screenshot(screenshot_path)
            logging.info(f"Captured screenshot: {screenshot_path}")
            log_analytics("Screenshot", data1=screenshot_path)
            time.sleep(interval)
    except Exception as e:
        logging.error("Error in capture_screen", exc_info=True)
        raise


def classify_screenshot(image_path):
    """Classifies a screenshot using a zero-shot classification model."""
    try:
        logging.info(f"Classifying screenshot: {image_path}")
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        labels = ["work-related", "entertainment"]
        with open(image_path, "rb") as img:
            results = classifier(img.read(), labels)
        logging.info(f"Classification results: {results}")
        log_analytics("Classification", data1=image_path, data2=results['labels'][0], data3=results['scores'][0])
        return results
    except Exception as e:
        logging.error("Error in classify_screenshot", exc_info=True)
        raise


def send_notification(message):
    """Sends a notification to the user."""
    try:
        logging.info(f"Sending notification: {message}")
        notification.notify(
            title="Procrastination Alert!",
            message=message,
            app_name="Procrastination Prevention System",
        )
        log_analytics("Notification", data1=message)
    except Exception as e:
        logging.error("Error in send_notification", exc_info=True)
        raise


if __name__ == "__main__":
    try:
        # Collect user intention
        user_intention = collect_user_input()
        logging.info(f"User Intention: {user_intention}")

        # Parse user intention
        parsed_intention = parse_intention(user_intention)
        logging.info(f"Parsed Intention: {parsed_intention}")

        # Send a notification
        send_notification("You're off track! Focus on your coding tasks.")

        # Start capturing screenshots (adjust interval as needed)
        capture_screen(interval=60)  # Example: take screenshots every 60 seconds

    except Exception as e:
        logging.critical("Unhandled exception in the application", exc_info=True)
