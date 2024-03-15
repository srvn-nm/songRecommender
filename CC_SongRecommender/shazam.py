# noinspection PyCompatibility
def recognize_song_shazam(audio_file_path):
    import requests

    url = "https://shazam-api-free.p.rapidapi.com/shazam/recognize/"

    payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"{audio_file_path}\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        "content-type": "multipart/form-data; boundary=---011000010111000001101001",
        "X-RapidAPI-Key": "4f572370c6mshea36af5374dcaa6p10e8ddjsn40a8eb8b2bf2",
        "X-RapidAPI-Host": "shazam-api-free.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()
