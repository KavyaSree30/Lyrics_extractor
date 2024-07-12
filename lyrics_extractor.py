import requests

class SongLyrics:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.genius.com"
    
    def search_song(self, song_name):
        endpoint = "/search"
        url = f"{self.base_url}{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        params = {
            'q': song_name
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise HTTP errors if any
            
            response_json = response.json()
            if 'response' in response_json and 'hits' in response_json['response']:
                return response_json['response']['hits']
            else:
                return []
        
        except requests.exceptions.RequestException as e:
            print(f"Error searching song: {str(e)}")
            return []

    def get_lyrics(self, song_id):
        endpoint = f"/songs/{song_id}"
        url = f"{self.base_url}{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise HTTP errors if any
            
            response_json = response.json()
            if 'response' in response_json and 'song' in response_json['response']:
                if 'lyrics' in response_json['response']['song']:
                    return response_json['response']['song']['lyrics']
                else:
                    return 'Lyrics not found'
            else:
                return 'Lyrics not found'
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching lyrics: {str(e)}")
            return 'Lyrics not found'
