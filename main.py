from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import requests
from io import BytesIO
from kivy.core.image import Image as CoreImage
import os


config = {
    "api_url": "http://localhost:8111/api/images",
    "timeout_slide": 5
}

class SlideshowApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_textures = []
        self.current_image_index = 0
        self.image_widget = None

    def build(self):
        layout = BoxLayout(orientation='horizontal')
        
        self.image_widget = Image(source='', allow_stretch=True)
        layout.add_widget(self.image_widget)
        
        self.fetch_and_preload_images()
        
        return layout

    def fetch_and_preload_images(self):
        try:
            response = requests.get(config["api_url"])
            response.raise_for_status()
            data = response.json()
            image_urls = data.get('images', [])
            
            supported_formats = ('.png', '.jpg', '.jpeg', '.gif')
            filtered_urls = [url for url in image_urls if url.lower().endswith(supported_formats)]
            
            if not filtered_urls:
                return
            
            for url in filtered_urls:
                try:
                    img_response = requests.get(url, timeout=10)
                    img_response.raise_for_status()
                    img_data = BytesIO(img_response.content)
                    core_image = CoreImage(img_data, ext=url.split('.')[-1].lower())
                    self.image_textures.append(core_image.texture)
                except Exception as e:
                    print(f'Ошибка загрузки {url}: {str(e)}')
                    continue
            
            if self.image_textures:
                self.image_widget.texture = self.image_textures[0]
                Clock.schedule_interval(self.switch_image, config["timeout_slide"])

                
        except Exception as e:
            print(f'Ошибка загрузки списка: {str(e)}')

    def switch_image(self, dt):
        if not self.image_textures:
            return
        self.current_image_index = (self.current_image_index + 1) % len(self.image_textures)
        self.image_widget.texture = self.image_textures[self.current_image_index]

if __name__ == '__main__':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
    SlideshowApp().run()