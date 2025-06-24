import abc

class Notification(abc.ABC):
    @abc.abstractmethod
    def notify(self):
        """Send a notification"""

class SMS(Notification):
    def __init__(self):
        self.recepient = "+1-555-SMS-DEFAULT"
        self.message = "Default SMS: Your item has shipped!"

    def notify(self):
        print(f"SMS Sent to: {self.recepient}, Message: '{self.message}'")


class Email(Notification):
    def __init__(self):
        self.recepient = "default@example.com"
        self.subject = "Default Email Subject"
        self.message = "This is a pre-defined email message."
        self.attachment = "no_attachment.pdf"

    def notify(self):
        print(f"Email Sent to: {self.recepient}")
        print(f"Subject: '{self.subject}'")
        print(f"Message: '{self.message}'")
        print(f"Attachment: '{self.attachment}'")

class PushNotification(Notification):
    def __init__(self):
        self.device_token = "DEV-TOKEN-DEFAULT-123"
        self.title = "Default Push Title"
        self.message = "You have a new default push notification!"
        self.payload = {"type": "info"}

    def notify(self):
        print(f"Push Notification Sent to Device: {self.device_token}")
        print(f"Title: '{self.title}'")
        print(f"Message: '{self.message}'")
        if self.payload:
            print(f"Payload: {self.payload}")

class NotificationCreator(abc.ABC):
    @abc.abstractmethod
    def create_notification(self) -> Notification:
        """Factory method"""
        pass

class SMSCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SMS()

class EmailCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return Email()

class PushNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return PushNotification()


# --- Main Application Logic ---
if __name__ == "__main__":
    print("Choose a notification type:")
    print("1. SMS")
    print("2. Email")
    print("3. Push")
    choice = input("Enter number (1, 2, or 3): ").strip()

    creator: NotificationCreator = None

    if choice == "1":
        creator = SMSCreator()
    elif choice == "2":
        creator = EmailCreator()
    elif choice == "3":
        creator = PushNotificationCreator()
    else:
        print("Invalid choice. Cannot create notification.")
        exit()

    print("\n--- Requesting Notification from Factory ---")
    notification_object = creator.create_notification()

    print("\n--- Sending Notification ---")
    notification_object.notify()

    print("\nNotification process complete.")