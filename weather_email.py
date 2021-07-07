import smtplib
import ssl


def send_message(message, sender_email, receiver_email, password):
    """Sends an email using an email provider

    Parameters
    ----------
    message : str
        The message to display to the recipient in the body of the email.
    sender_email : str
        The sender's email address the email will be sent from.
    receiver_email : str
        The recipient's email address the email will be sent to.
    password : str
        Password of the sender's email account.
    """

    # Outgoing email provider settings (Gmail)
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    context = ssl.create_default_context()

    # Send email to recipient
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
