import requests


# noinspection PyCompatibility
def send_email_with_firebase(to_email, subject, text):
    url = "https://send-mail-serverless.p.rapidapi.com/send"

    payload = {
        "personalizations": [{"to": [
            {
                "email": to_email,
                "name": "Recipient name"
            }
        ]}],
        "from": {
            "email": "test@firebese.com",
            "name": "Firebese Test Use"
        },
        "reply_to": {
            "email": "test@firebese.com",
            "name": "Firebese Test User"
        },
        "subject": subject,
        "content": [
            {
                "type": "text/html",
                "value": "Hello User <b>Html</b>"
            },
            {
                "type": "text/plan",
                "value": text
            }
        ],
        "headers": {
            "List-Unsubscribe": "<mailto: unsubscribe@firebese.com?subject=unsubscribe>, <https://firebese.com/unsubscribe/id>"}
    }
    headers = {
        "content-type": "application/json",
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "4f572370c6mshea36af5374dcaa6p10e8ddjsn40a8eb8b2bf2",
        "X-RapidAPI-Host": "send-mail-serverless.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()
