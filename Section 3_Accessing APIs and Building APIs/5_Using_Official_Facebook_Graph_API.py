import requests

with open(
    "Section 3_Accessing APIs and Building APIs\\FaceBookAccessToken_APIKey.txt", "r"
) as f:
    accesstoken = f.read()

url = f"https://graph.facebook.com/v16.0/me?fields=id%2Cname&access_token={accesstoken}"


def main():
    response = requests.get(url)
    print(response.json())


if __name__ == "__main__":
    main()
