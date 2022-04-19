from abc import ABC, abstractmethod


class BaseCommand(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError("Please implement in subclass")


class EMailCommand(BaseCommand):
    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.send_email(self.data)


class SMSCommand(object):
    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.send_sms(self.data)


class NotificationService(object):
    def send_email(self, data):
        print("Sending Email", data)

    def send_sms(self, data):
        print("Sending SMS", data)


class NotificationInvoker(object):
    def __init__(self):
        self.notification_history = []

    def invoke(self, command):
        self.notification_history.append(command)
        command.execute()


if __name__ == "__main__":
    invoker = NotificationInvoker()
    sender = NotificationService()
    invoker.invoke(EMailCommand(sender, {"subject": "Test Email"}))
    invoker.invoke(SMSCommand(sender, {"subject": "Test SMS"}))
    print(invoker.notification_history)
