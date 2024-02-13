from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from send_birthday_message import send_birthday_wishes

class BirthdayWishesApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.recipient_name_input = TextInput(hint_text='Recipient Name')
        self.birthday_message_input = TextInput(hint_text='Birthday Message')
        self.send_button = Button(text='Send Birthday Wishes')
        self.send_button.bind(on_press=self.send_birthday_wishes)
        self.layout.add_widget(self.recipient_name_input)
        self.layout.add_widget(self.birthday_message_input)
        self.layout.add_widget(self.send_button)
        return self.layout

    def send_birthday_wishes(self, instance):
        recipient_name = self.recipient_name_input.text
        birthday_message = self.birthday_message_input.text
        send_birthday_wishes( recipient_name , birthday_message)

if __name__ == '__main__':
    BirthdayWishesApp().run()
